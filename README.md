# THSRC Claude Skills - 台灣高鐵查詢技能

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

一個用於本地環境的台灣高鐵（THSRC）即時資訊查詢工具。透過 TDX (運輸資料流通服務) API 提供時刻表、即時班次、車次狀態和座位查詢功能。

> ⚠️ **重要說明**：由於 Claude Desktop Skills 的網路限制，本工具**無法**在 Claude Desktop 中使用。
> 如需在 Claude Desktop 中使用高鐵查詢功能，請使用 [THSRC MCP Server](https://github.com/physictim/thsrc_mcp) 版本。

## 🚀 快速開始

### 本地命令列使用

設定 TDX API 憑證後，直接執行：

```bash
cd scripts
python thsrc_api.py stations
python thsrc_api.py timetable 台北 左營 2024-01-15
```

> **注意**：使用前需要先設定 TDX API 憑證（詳見[設定](#️-設定)）

## ✨ 功能特色

- 🚉 **車站資訊查詢** - 顯示所有 12 個高鐵車站詳細資訊
- 📅 **時刻表查詢** - 查詢指定路線和日期的班次時刻
- ⏱️ **即時班次狀態** - 獲取車站的即時班次資訊
- 🚄 **車次詳細資訊** - 查詢特定車次的完整資訊
- 💺 **座位狀態查詢** - 檢查指定路線的剩餘座位情況
- 🌐 **多語言支援** - 支援中文、英文站名及站點 ID 查詢

## 📦 安裝

### 方法 1：直接複製儲存庫（推薦）

```bash
# 複製儲存庫
git clone https://github.com/physictim/thsrc_claude_skills.git

# 進入專案目錄
cd thsrc_claude_skills
```

### 方法 2：下載 ZIP 檔案

1. 前往 [Releases](https://github.com/physictim/thsrc_claude_skills/releases) 下載最新版本
2. 解壓縮到您想要的目錄
3. 進入專案資料夾

## ⚙️ 設定

### 取得 TDX API 憑證

1. 前往 [TDX 運輸資料流通服務平台](https://tdx.transportdata.tw/)
2. 註冊帳號並登入
3. 建立應用程式以取得：
   - Client ID
   - Client Secret

### 設定環境變數

**macOS/Linux:**
```bash
export TDX_CLIENT_ID="your_client_id"
export TDX_CLIENT_SECRET="your_client_secret"
```

將以下內容加入 `~/.zshrc` 或 `~/.bashrc` 以永久儲存：
```bash
echo 'export TDX_CLIENT_ID="your_client_id"' >> ~/.zshrc
echo 'export TDX_CLIENT_SECRET="your_client_secret"' >> ~/.zshrc
source ~/.zshrc
```

**Windows (PowerShell):**
```powershell
$env:TDX_CLIENT_ID="your_client_id"
$env:TDX_CLIENT_SECRET="your_client_secret"
```

## 📖 使用方法

### 命令列介面

安裝並設定環境變數後，可以使用以下指令查詢高鐵資訊：

### 指令範例

#### 1️⃣ 車站列表查詢

**指令：**
```bash
python scripts/thsrc_api.py stations
```

**輸出範例：**
```json
[
  {
    "StationID": "0990",
    "StationName": {"Zh_tw": "南港", "En": "Nangang"}
  },
  {
    "StationID": "1000",
    "StationName": {"Zh_tw": "台北", "En": "Taipei"}
  },
  ...
]
```

---

#### 2️⃣ 時刻表查詢

**指令：**
```bash
# 使用中文站名
python scripts/thsrc_api.py timetable 台北 左營 2024-01-15

# 使用英文站名
python scripts/thsrc_api.py timetable Taipei Zuoying 2024-01-15

# 使用站點 ID
python scripts/thsrc_api.py timetable 1000 1070 2024-01-15
```

**輸出範例：**
```json
[
  {
    "TrainNo": "803",
    "DepartureTime": "06:30:00",
    "ArrivalTime": "08:15:00",
    "StopTimes": [...]
  },
  ...
]
```

---

#### 3️⃣ 即時班次查詢

**指令：**
```bash
# 使用中文站名
python scripts/thsrc_api.py live 台中

# 使用英文站名
python scripts/thsrc_api.py live Taichung

# 使用站點 ID
python scripts/thsrc_api.py live 1040
```

**輸出範例：**
```json
[
  {
    "TrainNo": "152",
    "Direction": "0",
    "ScheduledArrivalTime": "14:35:00",
    "DelayTime": 0,
    "TrainStatus": "準點"
  },
  ...
]
```

---

#### 4️⃣ 特定車次資訊查詢

**指令：**
```bash
python scripts/thsrc_api.py train 823 2024-01-15
```

**輸出範例：**
```json
[
  {
    "TrainNo": "823",
    "TrainTypeName": {"Zh_tw": "直達車"},
    "StopTimes": [
      {
        "StationName": {"Zh_tw": "台北"},
        "DepartureTime": "13:00:00"
      },
      {
        "StationName": {"Zh_tw": "板橋"},
        "ArrivalTime": "13:07:00",
        "DepartureTime": "13:09:00"
      },
      ...
    ]
  }
]
```

---

#### 5️⃣ 座位狀態查詢

**指令：**
```bash
# 查詢台北到左營（高雄）的座位狀態
python scripts/thsrc_api.py seats 台北 左營 2024-01-15
```

**輸出範例：**
```json
[
  {
    "TrainNo": "803",
    "DepartureTime": "06:30:00",
    "StandardSeatStatus": "Available",
    "BusinessSeatStatus": "Available"
  },
  {
    "TrainNo": "807",
    "DepartureTime": "07:00:00",
    "StandardSeatStatus": "Limited",
    "BusinessSeatStatus": "Available"
  },
  ...
]
```

> 💡 **資料更新頻率**：當日查詢每 10 分鐘更新 / 未來日期每日 10:00、16:00、22:00 更新

## 🚉 支援的車站

| 中文站名 | English | 站點 ID |
|---------|---------|--------|
| 南港 | Nangang | 0990 |
| 台北 | Taipei | 1000 |
| 板橋 | Banqiao | 1010 |
| 桃園 | Taoyuan | 1020 |
| 新竹 | Hsinchu | 1030 |
| 苗栗 | Miaoli | 1035 |
| 台中 | Taichung | 1040 |
| 彰化 | Changhua | 1043 |
| 雲林 | Yunlin | 1047 |
| 嘉義 | Chiayi | 1050 |
| 台南 | Tainan | 1060 |
| 左營 | Zuoying | 1070 |

**別名：** 高雄 = 左營

## 🔧 命令列測試

可以直接使用 Python 腳本測試 API 功能：

```bash
cd scripts

# 查詢車站列表
python thsrc_api.py stations

# 查詢時刻表（台北→左營，2024-01-15）
python thsrc_api.py timetable 台北 左營 2024-01-15

# 查詢即時班次（台北站）
python thsrc_api.py live 台北

# 查詢特定車次（823號，2024-01-15）
python thsrc_api.py train 823 2024-01-15

# 查詢座位狀態（台北→左營，2024-01-15）
python thsrc_api.py seats 台北 左營 2024-01-15
```

## 📁 專案結構

```
thsrc/
├── SKILL.md                    # 技能主文件（Claude 使用）
├── README.md                   # 本檔案
├── scripts/
│   └── thsrc_api.py           # TDX API 查詢腳本
└── references/
    └── stations.md            # 車站參考資料
```

## 🛠️ 技術細節

### API 功能

1. **get_stations()** - 取得所有車站資訊
2. **get_timetable(origin, dest, date)** - 查詢時刻表
3. **get_live_schedule(station)** - 取得即時班次
4. **get_train_info(train_no, date)** - 查詢車次資訊
5. **get_available_seats(origin, dest, date)** - 查詢座位狀態

### 相依套件

```python
httpx>=0.24.0      # HTTP 客戶端
python-dotenv      # 環境變數管理（選用）
```

安裝相依套件：
```bash
pip install httpx python-dotenv
```

## ⚠️ 注意事項

1. **日期格式**：必須使用 `YYYY-MM-DD` 格式（例如：2024-01-15）
2. **站名格式**：支援中文、英文或站點 ID
3. **API 限制**：請遵守 TDX API 的使用限制和配額
4. **憑證安全**：請勿在公開場合分享您的 API 憑證
5. **座位更新頻率**：
   - 當日查詢：每 10 分鐘更新
   - 未來日期：每日 10:00、16:00、22:00 更新

## 🐛 疑難排解

### 問題：找不到 TDX 憑證
確保環境變數已正確設定：
```bash
echo $TDX_CLIENT_ID
echo $TDX_CLIENT_SECRET
```

### 問題：無效的車站名稱
請檢查站名拼字，參考支援的車站列表

### 問題：API 請求逾時
- 檢查網路連線
- 確認 TDX API 服務狀態
- 稍後重試

## 📄 授權條款

本專案採用 MIT 授權條款 - 詳見 [LICENSE](LICENSE) 檔案

## 🔗 相關連結

- [TDX 運輸資料流通服務平台](https://tdx.transportdata.tw/)
- [台灣高鐵官網](https://www.thsrc.com.tw/)
- [Claude Code](https://claude.ai/claude-code)
- [Model Context Protocol](https://modelcontextprotocol.io/)

## 👨‍💻 作者

**physictim**
- GitHub: [@physictim](https://github.com/physictim)

## 🤝 貢獻

歡迎提交 Issues 和 Pull Requests！

## 📝 更新日誌

### v1.0.0 (2026-01-13)
- 🎉 初始版本發布
- ✅ 支援所有基本查詢功能
- ✅ 多語言站名支援
- ✅ 完整的命令列介面

---

**如果這個專案對您有幫助，請給個 ⭐️ Star！**
