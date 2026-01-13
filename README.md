# THSRC Claude Skills - 台灣高鐵查詢技能

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

一個用於 Claude Code 和 Claude Desktop 的台灣高鐵（THSRC）即時資訊查詢技能。透過 TDX (運輸資料流通服務) API 提供時刻表、即時班次、車次狀態和座位查詢功能。

## ✨ 功能特色

- 🚉 **車站資訊查詢** - 顯示所有 12 個高鐵車站詳細資訊
- 📅 **時刻表查詢** - 查詢指定路線和日期的班次時刻
- ⏱️ **即時班次狀態** - 獲取車站的即時班次資訊
- 🚄 **車次詳細資訊** - 查詢特定車次的完整資訊
- 💺 **座位狀態查詢** - 檢查指定路線的剩餘座位情況
- 🌐 **多語言支援** - 支援中文、英文站名及站點 ID 查詢

## 📦 安裝

### 在 Claude Desktop 中安裝

1. 下載最新版本的 `thsrc.zip` from [Releases](https://github.com/physictim/thsrc_claude_skills/releases)
2. 開啟 Claude Desktop
3. 點選設定 → Skills → Import Skill
4. 選擇下載的 `thsrc.zip` 檔案
5. 完成安裝！

### 手動安裝

```bash
# 複製儲存庫
git clone https://github.com/physictim/thsrc_claude_skills.git

# 複製到 Claude skills 目錄
cp -r thsrc_claude_skills ~/.claude/skills/thsrc
```

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

安裝完成後，在 Claude Code 或 Claude Desktop 中可以直接使用自然語言查詢：

### 中文查詢範例
```
查詢明天台北到左營的高鐵班次
台中車站現在有哪些班次？
823 車次明天的詳細資訊
台北到高雄明天還有座位嗎？
顯示所有高鐵車站列表
```

### 英文查詢範例
```
Show me THSR schedules from Taipei to Zuoying tomorrow
What trains are at Taichung station now?
Give me details for train 823 tomorrow
Are there available seats from Taipei to Kaohsiung tomorrow?
List all THSR stations
```

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
