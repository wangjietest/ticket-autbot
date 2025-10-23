import json
import time
import pickle
from os.path import exists
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

class SimpleTicketBot:
    def __init__(self, config):
        self.config = config
        self.driver = None
    
    def init_browser(self):
        #配置chrome选项
        options = Options()

        #添加移动端模拟
        options.add_experimental_option("mobileEmulation", {"deviceName": "Nexus 6"})
       
        #去除webdriver标识
        options.add_argument("--disable-blink-features=AutomationControlled")

        #减少错误输出的配置,仅显示严重错误
        options.add_argument("--log-level=3")
        

        #启动浏览器
        self.driver =  webdriver.Chrome(
            executable_path=self.config['driver_path'],
            options=options
        )
        print("浏览器启动成功")

    def login(self):
        #简单的登录方法
        print("正在访问大麦网")
        self.driver.get("https://www.damai.cn/")

        #尝试加载cookie
        if not self.load_cookies():
            print("请手动点击登录按钮进行登录。。。")
            input("登录完成后，按回车继续。。。")
            self.save_cookies()

        print("登录处理完成！")

    def save_cookies(self):
        #保存登录后的cookies
        try:
            cookies = self.driver.get_cookies()
            with open('cookies.pkl','wb') as f:
                pickle.dump(cookies,f)
            print("cookies保存成功")
        except Exception as e:
            print(f"保存cookies失败:{e}")


    def load_cookies(self):
        #加载已保存的cookies

        try:
            if exists('cookies.pkl'):
                with open('cookies.pkl','rb') as f:
                    cookies = pickle.load(f)

                    #先访问大麦网域名

                    self.driver.get('https://www.damai.cn/')
                    time.sleep(2)

                    #添加每个cookies
                    for cookie in cookies:
                        cookie_dict = {
                            'domain': '.damai.cn',
                            'name': cookie.get('name'),
                            'value': cookie.get('value'),
                            'path': '/',
                            'httpOnly': False,
                            'HostOnly': False,
                            'Secure': False
                        }
                        self.driver.add_cookie(cookie_dict)
                    
                    print("cookies加载成功")
                    return True
            else:
                print("cookies文件不存在，需要重新登录")
                return False
        except Exception as e:
            print(f"加载cookies失败:{e}")
            return False


    def go_to_target_page(self):
        #访问目标购票页面
        print(f"正在访问目标购票页面:{self.config['target_url']}")
        self.driver.get(self.config['target_url'])
        print("目标页面加载完成")

if __name__ == "__main__":
    #加载配置
    with open('config.json', 'r', encoding='utf-8') as f:
        config = json.load(f)

    #创建机器人实例
    bot = SimpleTicketBot(config)

    #启动浏览器
    bot.init_browser()

    #登录
    bot.login()

    #访问目标页面
    bot.go_to_target_page()

    print("程序运行完成")
