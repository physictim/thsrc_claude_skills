# THSRC Claude Skills - 台灣高鐵查詢技能

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

一個用於 Claude Code 的台灣高鐵（THSRC）即時資訊查詢技能。透過 TDX (運輸資料流通服務) API 提供時刻表、即時班次、車次狀態和座位查詢功能。

## 📱 適用環境

| 環境 | 狀態 | 說明 |
|------|------|------|
| **Claude Code CLI** | ✅ 完全支援 | 可用自然語言查詢，無網路限制 |
| **本地命令列** | ✅ 完全支援 | 直接執行 Python 腳本 |
| **Claude Desktop** | ❌ 不支援 | 網路沙盒限制，請使用 [MCP Server 版本](https://github.com/physictim/thsrc_mcp) |

## 🚀 快速開始

### 在 Claude Code 中使用（推薦）

```bash
# 安裝 skill
/plugin marketplace add physictim/thsrc_claude_skills
/plugin install physictim@thsrc
```

然後就可以用自然語言詢問：

```
查詢明天台北到左營的高鐵班次
台中車站現在有哪些班次？
823 車次明天的詳細資訊
```

Claude 會自動執行查詢並以表格形式呈現結果！

> **注意**：使用前需要先設定 TDX API 憑證（詳見[設定](#️-設定)）

## ✨ 功能特色

- 🚉 **車站資訊查詢** - 顯示所有 12 個高鐵車站詳細資訊
- 📅 **時刻表查詢** - 查詢指定路線和日期的班次時刻
- ⏱️ **即時班次狀態** - 獲取車站的即時班次資訊
- 🚄 **車次詳細資訊** - 查詢特定車次的完整資訊
- 💺 **座位狀態查詢** - 檢查指定路線的剩餘座位情況
- 🌐 **多語言支援** - 支援中文、英文站名及站點 ID 查詢

## 📦 安裝

### 方法 1：透過 Claude Code Marketplace（推薦）

在 Claude Code 中執行：

```bash
/plugin marketplace add physictim/thsrc_claude_skills
/plugin install physictim@thsrc
```

### 方法 2：直接複製儲存庫

```bash
git clone https://github.com/physictim/thsrc_claude_skills.git
cd thsrc_claude_skills
```

### 方法 3：下載 ZIP 檔案

1. 前往 [Releases](https://github.com/physictim/thsrc_claude_skills/releases) 下載最新版本
2. 解壓縮到您想要的目錄

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

### 在 Claude Code 中使用（推薦）

安裝 skill 後，直接用自然語言詢問，Claude 會自動查詢並以表格形式呈現結果：

### 自然語言查詢範例

#### 1️⃣ 車站列表查詢

**您可以這樣問：**
```
顯示所有高鐵車站列表
有哪些高鐵車站？
```

**Claude 會以表格呈現：**
```
台灣高鐵共有 12 個車站：

┌────┬──────────┬──────────┬──────────┐
│ #  │ 中文站名  │ 英文站名  │ 站點 ID  │
├────┼──────────┼──────────┼──────────┤
│ 1  │ 南港     │ Nangang  │ 0990     │
│ 2  │ 台北     │ Taipei   │ 1000     │
│ 3  │ 板橋     │ Banqiao  │ 1010     │
│ 4  │ 桃園     │ Taoyuan  │ 1020     │
│ 5  │ 新竹     │ Hsinchu  │ 1030     │
│ 6  │ 苗栗     │ Miaoli   │ 1035     │
│ 7  │ 台中     │ Taichung │ 1040     │
│ 8  │ 彰化     │ Changhua │ 1043     │
│ 9  │ 雲林     │ Yunlin   │ 1047     │
│ 10 │ 嘉義     │ Chiayi   │ 1050     │
│ 11 │ 台南     │ Tainan   │ 1060     │
│ 12 │ 左營     │ Zuoying  │ 1070     │
└────┴──────────┴──────────┴──────────┘
```

---

#### 2️⃣ 時刻表查詢

**您可以這樣問：**
```
查詢明天台北到左營的高鐵班次
今天下午台中到台南有哪些車次？
1月15日板橋到高雄的時刻表
```

**Claude 會以表格呈現：**
```
2026-01-14 台北→左營 高鐵班次（共找到 45 班次）

🚄 直達車次：
┌─────────┬──────────┬──────────┬──────┐
│ 車次    │ 出發時間  │ 抵達時間  │ 車程 │
├─────────┼──────────┼──────────┼──────┤
│ 803     │ 06:30    │ 08:15    │ 1h45m│
│ 807     │ 07:00    │ 08:45    │ 1h45m│
│ 813     │ 08:00    │ 09:45    │ 1h45m│
│ 823     │ 09:00    │ 10:45    │ 1h45m│
│ ...     │ ...      │ ...      │ ...  │
└─────────┴──────────┴──────────┴──────┘

註：以上為直達車次，實際票價與座位狀態請另行查詢
```

---

#### 3️⃣ 即時班次查詢

**您可以這樣問：**
```
台中車站現在有哪些班次？
台北站即時班次狀態
新竹站現在有什麼車？
```

**Claude 會以表格呈現：**
```
台中站即時班次資訊（2026-01-13 14:30 更新）

📍 北上列車：
┌─────────┬──────────┬──────┬──────────┐
│ 車次    │ 預計時間  │ 狀態 │ 目的地   │
├─────────┼──────────┼──────┼──────────┤
│ 152     │ 14:35    │ 準點 │ 南港     │
│ 256     │ 14:52    │ 準點 │ 台北     │
│ 160     │ 15:10    │ 準點 │ 板橋     │
└─────────┴──────────┴──────┴──────────┘

📍 南下列車：
┌─────────┬──────────┬──────┬──────────┐
│ 車次    │ 預計時間  │ 狀態 │ 目的地   │
├─────────┼──────────┼──────┼──────────┤
│ 151     │ 14:40    │ 準點 │ 左營     │
│ 655     │ 14:55    │ 誤點 │ 台南     │
│         │          │ 3分  │          │
└─────────┴──────────┴──────┴──────────┘
```

---

#### 4️⃣ 特定車次資訊查詢

**您可以這樣問：**
```
823 車次明天的詳細資訊
查詢 1234 號車次今天的時刻表
告訴我 807 車次停靠哪些站
```

**Claude 會以表格呈現：**
```
🚄 車次 823 詳細資訊（2026-01-14）

列車類型：直達車
起訖站：台北 → 左營
總車程：1 小時 45 分鐘

停靠站時刻表：
┌────┬──────────┬──────────┬──────────┐
│序號│ 車站     │ 抵達時間  │ 出發時間  │
├────┼──────────┼──────────┼──────────┤
│ 1  │ 台北     │ ----     │ 13:00    │
│ 2  │ 板橋     │ 13:07    │ 13:09    │
│ 3  │ 台中     │ 13:49    │ 13:51    │
│ 4  │ 台南     │ 14:30    │ 14:32    │
│ 5  │ 左營     │ 14:45    │ ----     │
└────┴──────────┴──────────┴──────────┘

💡 提醒：實際發車時間可能因應營運狀況調整
```

---

#### 5️⃣ 座位狀態查詢

**您可以這樣問：**
```
台北到高雄明天還有座位嗎？
查詢後天台中到台南的座位狀態
1月15日板橋到左營哪些車次還有位子？
```

**Claude 會以表格呈現：**
```
2026-01-14 台北→左營（高雄）座位狀態

✅ 有座位的班次：
┌─────────┬──────────┬────────────────────┐
│ 車次    │ 出發時間  │ 座位狀態           │
├─────────┼──────────┼────────────────────┤
│ 803     │ 06:30    │ ⭕ 充足            │
│ 807     │ 07:00    │ 🔶 少量（標準座）  │
│ 813     │ 08:00    │ ⭕ 充足            │
│ 823     │ 09:00    │ 🔶 少量（商務座）  │
│ ...     │ ...      │ ...                │
└─────────┴──────────┴────────────────────┘

❌ 已售完的班次：
- 835 (10:00)、845 (11:00)、857 (12:00)

座位圖示說明：
⭕ 充足 - 兩種座位皆充足
🔶 少量 - 部分座位類型剩餘較少
❌ 售完 - 該班次已無座位

💡 資料更新時間：每 10 分鐘（當日）/ 每日 10:00、16:00、22:00（未來日期）
```

---

### 本地命令列使用

如果您想直接在命令列執行 Python 腳本，也可以：

```bash
# 車站列表
python scripts/thsrc_api.py stations

# 時刻表查詢
python scripts/thsrc_api.py timetable 台北 左營 2024-01-15

# 即時班次
python scripts/thsrc_api.py live 台中

# 特定車次
python scripts/thsrc_api.py train 823 2024-01-15

# 座位狀態
python scripts/thsrc_api.py seats 台北 左營 2024-01-15
```

這些指令會直接輸出 JSON 格式的資料。

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
