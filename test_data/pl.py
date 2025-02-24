from pprint import pprint

from selenium.common import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
import os, sys, time,random
from selenium.webdriver.support.wait import WebDriverWait

errors = [NoSuchElementException, ElementNotInteractableException]
# 数据抓取
class Cap:
    def __init__(self,browser='chrome'):
        self.cap_data_count = None
        self.pub_sleep_time = 2
        self.log = []
        self.user_status = True
        self.user_status_dict = {}
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
        self.option.add_argument("--disable-background-tasks")
        self.option.add_argument("--disable-backgrounding-occluded-windows")
        # self.option.add_argument("--headless")  # 使用无头模式
        def setup(browser='chrome'):
            if browser == 'chrome':
                return webdriver.Chrome(options=self.option, service=self.service)
        self.driver = setup(browser=browser)

    def setup(self,browser='chrome'):
        if browser == 'chrome':
            return webdriver.Chrome(options=self.option, service=self.service)

    def teardown(self):
        self.driver.quit()

    def write_txt(self):
        with open(self.filename, 'w', encoding='utf-8') as f:
            f.write(self.data)

    def pl_already(self,url, file='./pl_already.txt'):
        if os.path.isfile(file):
            with open(file, 'r', encoding='utf-8') as f:
                al = [i.strip('\n') for i in f.readlines()]
        else:
            al = []
        if url in al:
            print(f"已抓取:{url} ")
            return True
        else:
            print(f"未抓取:{url}")
            with open(file, 'a', encoding='utf-8') as f:
                f.write(url + '\n')
            return False

    def pl(self, url=None, pl_text=None, pic=None):
        wait = WebDriverWait(self.driver, timeout=2, poll_frequency=.2, ignored_exceptions=errors)
        wait.until(lambda d: self.driver.find_elements(by=By.CLASS_NAME, value="jp8u3iov") or True)
        time.sleep(5)
        els = self.driver.find_elements(by=By.CLASS_NAME, value='jp8u3iov')
        time.sleep(3)
        try:
            els[1].click()
        except:
            return None
        if pic:
            parent_element = self.driver.find_elements(by=By.CLASS_NAME, value='comment-input-inner-container')
            child_element = parent_element[0].find_element(By.TAG_NAME, 'input')
            child_element.send_keys(pic)
        else:
            print("无图")

        time.sleep(2)
        input_div = self.driver.find_element(by=By.CLASS_NAME, value='lFk180Rt')
        input_div.click()
        time.sleep(0.5)
        input_div.click()
        time.sleep(0.5)
        input_div.click()
        time.sleep(0.5)
        input_div.click()
        time.sleep(0.5)
        if pl_text:
            input_tag = input_div.find_elements(by=By.TAG_NAME, value='div')[1].find_element(by=By.CLASS_NAME,
                                                                                             value='DraftEditor-editorContainer').find_element(
                by=By.TAG_NAME, value='div')
            input_tag.send_keys(pl_text)
        else:
            print("无文字")

        if pl_text or pic:
            self.driver.find_element(by=By.CLASS_NAME, value='WFB7wUOX').click()
            print("发布成功")
        time.sleep(5)

    def get_img(self):
        now_dir = os.path.dirname(os.path.abspath(__file__))
        now_dir = os.path.join(now_dir,'img')
        if os.path.isdir('img'):
            return [os.path.join(now_dir,img) for img in os.listdir('img') if img.endswith('jpg') or img.endswith('png') or img.endswith('jpeg') ]
        else:
            return None

    def dian_zan(self):
        try:
            self.driver.find_elements(by=By.CLASS_NAME, value='myn2Itp_')[1].click()
        except:
            print("没找到点赞节点")

    def pl_pre(self):
        with open('url.txt', 'r', encoding='utf-8') as f:
            url_list = [url.strip('\n') for url in f.readlines()]
        with open('keys.txt', 'r', encoding='utf-8') as f:
            keys = [i.strip('\n') for i in f.readlines()]

        for i,url in enumerate(url_list):
            print(i,end='')
            if self.pl_already(url):
                continue
            self.driver.get(url)
            time.sleep(2)
            try:
                mp = self.driver.find_element(by=By.CLASS_NAME, value='q438d7I8')
            except:
                continue
            li_list = mp.find_elements(by=By.TAG_NAME, value='li')
            time.sleep(2)
            filter_list = []
            for i in li_list:
                context = i.text + i.find_element(by=By.TAG_NAME, value='img').get_attribute('alt')
                for key in keys:
                    if key in context:
                        filter_list.append(i)

            if filter_list != []:
                random.choice(filter_list).click()
                if random.choice([True, False]):
                    self.dian_zan()
                pic = random.choice(self.get_img())
                print(pic)
                c.pl(pic=pic)
            else:
                continue



url = "https://www.douyin.com/user/MS4wLjABAAAALQOH6B7EVVq2rSZDgYtErif-N_Sbvqdz3tqbak27pYhC62B61EsiRDnaPvZ_ote7"
c = Cap()
c.pl_pre()


