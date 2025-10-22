# 简化版抢票机器人

## 功能
- 自动打开浏览器（移动端模拟）
- 手动登录大麦网
- 自动访问目标页面
- 基础抢票功能

## 使用方法
1. 安装依赖：`pip install selenium`
2. 配置 `config.json` 文件
3. 运行：`python simple_bot.py`

## 项目结构
my-ticket-bot/
├── simple_bot.py # 主程序
├── config.json # 配置文件
├── chromedriver.exe # Chrome浏览器驱动
└── README.md # 项目说明

## 配置说明
- `driver_path`: ChromeDriver路径
- `target_url`: 目标购票页面URL
- `sess`: 场次优先级列表
- `price`: 票档优先级列表
- `ticket_num`: 购票数量
- `viewer_person`: 购票人序号

## 注意事项
- 需要先手动登录大麦网
- 确保ChromeDriver版本与Chrome浏览器版本匹配
- 仅供学习使用