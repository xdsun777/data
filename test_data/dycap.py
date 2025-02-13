from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from json import JSONDecodeError
from selenium import webdriver
from selenium.common import *
import json, os, sys


errors = [NoSuchElementException, ElementNotInteractableException]

# 异常处理
class Cnm(Exception):
    def __init__(self, msg):
        self.msg = f"自定义异常：{msg}\n"


# 数据处理


# 运行配置
'''{
                "config_status": 0, 配置文件状态，0为初始状态，1为中断状态
                "urls":[], 一级url列表
                "total": 0, 一级url列表数量
                "count":0 当前head url在一级列表的位置

                "head_url": "" 当前head的url属于哪一个一级url
                "head_count":0, # 当前head url在列表中的位置

                "child_urls": [],当前head的粉丝关注列表用户主页的url
                "child_total": 0, 当前head的粉丝关注列表用户总数
                "child_count": 0, 当前head的粉丝关注列表的url在总数中的位置
            }
            '''


class RunnerConfig:
    def __init__(self, config_file='./fans.json', urls_file='./url.txt', key_file='./key.txt'):
        self.config = '''{
                "head_url": "",
                "head_count":0,
                "config_status": 0,
                "child_urls": [],
                "child_total": 0,
                "child_count": 0,
                "urls":[],
                "total": 0,
                "count":0
            }
            '''
        self.file_config = config_file
        self.file_urls = urls_file
        self.file_key = key_file

        self.runner_config = None
        self.runner_urls = None
        self.runner_key = None

        if not os.path.isdir('./output'):
            os.mkdir('./output')
        self.output = './output'

    def init_config(self):
        try:
            with open('./fans.json', 'w', encoding='utf-8') as f:
                f.write(self.config)
                return True
        except FileExistsError as e:
            print(e)
            return False

    def get_(self, file):
        def file_name(f: str):
            if f.endswith('.txt') or f.endswith('.json'):
                if '/' in f:
                    return f.split('/')[-1]
                if '\\' in f:
                    return f.split('\\')[-1]
                return f
            else:
                raise Cnm(f'{f}文件类型错误！')

        if os.path.isfile(file):
            f_name = file_name(file)
            if f_name == 'fans.json':
                try:
                    with open(self.file_config, 'r', encoding='utf-8') as f:
                        info = f.read()
                        self.runner_config = json.loads(info)
                        return self.runner_config
                except JSONDecodeError as e:
                    print(e)
                    return False
            elif f_name == 'url.txt':
                try:
                    with open(self.file_urls, 'r', encoding='utf-8') as f:
                        self.runner_urls = [i.strip('\n') for i in f.readlines()]
                        return self.runner_urls
                except FileNotFoundError as e:
                    print(e)
                    return False
            elif f_name == 'key.txt':
                try:
                    with open(file, 'r', encoding='utf-8') as f:
                        self.runner_urls = [i.strip('\n') for i in f.readlines()]
                        return self.runner_urls
                except FileExistsError as e:
                    print(e)
            else:
                raise Cnm(f'{file}文件不存在')
        else:
            raise Cnm(f'{file}文件不存在')


# 数据抓取
class Cap:
    def __init__(self):
        self.service = Service()
        self.option = webdriver.ChromeOptions()
        cap = {'performance': 'ALL'}
        self.option.set_capability('goog:loggingPrefs', cap)
        self.option.add_experimental_option("detach", True)

        if sys.platform == 'linux':
            self.option.add_argument(f'user-data-dir={os.environ["HOME"]}/onlyone/pro/douyin_sqlite_bak/test')
            self.option.binary_location = f'{os.environ["HOME"]}/onlyone/pro/douyin_sqlite_bak/selenium/chrome/linux64/131.0.6778.264/chrome'
            self.service.executable_path = f'{os.environ["HOME"]}/onlyone/pro/douyin_sqlite_bak/selenium/chromedriver/linux64/131.0.6778.264/chromedriver'
        else:
            self.option.add_argument(f'user-data-dir=C:{os.environ["HOMEPATH"]}\Documents\cached_google')
            self.option.binary_location = f'C:{os.environ["HOMEPATH"]}\Documents\chrome-win64\chrome.exe'
            self.service.executable_path = f'C:{os.environ["HOMEPATH"]}\Documents\chromedriver-win64\chromedriver.exe'
        self.option.add_argument(r'--disable-gpu-driver-bug-workarounds')
        self.option.add_argument(r'--no-default-browser-check')
        self.option.add_argument("--disable-gpu")  # 适用于 Linux 和 Windows 系统
        self.option.add_argument("--no-sandbox")  # Bypass OS security model
        self.option.add_argument("--disable-extensions")
        self.option.add_argument("--enable-unsafe-swiftshader")
        self.option.add_argument("--disable-3d-apis")
        # option.add_argument("--headless")  # 使用无头模式
        # option.add_argument("start-maximized")  # 启动最大化窗口
        # option.add_argument("disable-infobars")
        # option.add_argument("--disable-background-network-ingestion")
        # option.add_argument(r'--disable-background-networking')

    def setup(self, browser='chrome'):
        if browser == 'chrome':
            return webdriver.Chrome(options=self.option, service=self.service)

    @staticmethod
    def teardown(driver):
        driver.quit()

    @staticmethod
    def get_data(driver, url):
        user_info_list_into_dict = []
        driver.get(url)
        wait = WebDriverWait(driver, timeout=2, poll_frequency=.2, ignored_exceptions=errors)
        wait.until(lambda d: driver.find_elements(by=By.CLASS_NAME, value="C1cxu0Vq") or True)
        text_box = driver.find_elements(by=By.CLASS_NAME, value="C1cxu0Vq")





def main():
    # 运行条件： url.txt    fans.json     key.txt
    # 优先运行fans.json,随后运行url.txt,key.txt用于过滤筛选数据
    # if os.path.isfile('fans.json'):
    runner = RunnerConfig()
    c = Cap()

    driver = c.setup()
    fans_json = runner.get_('fans.json')

    if fans_json:
        print(fans_json)
        c.get_data(driver=driver, url='https://www.douyin.com/user/MS4wLjABAAAAtu9y3Z3_1SWmF27_rxpm0aFjXVRL9-6GXUJetoR05kkPfRIMWJJOQ5k19fkL2BPQ')


if __name__ == '__main__':
    main()
