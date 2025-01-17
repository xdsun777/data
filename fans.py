from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from pprint import pprint
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.common import *
import os.path
import json
import time
import sys
import re

url = "https://www.douyin.com/aweme/v1/web/user/following/list/?device_platform=webapp&aid=6383&channel=channel_pc_web&user_id=2122537659534131&sec_user_id=MS4wLjABAAAAnoZ9Rnmr6kvxgM3wb2IBMYeCj6gttYhW-7zlOepjxch87F9E62f8TgkqMoUqy6d3&offset=0&min_time=0&max_time=1736319532&count=20&source_type=1&gps_access=0&address_book_access=0&is_top=1&update_version_code=170400&pc_client_type=1&pc_libra_divert=Linux&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1536&screen_height=864&browser_language=zh&browser_platform=Linux+x86_64&browser_name=Chrome&browser_version=131.0.0.0&browser_online=true&engine_name=Blink&engine_version=131.0.0.0&os_name=Linux&os_version=x86_64&cpu_core_num=8&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=50&webid=7454097220578002451&uifid=e75c56bdf97dd123c08792ffa35cba4de8d74d7b2bc4961ed76373e52a768f56a3cf650b3477952e13a9bbc61c81ecdab6017fd1f7dde93766cec15cf57aa04fd5357e75aab09bc37f0338ffa81a8093ec551acd29c24077875a27598d9ae85514b88b1c2a22c832c9aa5a1d1af78a40c14479468e3c55f5df1395cecc515027aa0a95cd8af35d75cb56086b073af65e84e3a93b266b413a76641048260553e1&msToken=72HkCZ22PyiV-UWCPJqN9v9el__vSF6xKSOnkjq_xdqf-SyOkFmOsYkX2xrIMqh_b_gM-82T4qrX0abP8ipY5ohal7EumeHKNl9tiyxqD96SG9e1bgGZa744o5dO1vprx6PVRaD9oESvhVwgkcev1GqMaJC1crn9bG0_UIK1vtm4&a_bogus=Ej45hHW7OoQbKd%2FS8csz9V9legV%2FrTSy%2FeioWHoP9NKGGqUb28PBineIbowK4Tv4FSpiweAHUdPMbndbO4X0ZHnkumhkSgkRTtAIIwfo81JdbBJgV1W2ejbEKi4YWAsPKAIJNaEXX0UL1gcfZNcsWFFy9AeJ-%2FR8zqa6pP4g7x8BhemxV2xyTauzxiGe--%2FIsjW%3D&verifyFp=verify_m5ap3bbt_q3cr7vTt_OmLh_40eN_8tXI_C7e4phePvILG&fp=verify_m5ap3bbt_q3cr7vTt_OmLh_40eN_8tXI_C7e4phePvILG"

hander_string = """:authority:
www.douyin.com
:method:
GET
:path:
/aweme/v1/web/user/following/list/?device_platform=webapp&aid=6383&channel=channel_pc_web&user_id=2122537659534131&sec_user_id=MS4wLjABAAAAnoZ9Rnmr6kvxgM3wb2IBMYeCj6gttYhW-7zlOepjxch87F9E62f8TgkqMoUqy6d3&offset=0&min_time=0&max_time=1736319532&count=20&source_type=1&gps_access=0&address_book_access=0&is_top=1&update_version_code=170400&pc_client_type=1&pc_libra_divert=Linux&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1536&screen_height=864&browser_language=zh&browser_platform=Linux+x86_64&browser_name=Chrome&browser_version=131.0.0.0&browser_online=true&engine_name=Blink&engine_version=131.0.0.0&os_name=Linux&os_version=x86_64&cpu_core_num=8&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=50&webid=7454097220578002451&uifid=e75c56bdf97dd123c08792ffa35cba4de8d74d7b2bc4961ed76373e52a768f56a3cf650b3477952e13a9bbc61c81ecdab6017fd1f7dde93766cec15cf57aa04fd5357e75aab09bc37f0338ffa81a8093ec551acd29c24077875a27598d9ae85514b88b1c2a22c832c9aa5a1d1af78a40c14479468e3c55f5df1395cecc515027aa0a95cd8af35d75cb56086b073af65e84e3a93b266b413a76641048260553e1&msToken=72HkCZ22PyiV-UWCPJqN9v9el__vSF6xKSOnkjq_xdqf-SyOkFmOsYkX2xrIMqh_b_gM-82T4qrX0abP8ipY5ohal7EumeHKNl9tiyxqD96SG9e1bgGZa744o5dO1vprx6PVRaD9oESvhVwgkcev1GqMaJC1crn9bG0_UIK1vtm4&a_bogus=Ej45hHW7OoQbKd%2FS8csz9V9legV%2FrTSy%2FeioWHoP9NKGGqUb28PBineIbowK4Tv4FSpiweAHUdPMbndbO4X0ZHnkumhkSgkRTtAIIwfo81JdbBJgV1W2ejbEKi4YWAsPKAIJNaEXX0UL1gcfZNcsWFFy9AeJ-%2FR8zqa6pP4g7x8BhemxV2xyTauzxiGe--%2FIsjW%3D&verifyFp=verify_m5ap3bbt_q3cr7vTt_OmLh_40eN_8tXI_C7e4phePvILG&fp=verify_m5ap3bbt_q3cr7vTt_OmLh_40eN_8tXI_C7e4phePvILG
:scheme:
https
accept:
application/json, text/plain, */*
accept-encoding:
gzip, deflate, br, zstd
accept-language:
zh,zh-TW;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6
bd-ticket-guard-client-data:
eyJ0c19zaWduIjoidHMuMi4zNWJiOWEwYjZjMDkyOWFlOTYyMjA2Zjg5YTcxY2I0NDZiNTcyMGE1NDY2YmNkZDc1NzI0YzFjMzI2YTIwZjVlYzRmYmU4N2QyMzE5Y2YwNTMxODYyNGNlZGExNDkxMWNhNDA2ZGVkYmViZWRkYjJlMzBmY2U4ZDRmYTAyNTc1ZCIsInJlcV9jb250ZW50IjoidGlja2V0LHBhdGgsdGltZXN0YW1wIiwicmVxX3NpZ24iOiJ0aXBjbHN4QU41a1FEZmJDNTBRKzR1WjhNUUwrRFE1NHFwT3hTMXJKaXdBPSIsInRpbWVzdGFtcCI6MTczNjMxOTUyN30=
bd-ticket-guard-iteration-version:
1
bd-ticket-guard-ree-public-key:
BOaUYCNSu0+aMflkkEY7a6VfvZuXFHNuNunBgLI8LlR51TangFEgjAjZldhVKP7V2AfDzfCJFxIO4AR2RZovfyE=
bd-ticket-guard-version:
2
bd-ticket-guard-web-sign-type:
1
bd-ticket-guard-web-version:
2
cookie:
ttwid=1%7CicfEZFf5kqHOt54uHVYvx9GhLKl0Gsdl-ZoJ6dTDsKU%7C1735542274%7C2196f97867bd2bc9102258ad636539ed0e34640c53b4e025ef115357c6cc3e97; UIFID_TEMP=e75c56bdf97dd123c08792ffa35cba4de8d74d7b2bc4961ed76373e52a768f56011c164989f42932497884fa06859620c54470fcc08d4e0653ac3f9adf856ea7f9958eb59be6998dba7ede3a47f33f80; s_v_web_id=verify_m5ap3bbt_q3cr7vTt_OmLh_40eN_8tXI_C7e4phePvILG; dy_swidth=1536; dy_sheight=864; is_dash_user=0; FORCE_LOGIN=%7B%22videoConsumedRemainSeconds%22%3A180%7D; passport_csrf_token=738935f0174e0b9c63b17cbaa07e0192; passport_csrf_token_default=738935f0174e0b9c63b17cbaa07e0192; fpk1=U2FsdGVkX1+f1zkKmwyaTeFgiisZw2E2uXtWGrcC9EbXuc8Wxw9yRxgc6VgDar+pbGVWVZGTlLMVFcDr4as9ww==; fpk2=a11f5da7336cfe2e2fd950a3d968fdb0; __security_mc_1_s_sdk_crypt_sdk=8035d7c6-4eeb-8742; bd_ticket_guard_client_web_domain=2; UIFID=e75c56bdf97dd123c08792ffa35cba4de8d74d7b2bc4961ed76373e52a768f56a3cf650b3477952e13a9bbc61c81ecdab6017fd1f7dde93766cec15cf57aa04fd5357e75aab09bc37f0338ffa81a8093ec551acd29c24077875a27598d9ae85514b88b1c2a22c832c9aa5a1d1af78a40c14479468e3c55f5df1395cecc515027aa0a95cd8af35d75cb56086b073af65e84e3a93b266b413a76641048260553e1; __ac_nonce=0677e200e00e0279a8d15; __ac_signature=_02B4Z6wo00f01AADPOwAAIDD7ltolj332bQAIzhAAGeF54; csrf_session_id=0c4b16d98f2d1cb8ff9b7a0827369769; strategyABtestKey=%221736318993.898%22; gulu_source_res=eyJwX2luIjoiOTExNWRkYzU1NWVjYmYwYzYzMjQ3MTdhOGM0Nzc0ZmVhNTliMGMzNzRkMmJlNWEwMjFhNzU3MjViZTM2OTdhNSJ9; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Afalse%2C%22volume%22%3A1%7D; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1536%2C%5C%22screen_height%5C%22%3A864%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A8%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A50%7D%22; sdk_source_info=7e276470716a68645a606960273f276364697660272927676c715a6d6069756077273f276364697660272927666d776a68605a607d71606b766c6a6b5a7666776c7571273f275e58272927666a6b766a69605a696c6061273f27636469766027292762696a6764695a7364776c6467696076273f275e5827292771273f273533313631373c3436333632342778; bit_env=n5v1MCYzD_fcamEpj8J399HHqjv0Je4gqEgmD6PNHNsxVa9BaGn5KCPGPzIL_7haRPqHNHcj8pp2S-MePnASyH32puGrEFGFXYO4q4SlrqL3fFiigrMHBstonDfS5ivmsH0IG7zlGPWlr5E9zTUlRTwZVS2vpHKj5VQ25YQo544HrbSN1rbtDa_uYtTUiYxN4Za6F3-v_lCxylik69GJXtGMmUEGfVHE1A3sAg3bDOrEvQfLJnkzYc9HL0DVOgFTeJC_E4_A7YJD6Sv_HkDuMRTYOHhGr0VFitbuZzxjluonO0urwLublIUscSh_I1eOb6ukHjaDau1lbWkDLItnSTcvfZc1nWM2fwe6COya-A6xqOA8hgItYJ2jfQBhC_VH70DSJ71cH4mbs0otAfPMcqTmpJ8DJMkGdyJQ-iy8vBx0Kdvo8A23-BbUGMnXJlVAUa51iEJPCygkQxRjZ0q-DfVXWqdl-cSiJS_aaRSGzSlw-lsHxJ0x6qG2tJeuf-U8; passport_mfa_token=CjdEu54Q8n5%2B7L%2FnPIzjDRSmphGDL5N4CH4Uafv8I%2Feauqj2SS2L0e6lLWaaTg8wagjcFUGOrJ9eGkoKPCS9LAxzYCZR8Xff2NIyn%2BiZxJVt%2B30pWMcb9Uw8KcOqLbSjV%2F9edJEqGfTLECRTq%2BNXAMjhdeaQ77mIohD3oOYNGPax0WwgAiIBA972Qyg%3D; d_ticket=62076b2b0d771b726f2fc5668a3cd8a1cb0f5; passport_assist_user=CkGH46E9G_Trn-Wg7FJpyNIfHVV-KEHqgcdaecmdpKSuzbOY8_85YIe3H5NpE50yKre-HoXZvPJ9_CyV0ydpixeByRpKCjw4HuyyFOpysZlfwON6AL0-L4JYr81LxwsJyYXGVVI0RLVf1L-ygK21vhGdMBKV3nPnzUVxsoJwCiORPqUQ3qLmDRiJr9ZUIAEiAQOzPApT; n_mh=EMlfNUz7Yr5D8Hw7xwVqtNJ6llaNVxU4PGfzuLgUoMg; sso_uid_tt=b3853a65f8dfa59bb98d4790614be7ce; sso_uid_tt_ss=b3853a65f8dfa59bb98d4790614be7ce; toutiao_sso_user=59f1fca7de958613461cab083c5a8f94; toutiao_sso_user_ss=59f1fca7de958613461cab083c5a8f94; sid_ucp_sso_v1=1.0.0-KDExZjJmYWVkNjBiYTg1ZGFjYTgxMTFhYTQ2OGVjMzk2MWFhZGU2NTMKIQiQsNCZjc3SBBDNwvi7BhjvMSAMMO3mtKwGOAZA9AdIBhoCbGYiIDU5ZjFmY2E3ZGU5NTg2MTM0NjFjYWIwODNjNWE4Zjk0; ssid_ucp_sso_v1=1.0.0-KDExZjJmYWVkNjBiYTg1ZGFjYTgxMTFhYTQ2OGVjMzk2MWFhZGU2NTMKIQiQsNCZjc3SBBDNwvi7BhjvMSAMMO3mtKwGOAZA9AdIBhoCbGYiIDU5ZjFmY2E3ZGU5NTg2MTM0NjFjYWIwODNjNWE4Zjk0; __security_mc_1_s_sdk_sign_data_key_sso=c292a696-4a9c-96b4; __security_mc_1_s_sdk_cert_key=05058102-44d9-95d1; login_time=1736319310954; passport_auth_status=69fe8cfba428c59a5f901d90129b186c%2C; passport_auth_status_ss=69fe8cfba428c59a5f901d90129b186c%2C; uid_tt=e5a410d8b2445031586c2fd8d4c3a40d; uid_tt_ss=e5a410d8b2445031586c2fd8d4c3a40d; sid_tt=88ef478f80dee6034f8ffdaf6ae30483; sessionid=88ef478f80dee6034f8ffdaf6ae30483; sessionid_ss=88ef478f80dee6034f8ffdaf6ae30483; is_staff_user=false; SelfTabRedDotControl=%5B%5D; _bd_ticket_crypt_doamin=2; _bd_ticket_crypt_cookie=b1b6726901e86102b43abcc2e8018822; __security_mc_1_s_sdk_sign_data_key_web_protect=0c51fb3a-4abd-bc76; __security_server_data_status=1; biz_trace_id=1e59085d; store-region=cn-hb; store-region-src=uid; __security_mc_1_s_sdk_sign_data_key_login=b14f7b8a-4a4a-86f5; publish_badge_show_info=%220%2C0%2C0%2C1736319321374%22; sid_guard=88ef478f80dee6034f8ffdaf6ae30483%7C1736319322%7C5183990%7CSun%2C+09-Mar-2025+06%3A55%3A12+GMT; sid_ucp_v1=1.0.0-KDQwMjRhYWY1OTUwZWJmZWI2OGZkNjFlNmRmODk0OTlkNjlkOTUzOTcKGwiQsNCZjc3SBBDawvi7BhjvMSAMOAZA9AdIBBoCbGYiIDg4ZWY0NzhmODBkZWU2MDM0ZjhmZmRhZjZhZTMwNDgz; ssid_ucp_v1=1.0.0-KDQwMjRhYWY1OTUwZWJmZWI2OGZkNjFlNmRmODk0OTlkNjlkOTUzOTcKGwiQsNCZjc3SBBDawvi7BhjvMSAMOAZA9AdIBBoCbGYiIDg4ZWY0NzhmODBkZWU2MDM0ZjhmZmRhZjZhZTMwNDgz; home_can_add_dy_2_desktop=%221%22; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCT2FVWUNOU3UwK2FNZmxra0VZN2E2VmZ2WnVYRkhOdU51bkJnTEk4TGxSNTFUYW5nRkVnakFqWmxkaFZLUDdWMkFmRHpmQ0pGeElPNEFSMlJab3ZmeUU9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoyfQ%3D%3D; IsDouyinActive=false; passport_fe_beating_status=true; odin_tt=1c8f3c4b35d692c53cbffa9b3ba4d110eabcae9c6b32210ba90247f974b5668b5cbd1ce048dcdb71aa89be47f49693bf
priority:
u=1, i
referer:
https://www.douyin.com/user/MS4wLjABAAAAnoZ9Rnmr6kvxgM3wb2IBMYeCj6gttYhW-7zlOepjxch87F9E62f8TgkqMoUqy6d3?from_tab_name=main
sec-ch-ua:
"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"
sec-ch-ua-mobile:
?0
sec-ch-ua-platform:
"Linux"
sec-fetch-dest:
empty
sec-fetch-mode:
cors
sec-fetch-site:
same-origin
uifid:
e75c56bdf97dd123c08792ffa35cba4de8d74d7b2bc4961ed76373e52a768f56a3cf650b3477952e13a9bbc61c81ecdab6017fd1f7dde93766cec15cf57aa04fd5357e75aab09bc37f0338ffa81a8093ec551acd29c24077875a27598d9ae85514b88b1c2a22c832c9aa5a1d1af78a40c14479468e3c55f5df1395cecc515027aa0a95cd8af35d75cb56086b073af65e84e3a93b266b413a76641048260553e1
user-agent:
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36
"""
GLOBAL_FANS_URL_LIST = []


def header_handle(h: str):
    dict_header = {}
    s_h = h.split('\n')
    if s_h[-1] == "":
        s_h.pop(-1)
    temp_key = ""
    for (i, t) in enumerate(s_h):
        s = re.sub(':', "", t)
        if i % 2 == 0:
            dict_header[s] = ""
            temp_key = s
        else:
            dict_header[temp_key] = t
    return dict_header


errors = [NoSuchElementException, ElementNotInteractableException]

fans_json_init = {
  "homeUrl": "",
  "status": 0,
  "total": 10,
  "count": 0,
  "context": []
}

# 粉丝关注组件
def fans_components():
    init_url = "https://www.douyin.com/user/MS4wLjABAAAA3Q_dDfe9fUyv98XebwPhggjNiB7hA2PxfKPH-kQytVw?from_tab_name=main&vid=7443028889464622395"
    # init_url="https://www.douyin.com/user/MS4wLjABAAAAGRXX0YDHtAKwELlQ4IBx-PPXgrzW9l0A7Obb2YdnYh03KegT0uzE-vWjEkfptEBc?from_tab_name=main"
    # init_url = "https://www.douyin.com/user/MS4wLjABAAAAl2tNkF2zDV3vcvxk4BnOEek1bGgfdLsoAVEXZTWWpD3NNa4Fvz1p77mkxHhaPOOy"
    driver = setup()

    if os.path.isfile('./fans.json'):
        with open('fans.json','r') as f:
            fansJ = json.loads(f.read())
    else:
        fansJ = json.loads(fans_json_init)

    if fansJ['status'] == 0:
        r = fans(driver, init_url)
        for i,t in enumerate(r):
            fans(driver, t['sec_uid'])

            fansJ['homeUrl'] = init_url
            fansJ['status'] = 1
            fansJ['total'] = len(r)
            fansJ['count'] = i
            fansJ['context'] = r
            with open('fans.json', 'w') as f:
                f.write(json.dumps(fansJ))
    else:
        count = fansJ['count']
        for i,t in enumerate(fansJ['context'][fansJ['count']:fansJ['total']]):
            if i < count:
                continue
            fans(driver,t['sec_uid'])
            fansJ['status'] = 1
            fansJ['count'] = i
            with open('fans.json', 'w') as f:
                f.write(json.dumps(fansJ))


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
        option.add_argument(r'user-data-dir=C:\Users\ly\Documents\cached_google')
        option.binary_location = r'C:\Program Files\Google\Chrome Dev\Application\chrome.exe'
        service.executable_path = r'C:\Users\ly\Documents\chromedriver-win64\chromedriver.exe'
    # option.add_argument("--disable-background-network-ingestion")
    # option.add_argument(r'--no-default-browser-check')
    # option.add_argument(r'--disable-background-networking')
    # option.add_argument(r'--disable-gpu-driver-bug-workarounds')

    driver = webdriver.Chrome(options=option, service=service)
    return driver


def teardown(driver):
    driver.quit()


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
            finally:
                driver.find_element(by=By.CLASS_NAME, value='KArYflhI').click()
                print("超出索引,粉丝关注列表不存在")
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
                    with open('./fans_info/.txt','a+') as f:
                        f.write(json.dumps(i)+"\n")
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


# setup()
fans_components()

# 昵称	            UID	                 简介	                  SECUID	抖音号	        精准	   蓝V认证	    粉丝数            关注数量
# 猎鹰热清洗设备厂家	1992781461457348	环境清洁综合解决方案服务商。	MS4wLjABAA	vlieyinggaoya		   蓝V	        7383             4075
# nickname          uid                 signature               sec_uid     unique_id                           follower_count  following_count
# with open('info_list.txt','r') as f:
#     d = f.readlines()
#     for i in d:
#         print(json.loads(i))
