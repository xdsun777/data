from selenium.common import ElementNotInteractableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.common import *
from selenium import webdriver
import sys,os


ERRORS = [NoSuchElementException, ElementNotInteractableException]


def __init__():
    base_path = os.path.dirname(os.path.abspath(__file__))
    source_path = os.path.join(base_path, 'source')
    service = Service()
    option = webdriver.ChromeOptions()
    cap = {'performance': 'ALL'}
    option.set_capability('goog:loggingPrefs', cap)
    option.add_experimental_option("detach", True)

    option.add_argument(f'user-data-dir={os.path.join(source_path,"cached_google")}')
    if sys.platform == 'linux':
        option.binary_location = f'{os.path.join(source_path, "chrome/chrome")}'
        service.executable_path = f'{os.path.join(source_path,"chromedriver")}'
    else:
        option.binary_location = f'{os.path.join(source_path,"chrome/chrome.exe")}'
        service.executable_path = f'{os.path.join(source_path,"chromedriver.exe")}'
    print(os.path.join(source_path,"cached_google"))
    option.add_argument(r'--disable-gpu-driver-bug-workarounds')
    option.add_argument(r'--no-default-browser-check')
    option.add_argument("--disable-gpu")  # 适用于 Linux 和 Windows 系统
    option.add_argument("--no-sandbox")  # Bypass OS security model
    option.add_argument("--disable-extensions")
    option.add_argument("--enable-unsafe-swiftshader")
    option.add_argument("--disable-3d-apis")
    # option.add_argument("--headless")  # 使用无头模式
    # option.add_argument("start-maximized")  # 启动最大化窗口
    # option.add_argument("disable-infobars")
    # option.add_argument("--disable-background-network-ingestion")
    # option.add_argument(r'--disable-background-networking')
    return webdriver.Chrome(options=option, service=service)