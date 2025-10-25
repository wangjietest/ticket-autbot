import json
from simple_bot import SimpleTicketBot
import time
from selenium.webdriver.common.by import By

with open('config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)

#创建浏览器实例
bot = SimpleTicketBot(config)

#启动浏览器
bot.init_browser()

#登录
bot.login()

#访问目标页面
bot.go_to_target_page()

#添加等待时间
time.sleep(3)

print("===查找所有按钮===")
buttons = bot.driver.find_elements(By.TAG_NAME, "button")
print(f"找到{len(buttons)}个按钮")

for i,button in enumerate(buttons):
    text = button.text.strip()
    tag_name = button.tag_name
    class_name = button.get_attribute("class")
    type_name = button.get_attribute("type")
    id_name = button.get_attribute("id")

    print(f"{i+1}.文本：{text}，标签名：{tag_name}，类名：{class_name}，类型：{type_name}，ID：{id_name}")

print("调试完成")
input("按回车键退出...")