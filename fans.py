import json
import os.path
import sys
import time

from selenium import webdriver
from selenium.common import *
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

GLOBAL_FANS_URL_LIST = []
errors = [NoSuchElementException, ElementNotInteractableException]
init_fans_str = '''{
    "homeUrl": "",
    "status": 0,
    "count": 0,
    "total": 0,
    "context": []
}
'''


def setup():
    service = Service()
    option = webdriver.ChromeOptions()
    cap = {'performance': 'ALL'}
    option.set_capability('goog:loggingPrefs', cap)
    option.add_experimental_option("detach", True)

    if sys.platform == 'linux':
        option.add_argument(r"user-data-dir=/home/charm/onlyone/pro/douyin_sqlite_bak/test")
        option.binary_location = r'/home/charm/onlyone/pro/douyin_sqlite_bak/selenium/chrome/linux64/131.0.6778.264/chrome'
        service.executable_path = '/home/charm/onlyone/pro/douyin_sqlite_bak/selenium/chromedriver/linux64/131.0.6778.264/chromedriver'
    else:
        option.add_argument(f'user-data-dir=C:{os.environ["HOMEPATH"]}\Documents\cached_google')
        option.binary_location = f'C:{os.environ["HOMEPATH"]}\Documents\chrome-win64\chrome.exe'
        service.executable_path = f'C:{os.environ["HOMEPATH"]}\Documents\chromedriver-win64\chromedriver.exe'
    option.add_argument(r'--disable-gpu-driver-bug-workarounds')
    option.add_argument(r'--no-default-browser-check')
    # option.add_argument("--disable-background-network-ingestion")
    # option.add_argument(r'--disable-background-networking')

    driver = webdriver.Chrome(options=option, service=service)
    return driver


def teardown(driver):
    driver.quit()


# 粉丝关注组件
def fans_component(url=None):
    driver = setup()

    if os.path.isfile('fans.json'):
        with open('fans.json', 'r+') as f:
            fansJ = json.loads(f.read())
            f.seek(0)
            f.truncate()

            print(f"主页链接:{fansJ['homeUrl']}\n采集进度:{fansJ['count']}/{fansJ['total']}")
            if fansJ['total'] == fansJ['count']:
                print("采集完成")
                f.write(init_fans_str)
            else:
                print(f"采集链接:{fansJ['context'][fansJ['count']]}")
                for i, T_url in enumerate(fansJ['context']):
                    if i == fansJ['count']:
                        fansJ['count'] = i
                        f.write(json.dumps(fansJ))
                        fans(driver, T_url['sec_uid'])
    elif url is not None:
        fansJ = json.loads(init_fans_str)
        r = fans(driver, url)
        for i, t in enumerate(r):
            fans(driver, t['sec_uid'])

            fansJ['homeUrl'] = url
            fansJ['status'] = 1
            fansJ['total'] = len(r)
            fansJ['count'] = i
            fansJ['context'] = r
            with open('fans.json', 'w') as f:
                f.write(json.dumps(fansJ))


def fans(driver,
         url="https://www.douyin.com/user/MS4wLjABAAAA3Q_dDfe9fUyv98XebwPhggjNiB7hA2PxfKPH-kQytVw?from_tab_name=main&vid=7443028889464622395"):
    # 昵称 uid 简介 sec_uid 抖音号 精准 蓝v认证 粉丝数 创建时间
    # '{"label_style":5,"label_text":"海南泽优汽车服务有限公司","is_biz_account":1}'
    driver.get(url)

    title = driver.title
    if os.path.isdir('./fans_info') is False:
        os.mkdir("./fans_info")
    user_info_file = os.path.join("./fans_info", title + ".txt")
    print("保存在:", user_info_file)
    user_info_list_into_dict = []

    wait = WebDriverWait(driver, timeout=2, poll_frequency=.2, ignored_exceptions=errors)
    wait.until(lambda d: driver.find_elements(by=By.CLASS_NAME, value="C1cxu0Vq") or True)
    text_box = driver.find_elements(by=By.CLASS_NAME, value="C1cxu0Vq")
    for i in text_box[0:2]:
        i.click()
        node_list = []
        time.sleep(2)
        if driver.find_elements(by=By.CLASS_NAME, value='i5U4dMnB') == []:
            print("隐私用户")
            break
        while True:
            time.sleep(2)
            if driver.find_elements(by=By.CLASS_NAME, value='vc-captcha-close-btn') != []:  # 检测验证
                driver.find_element(by=By.CLASS_NAME, value='vc-captcha-close-btn').click()

            nodes = driver.find_elements(by=By.CLASS_NAME, value='i5U4dMnB')
            try:
                ActionChains(driver).scroll_to_element(nodes[-1]).perform()
            except:
                print("超出索引,粉丝关注列表不存在")
                # 关闭粉丝关注弹窗面板
                driver.find_element(by=By.CLASS_NAME, value='KArYflhI').click()
                break

            log = driver.get_log('performance')
            log_handle_result = log_handle(driver, log)
            if log_handle_result:
                user_info_list_into_dict += log_handle_result
                try:
                    with open(user_info_file, 'a+') as f:
                        for i in log_handle_result:
                            f.write(json.dumps(i) + "\n")
                except OSError:
                    with open('./fans_info/.txt', 'a+') as f:
                        f.write(json.dumps(i) + "\n")
            if len(node_list) == len(nodes):
                break
            node_list = nodes
            driver.implicitly_wait(2)
            print(len(node_list))
        driver.find_element(by=By.CLASS_NAME, value='KArYflhI').click()
    return user_info_list_into_dict


def log_handle(driver, log) -> list:
    fans_list = []
    for i in log:
        logjson = json.loads(i['message'])['message']
        if logjson['method'] == 'Network.responseReceived':
            params = logjson['params']
            requestUrl = params['response']['url']
            # 粉丝
            if 'user/follower/list' in requestUrl:
                requestId = params['requestId']
                response_body = driver.execute_cdp_cmd('Network.getResponseBody', {'requestId': requestId})
                body_data = response_body["body"]
                for i in json.loads(body_data)["followers"]:
                    is_biz_account = False
                    if i['account_cert_info'] is None:
                        is_biz_account = True
                    # user_info = [i['nickname'], i['uid'], i['signature'], "https://www.douyin.com/user/" + i['sec_uid'],
                    #              i['unique_id'], is_biz_account, i['follower_count'], i['following_count']]

                    user_info = {"nickname": i['nickname'],
                                 "uid": i['uid'],
                                 "signature": i['signature'],
                                 "sec_uid": "https://www.douyin.com/user/" + i['sec_uid'],
                                 "unique_id": i['unique_id'],
                                 "is_biz_account": is_biz_account,
                                 "follower_count": i['follower_count'],
                                 "following_count": i['following_count']}
                    fans_list.append(user_info)

            # 关注
            if 'user/following/list' in requestUrl:
                requestId = params['requestId']
                response_body = driver.execute_cdp_cmd('Network.getResponseBody', {'requestId': requestId})
                body_data = response_body["body"]
                for i in json.loads(body_data)["followings"]:
                    is_biz_account = False
                    if i['account_cert_info'] is None:
                        is_biz_account = True
                    # user_info = [i['nickname'], i['uid'], i['signature'], "https://www.douyin.com/user/" + i['sec_uid'],
                    #              i['unique_id'], is_biz_account, i['follower_count'], i['following_count']]
                    # pprint(user_info)
                    user_info = {"nickname": i['nickname'],
                                 "uid": i['uid'],
                                 "signature": i['signature'],
                                 "sec_uid": "https://www.douyin.com/user/" + i['sec_uid'],
                                 "unique_id": i['unique_id'],
                                 "is_biz_account": is_biz_account,
                                 "follower_count": i['follower_count'],
                                 "following_count": i['following_count']}
                    fans_list.append(user_info)
    if fans_list:
        return fans_list


# 昵称	            UID	                 简介	                  SECUID	抖音号	        精准	   蓝V认证	    粉丝数            关注数量
# 猎鹰热清洗设备厂家	1992781461457348	环境清洁综合解决方案服务商。	MS4wLjABAA	vlieyinggaoya		   蓝V	        7383             4075
# nickname          uid                 signature               sec_uid     unique_id                           follower_count  following_count

tip = """***************************
使用方法?
1.直接采集
请直接添加dy主页连接
例如:
    fans.exe "https://www.douyin.com/user/MS4wLjABAAAA3Q_dDfe9fUyv98XebwPhggjNiB7hA2PxfKPH-kQytVw?from_tab_name=main&vid=7443028889464622395"

2.从上次中断处采集
例如:
    fans.exe p
***************************
"""

# option.add_argument(f'user-data-dir=C:{os.environ["HOMEPATH"]}\Documents\cached_google')
# option.binary_location = f'C:\Program Files\Google\Chrome Dev\Application\chrome.exe'
# service.executable_path = f"C:{os.environ['HOMEPATH']}\Documents\chromedriver-win64\chromedriver.exe"

def txt_data_clean(dir='fans_info'):
    if os.path.isdir(dir):
        fd = [os.path.join(dir,i) for i in os.listdir(dir) if i.endswith('.txt')]
        print(fd)

if __name__ == '__main__':
    try:
        if sys.platform == 'win32':
            if os.path.isfile(f'C:{os.environ["HOMEPATH"]}\Documents\chromedriver-win64\chromedriver.exe') is False:
                os.mkdir(f'C:{os.environ["HOMEPATH"]}\Documents\chromedriver-win64')
                with open('chromedriver.exe', 'rb') as f:
                    with open(f'C:{os.environ["HOMEPATH"]}\Documents\chromedriver-win64\chromedriver.exe', 'wb') as exe:
                        exe.write(f.read())
            if os.path.isdir(f'C:{os.environ["HOMEPATH"]}\Documents\cached_google') is False:
                os.mkdir(f'C:{os.environ["HOMEPATH"]}\Documents\cached_google')
            if os.path.isfile(f'C:{os.environ["HOMEPATH"]}\Documents\chrome-win64\chrome.exe') is False:
                print(f'请安装谷歌浏览器到:C:{os.environ["HOMEPATH"]}\Documents\chrome-win64\chrome.exe')
                exit(0)


        if os.path.isfile('fans.json'):
            print("fans.json文件存在")
            fans_component()
        else:
            print("fans.json文件不存在")
            if os.path.isfile('url.txt'):
                with open('url.txt','r',encoding='utf-8') as f:
                    urls = f.readlines()
                for u in urls:
                    print(u)
                    if "https://" in u:
                       fans_component(u)
            exit(0)

        # args = sys.argv
        # if args[1] == 'p':
        #     print("从中断开始")
        #     if os.path.isfile('fans.json'):
        #         print("fans.json文件存在")
        #         fans_component()
        #     else:
        #         print("fans.json文件不存在")
        #         exit(0)
        # elif "https://" in args[1]:
        #     fans_component(args[1])
    except IndexError:
        print(tip)
