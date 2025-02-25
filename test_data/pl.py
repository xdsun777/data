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
            return [os.path.join(now_dir,img) for img in os.listdir('img') if (img.endswith('jpg') or img.endswith('png') or img.endswith('jpeg')) and 'zl' in img ]
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

# 总数：total 评论内容：text:str   回复总数：reply_comment_total 回复内容：reply_comment[] 用户信息：user:
# [uid,short_id,nickname,sec_uid]
https://www.douyin.com/user/MS4wLjABAAAA40KxWaYeFOZOOmdBeRwskW5k3bYD2Iq3GUv9Yjeoce0
{
  "cid": "7464207945624011580",
  "text": "[赞][赞][赞][赞]",
  "aweme_id": "7462230819956854076",
  "create_time": 1737896343,
  "digg_count": 0,
  "status": 1,
  "user": {
    "uid": "2207429485159517",
    "short_id": "3561486850",
    "nickname": "用户7022719567781",
    "signature": "",
    "avatar_larger": {
      "uri": "1080x1080/aweme-avatar/tos-cn-i-0813_ce813ed3d7ef4be09973698b54a9595a",
      "url_list": [
        "https://p3-pc.douyinpic.com/aweme/1080x1080/aweme-avatar/tos-cn-i-0813_ce813ed3d7ef4be09973698b54a9595a.jpeg?from=2956013662"
      ],
      "width": 720,
      "height": 720
    },
    "avatar_thumb": {
      "uri": "100x100/aweme-avatar/tos-cn-i-0813_ce813ed3d7ef4be09973698b54a9595a",
      "url_list": [
        "https://p3-pc.douyinpic.com/aweme/100x100/aweme-avatar/tos-cn-i-0813_ce813ed3d7ef4be09973698b54a9595a.jpeg?from=2956013662"
      ],
      "width": 720,
      "height": 720
    },
    "avatar_medium": {
      "uri": "720x720/aweme-avatar/tos-cn-i-0813_ce813ed3d7ef4be09973698b54a9595a",
      "url_list": [
        "https://p3-pc.douyinpic.com/aweme/720x720/aweme-avatar/tos-cn-i-0813_ce813ed3d7ef4be09973698b54a9595a.jpeg?from=2956013662"
      ],
      "width": 720,
      "height": 720
    },
    "is_verified": true,
    "follow_status": 0,
    "aweme_count": 0,
    "following_count": 0,
    "follower_count": 0,
    "favoriting_count": 0,
    "total_favorited": 0,
    "is_block": false,
    "hide_search": false,
    "constellation": 0,
    "mate_add_permission": 0,
    "hide_location": false,
    "weibo_verify": "",
    "custom_verify": "",
    "unique_id": "dyuw3i89zv76",
    "familiar_confidence": 0,
    "special_lock": 1,
    "need_recommend": 0,
    "is_binded_weibo": false,
    "weibo_name": "",
    "weibo_schema": "",
    "weibo_url": "",
    "story_open": false,
    "story_count": 0,
    "has_facebook_token": false,
    "has_twitter_token": false,
    "fb_expire_time": 0,
    "tw_expire_time": 0,
    "has_youtube_token": false,
    "youtube_expire_time": 0,
    "room_id": 0,
    "live_verify": 0,
    "authority_status": 0,
    "verify_info": "",
    "shield_follow_notice": 0,
    "shield_digg_notice": 0,
    "shield_comment_notice": 0,
    "mate_relation": {
      "mate_status": 0,
      "mate_apply_forward": 0,
      "mate_apply_reverse": 0
    },
    "private_relation_list": null,
    "creator_tag_list": null,
    "with_commerce_entry": false,
    "verification_type": 1,
    "enterprise_verify_reason": "",
    "is_ad_fake": false,
    "batch_unfollow_contain_tabs": null,
    "region": "CN",
    "account_region": "",
    "sync_to_toutiao": 0,
    "commerce_user_level": 0,
    "live_agreement": 0,
    "platform_sync_info": null,
    "with_shop_entry": false,
    "is_discipline_member": false,
    "secret": 0,
    "has_orders": false,
    "prevent_download": false,
    "show_image_bubble": false,
    "geofencing": [],
    "unique_id_modify_time": 1740388904,
    "video_icon": {
      "uri": "",
      "url_list": [],
      "width": 720,
      "height": 720
    },
    "ins_id": "",
    "google_account": "",
    "youtube_channel_id": "",
    "youtube_channel_title": "",
    "apple_account": 0,
    "with_dou_entry": false,
    "with_fusion_shop_entry": false,
    "is_phone_binded": false,
    "accept_private_policy": false,
    "twitter_id": "",
    "twitter_name": "",
    "user_canceled": false,
    "has_email": false,
    "is_gov_media_vip": false,
    "live_agreement_time": 0,
    "status": 1,
    "avatar_uri": "aweme-avatar/tos-cn-i-0813_ce813ed3d7ef4be09973698b54a9595a",
    "follower_status": 0,
    "neiguang_shield": 0,
    "comment_setting": 0,
    "duet_setting": 0,
    "reflow_page_gid": 0,
    "reflow_page_uid": 0,
    "user_rate": 1,
    "download_setting": -1,
    "download_prompt_ts": 0,
    "react_setting": 0,
    "live_commerce": false,
    "cover_url": [
      {
        "uri": "c8510002be9a3a61aad2",
        "url_list": [
          "https://p9-pc-sign.douyinpic.com/obj/c8510002be9a3a61aad2?lk3s=b031305e&x-expires=1741597200&x-signature=6Xl9Bvmy15aKHSYr6m05eplE1iI%3D&from=2956013662",
          "https://p3-pc-sign.douyinpic.com/obj/c8510002be9a3a61aad2?lk3s=b031305e&x-expires=1741597200&x-signature=3dgyJBHxKBSlB7Nt1e%2B%2FjJWr6ZQ%3D&from=2956013662"
        ],
        "width": 720,
        "height": 720
      }
    ],
    "show_gender_strategy": 0,
    "language": "zh-Hans",
    "has_insights": false,
    "item_list": null,
    "user_mode": 0,
    "user_period": 0,
    "has_unread_story": false,
    "new_story_cover": null,
    "is_star": false,
    "cv_level": "",
    "type_label": null,
    "ad_cover_url": null,
    "comment_filter_status": 0,
    "avatar_168x168": {
      "uri": "168x168/aweme-avatar/tos-cn-i-0813_ce813ed3d7ef4be09973698b54a9595a",
      "url_list": [
        "https://p3-pc.douyinpic.com/img/aweme-avatar/tos-cn-i-0813_ce813ed3d7ef4be09973698b54a9595a~c5_168x168.jpeg?from=2956013662"
      ],
      "width": 720,
      "height": 720
    },
    "avatar_300x300": {
      "uri": "300x300/aweme-avatar/tos-cn-i-0813_ce813ed3d7ef4be09973698b54a9595a",
      "url_list": [
        "https://p3-pc.douyinpic.com/img/aweme-avatar/tos-cn-i-0813_ce813ed3d7ef4be09973698b54a9595a~c5_300x300.jpeg?from=2956013662"
      ],
      "width": 720,
      "height": 720
    },
    "relative_users": null,
    "cha_list": null,
    "sec_uid": "MS4wLjABAAAAzZNGYKZ0gliOktLwehagYcEps0vF10kFzIzGYmUsFgN9pGWJsOErH-hhvAIq6FFS",
    "urge_detail": {
      "user_urged": 0
    },
    "need_points": null,
    "homepage_bottom_toast": null,
    "can_set_geofencing": null,
    "room_id_str": "0",
    "white_cover_url": null,
    "user_tags": null,
    "stitch_setting": 0,
    "is_mix_user": false,
    "enable_nearby_visible": false,
    "ban_user_functions": [],
    "aweme_control": {
      "can_forward": true,
      "can_share": true,
      "can_comment": true,
      "can_show_comment": true
    },
    "user_not_show": 1,
    "ky_only_predict": 0,
    "user_not_see": 0,
    "card_entries": null,
    "signature_display_lines": 0,
    "display_info": null,
    "follower_request_status": 0,
    "live_status": 0,
    "is_not_show": false,
    "card_entries_not_display": null,
    "card_sort_priority": null,
    "show_nearby_active": false,
    "interest_tags": null,
    "school_category": 0,
    "search_impr": {
      "entity_id": "2207429485159517"
    },
    "link_item_list": null,
    "user_permissions": null,
    "offline_info_list": null,
    "is_cf": 0,
    "is_blocking_v2": false,
    "is_blocked_v2": false,
    "close_friend_type": 0,
    "signature_extra": null,
    "max_follower_count": 0,
    "personal_tag_list": null,
    "cf_list": null,
    "im_role_ids": null,
    "not_seen_item_id_list": null,
    "batch_unfollow_relation_desc": null,
    "contacts_status": 1,
    "risk_notice_text": "",
    "follower_list_secondary_information_struct": null,
    "endorsement_info_list": null,
    "text_extra": null,
    "contrail_list": null,
    "data_label_list": null,
    "not_seen_item_id_list_v2": null,
    "is_ban": false,
    "special_people_labels": null,
    "special_follow_status": 0,
    "familiar_visitor_user": null,
    "live_high_value": 0,
    "awemehts_greet_info": "",
    "avatar_schema_list": null,
    "profile_mob_params": null,
    "disable_image_comment_saved": 0,
    "verification_permission_ids": null
  },
  "reply_id": "0",
  "user_digged": 0,
  "reply_comment": null,
  "text_extra": [],
  "label_text": "",
  "label_type": -1,
  "reply_comment_total": 0,
  "reply_to_reply_id": "0",
  "is_author_digged": false,
  "stick_position": 0,
  "user_buried": false,
  "label_list": null,
  "is_hot": false,
  "text_music_info": null,
  "image_list": null,
  "is_note_comment": 0,
  "ip_label": "海南",
  "can_share": true,
  "item_comment_total": 16,
  "level": 1,
  "video_list": null,
  "sort_tags": "{\"reply_0\":1}",
  "is_user_tend_to_reply": false,
  "content_type": 1,
  "is_folded": false,
  "enter_from": "homepage_hot"
}