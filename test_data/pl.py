from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
import os, sys, time


# 数据抓取
class Cap:
    def __init__(self):
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

    def setup(self, browser='chrome'):
        if browser == 'chrome':
            return webdriver.Chrome(options=self.option, service=self.service)

    @staticmethod
    def teardown(driver):
        driver.quit()


pic = r"C:\Users\ly\Desktop\7880lh.jpg"
url = "https://www.douyin.com/user/MS4wLjABAAAALQOH6B7EVVq2rSZDgYtErif-N_Sbvqdz3tqbak27pYhC62B61EsiRDnaPvZ_ote7?modal_id=7442621376797642019"
url = "https://www.douyin.com/user/MS4wLjABAAAALQOH6B7EVVq2rSZDgYtErif-N_Sbvqdz3tqbak27pYhC62B61EsiRDnaPvZ_ote7?modal_id=7471447189479296308"
c = Cap()
driver = c.setup()


def pl(driver, url, pl_text=None, pic=None):
    driver.get(url)
    time.sleep(5)
    els = driver.find_elements(by=By.CLASS_NAME, value='jp8u3iov')
    els[0].click()

    if pic:
        parent_element = driver.find_elements(by=By.CLASS_NAME, value='comment-input-inner-container')
        child_element = parent_element[0].find_element(By.TAG_NAME, 'input')
        child_element.send_keys(pic)

    time.sleep(2)
    input_div = driver.find_element(by=By.CLASS_NAME, value='lFk180Rt')
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

    if pl_text or pic:
        driver.find_element(by=By.CLASS_NAME, value='WFB7wUOX').click()
        print("发布成功")


pl(driver, url,pl_text='哈哈哈哈哈')
