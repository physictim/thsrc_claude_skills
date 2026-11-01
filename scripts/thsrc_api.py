#!/usr/bin/env python3
"""
台灣高鐵 TDX API 查詢工具
用於查詢高鐵時刻表、班次狀態和座位信息
"""
import asyncio
import httpx
import os
import sys
import json
from datetime import datetime, timedelta
from typing import Dict, Any, Optional

class THSRAPIClient:
    """台灣高鐵 API 客戶端"""

    # 車站映射表
    STATION_NAME_TO_ID = {
        "南港": "0990", "台北": "1000", "臺北": "1000", "板橋": "1010",
        "桃園": "1020", "新竹": "1030", "苗栗": "1035",
        "台中": "1040", "臺中": "1040", "彰化": "1043", "雲林": "1047",
        "嘉義": "1050", "台南": "1060", "臺南": "1060", "左營": "1070",
        "高雄": "1070",  # 別名
        # 簡體字也認得
        "板桥": "1010", "桃园": "1020", "云林": "1047", "嘉义": "1050", "左营": "1070",
    }

    STATION_EN_TO_ID = {
        "Nangang": "0990", "Taipei": "1000", "Banqiao": "1010",
        "Taoyuan": "1020", "Hsinchu": "1030", "Miaoli": "1035",
        "Taichung": "1040", "Changhua": "1043", "Yunlin": "1047",
        "Chiayi": "1050", "Tainan": "1060", "Zuoying": "1070"
    }

    def __init__(self, client_id: str, client_secret: str):
        self.client_id = client_id
        self.client_secret = client_secret
        self.access_token = None
        self.token_expires = None
        self.base_url = "https://tdx.transportdata.tw/api/basic/v2"

    def normalize_station(self, station: str) -> str:
        """將站名或ID轉換爲標準站點ID"""
        # 如果已經是ID格式，直接返回
        if station.isdigit() and len(station) == 4:
            return station

        # 嘗試中文站名
        if station in self.STATION_NAME_TO_ID:
            return self.STATION_NAME_TO_ID[station]

        # 嘗試英文站名
        if station in self.STATION_EN_TO_ID:
            return self.STATION_EN_TO_ID[station]

        raise ValueError(f"無效的車站名稱或ID: {station}")

    async def get_access_token(self) -> str:
        """取得或更新 Access Token"""
        if self.access_token and self.token_expires and datetime.now() < self.token_expires:
            return self.access_token

        async with httpx.AsyncClient() as client:
            response = await client.post(
                "https://tdx.transportdata.tw/auth/realms/TDXConnect/protocol/openid-connect/token",
                headers={"content-type": "application/x-www-form-urlencoded"},
                data={
                    "grant_type": "client_credentials",
                    "client_id": self.client_id,
                    "client_secret": self.client_secret
                }
            )

        token_data = response.json()
        self.access_token = token_data["access_token"]
        expires_in = token_data.get("expires_in", 3600)
        self.token_expires = datetime.now() + timedelta(seconds=expires_in - 60)

        return self.access_token

    async def api_request(self, endpoint: str, params: Dict = None) -> Dict[str, Any]:
        """通用 API 請求方法"""
        token = await self.get_access_token()
        headers = {
            "authorization": f"Bearer {token}",
            "Accept-Encoding": "gzip"
        }

        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.get(
                f"{self.base_url}/{endpoint}",
                headers=headers,
                params=params or {}
            )
            response.raise_for_status()
            return response.json()

    async def get_stations(self) -> Dict[str, Any]:
        """取得台灣高鐵車站列表"""
        return await self.api_request("Rail/THSR/Station")

    async def get_timetable(
        self,
        origin_station: str,
        destination_station: str,
        travel_date: str
    ) -> Dict[str, Any]:
        """
        查詢高鐵時刻表

        Args:
            origin_station: 起站（支持中文、英文或ID）
            destination_station: 迄站（支持中文、英文或ID）
            travel_date: 乘車日期 (YYYY-MM-DD)
        """
        origin_id = self.normalize_station(origin_station)
        dest_id = self.normalize_station(destination_station)
        endpoint = f"Rail/THSR/DailyTimetable/OD/{origin_id}/to/{dest_id}/{travel_date}"
        return await self.api_request(endpoint)

    async def get_live_schedule(self, station: str) -> Dict[str, Any]:
        """
        取得指定車站即時時刻表

        Args:
            station: 車站名稱或ID
        """
        station_id = self.normalize_station(station)
        endpoint = f"Rail/THSR/LiveBoard/Station/{station_id}"
        return await self.api_request(endpoint)

    async def get_train_info(self, train_no: str, travel_date: str) -> Dict[str, Any]:
        """
        查詢特定班次資訊

        Args:
            train_no: 車次號碼（例如：823）
            travel_date: 乘車日期 (YYYY-MM-DD)
        """
        endpoint = f"Rail/THSR/DailyTimetable/TrainNo/{train_no}/{travel_date}"
        return await self.api_request(endpoint)

    async def get_available_seats(
        self,
        origin_station: str,
        destination_station: str,
        train_date: str
    ) -> Dict[str, Any]:
        """
        查詢剩餘座位狀態

        Args:
            origin_station: 起站
            destination_station: 迄站
            train_date: 乘車日期 (YYYY-MM-DD)
        """
        origin_id = self.normalize_station(origin_station)
        dest_id = self.normalize_station(destination_station)
        endpoint = f"Rail/THSR/AvailableSeatStatus/Train/OD/{origin_id}/to/{dest_id}/TrainDate/{train_date}"
        return await self.api_request(endpoint)


async def main():
    """命令行接口"""
    if len(sys.argv) < 2:
        print("使用方式:")
        print("  python thsrc_api.py stations")
        print("  python thsrc_api.py timetable <起站> <迄站> <日期>")
        print("  python thsrc_api.py live <車站>")
        print("  python thsrc_api.py train <車次> <日期>")
        print("  python thsrc_api.py seats <起站> <迄站> <日期>")
        sys.exit(1)

    # 從環境變量讀取 API 憑證
    client_id = os.getenv("TDX_CLIENT_ID")
    client_secret = os.getenv("TDX_CLIENT_SECRET")

    if not client_id or not client_secret:
        print("錯誤: 請設置環境變量 TDX_CLIENT_ID 和 TDX_CLIENT_SECRET")
        sys.exit(1)

    client = THSRAPIClient(client_id, client_secret)
    command = sys.argv[1]

    try:
        if command == "stations":
            result = await client.get_stations()
        elif command == "timetable" and len(sys.argv) >= 5:
            result = await client.get_timetable(sys.argv[2], sys.argv[3], sys.argv[4])
        elif command == "live" and len(sys.argv) >= 3:
            result = await client.get_live_schedule(sys.argv[2])
        elif command == "train" and len(sys.argv) >= 4:
            result = await client.get_train_info(sys.argv[2], sys.argv[3])
        elif command == "seats" and len(sys.argv) >= 5:
            result = await client.get_available_seats(sys.argv[2], sys.argv[3], sys.argv[4])
        else:
            print("無效的命令或參數")
            sys.exit(1)

        print(json.dumps(result, ensure_ascii=False, indent=2))
    except Exception as e:
        print(f"錯誤: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())
