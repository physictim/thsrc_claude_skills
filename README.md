# THSRC Claude Skills - 台湾高铁查询技能

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

一个用于 Claude Code 和 Claude Desktop 的台湾高铁（THSRC）实时信息查询技能。通过 TDX (Transport Data Exchange) API 提供时刻表、即时班次、车次状态和座位查询功能。

## ✨ 功能特色

- 🚉 **车站信息查询** - 显示所有12个高铁车站详细信息
- 📅 **时刻表查询** - 查询指定路线和日期的班次时刻
- ⏱️ **即时班次状态** - 获取车站的实时班次信息
- 🚄 **车次详细资讯** - 查询特定车次的完整信息
- 💺 **座位状态查询** - 检查指定路线的剩余座位情况
- 🌐 **多语言支持** - 支持中文、英文站名及站点ID查询

## 📦 安装

### 在 Claude Desktop 中安装

1. 下载最新版本的 `thsrc.zip` from [Releases](https://github.com/physictim/thsrc_claude_skills/releases)
2. 打开 Claude Desktop
3. 点击设置 → Skills → Import Skill
4. 选择下载的 `thsrc.zip` 文件
5. 完成安装！

### 手动安装

```bash
# 克隆仓库
git clone https://github.com/physictim/thsrc_claude_skills.git

# 复制到 Claude skills 目录
cp -r thsrc_claude_skills ~/.claude/skills/thsrc
```

## ⚙️ 配置

### 获取 TDX API 凭证

1. 访问 [TDX 运输资料流通服务平台](https://tdx.transportdata.tw/)
2. 注册账号并登录
3. 创建应用程序以获取：
   - Client ID
   - Client Secret

### 设置环境变量

**macOS/Linux:**
```bash
export TDX_CLIENT_ID="your_client_id"
export TDX_CLIENT_SECRET="your_client_secret"
```

将以下内容添加到 `~/.zshrc` 或 `~/.bashrc` 以永久保存：
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

安装完成后，在 Claude Code 或 Claude Desktop 中可以直接使用自然语言查询：

### 中文查询示例
```
查询明天台北到左营的高铁班次
台中车站现在有哪些班次？
823车次明天的详细资讯
台北到高雄明天还有座位吗？
显示所有高铁车站列表
```

### English Queries
```
Show me THSR schedules from Taipei to Zuoying tomorrow
What trains are at Taichung station now?
Give me details for train 823 tomorrow
Are there available seats from Taipei to Kaohsiung tomorrow?
List all THSR stations
```

## 🚉 支持的车站

| 中文站名 | English | 站点ID |
|---------|---------|--------|
| 南港 | Nangang | 0990 |
| 台北 | Taipei | 1000 |
| 板桥 | Banqiao | 1010 |
| 桃园 | Taoyuan | 1020 |
| 新竹 | Hsinchu | 1030 |
| 苗栗 | Miaoli | 1035 |
| 台中 | Taichung | 1040 |
| 彰化 | Changhua | 1043 |
| 云林 | Yunlin | 1047 |
| 嘉义 | Chiayi | 1050 |
| 台南 | Tainan | 1060 |
| 左营 | Zuoying | 1070 |

**别名：** 高雄 = 左营

## 🔧 命令行测试

可以直接使用 Python 脚本测试 API 功能：

```bash
cd scripts

# 查询车站列表
python thsrc_api.py stations

# 查询时刻表（台北→左营，2024-01-15）
python thsrc_api.py timetable 台北 左营 2024-01-15

# 查询即时班次（台北站）
python thsrc_api.py live 台北

# 查询特定车次（823号，2024-01-15）
python thsrc_api.py train 823 2024-01-15

# 查询座位状态（台北→左营，2024-01-15）
python thsrc_api.py seats 台北 左营 2024-01-15
```

## 📁 项目结构

```
thsrc/
├── SKILL.md                    # 技能主文档（Claude 使用）
├── README.md                   # 本文件
├── scripts/
│   └── thsrc_api.py           # TDX API 查询脚本
└── references/
    └── stations.md            # 车站参考资料
```

## 🛠️ 技术细节

### API 功能

1. **get_stations()** - 获取所有车站信息
2. **get_timetable(origin, dest, date)** - 查询时刻表
3. **get_live_schedule(station)** - 获取即时班次
4. **get_train_info(train_no, date)** - 查询车次信息
5. **get_available_seats(origin, dest, date)** - 查询座位状态

### 依赖项

```python
httpx>=0.24.0      # HTTP 客户端
python-dotenv      # 环境变量管理（可选）
```

安装依赖：
```bash
pip install httpx python-dotenv
```

## ⚠️ 注意事项

1. **日期格式**：必须使用 `YYYY-MM-DD` 格式（例如：2024-01-15）
2. **站名格式**：支持中文、英文或站点ID
3. **API 限制**：请遵守 TDX API 的使用限制和配额
4. **凭证安全**：不要在公开场合分享你的 API 凭证
5. **座位更新频率**：
   - 当日查询：每10分钟更新
   - 未来日期：每日 10:00、16:00、22:00 更新

## 🐛 故障排除

### 问题：找不到 TDX 凭证
确保环境变量已正确设置：
```bash
echo $TDX_CLIENT_ID
echo $TDX_CLIENT_SECRET
```

### 问题：无效的车站名称
检查站名拼写，参考支持的车站列表

### 问题：API 请求超时
- 检查网络连接
- 确认 TDX API 服务状态
- 稍后重试

## 📄 许可证

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件

## 🔗 相关链接

- [TDX 运输资料流通服务平台](https://tdx.transportdata.tw/)
- [台湾高铁官网](https://www.thsrc.com.tw/)
- [Claude Code](https://claude.ai/claude-code)
- [Model Context Protocol](https://modelcontextprotocol.io/)

## 👨‍💻 作者

**physictim**
- GitHub: [@physictim](https://github.com/physictim)

## 🤝 贡献

欢迎提交 Issues 和 Pull Requests！

## 📝 更新日志

### v1.0.0 (2026-01-13)
- 🎉 初始版本发布
- ✅ 支持所有基本查询功能
- ✅ 多语言站名支持
- ✅ 完整的命令行界面

---

**如果这个项目对你有帮助，请给个 ⭐️ Star！**
