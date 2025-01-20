import json
import os.path
from binascii import a2b_qp

from temp_data import city_data
# noinspection PyUnresolvedReferences
import requests, time
from excel import *
from sql import *


class DataHandle:
    """数据处理类"""

    def __dir__(self):
        pass

    def __init__(self, origin_data):
        if type(origin_data) is list:
            self._data = origin_data
        else:
            print("数据必须是list类型")
            exit(-1)
        self._final_data = None
        self._temp_data = None

        self.create_time = time.strftime('%Y-%m-%d %H:%M:%S')

    @staticmethod
    def get_place(phone):
        """获取手机号归属地"""
        url = 'https://cx.shouji.360.cn/phonearea.php?number=18942955144' + phone
        rs = requests.get(url)
        d = rs.json().get('data')
        try:
            # return 市
            return d.get('city')
        except AttributeError:
            print("data没有city属性，返回空")
            return None

    @staticmethod
    def qx_to_s(qx):
        """市县区 转 省"""
        for s in city_data:
            if qx is not None and type(qx) != 'NoneType':
                _h = qx + "市"
                _x = qx + "县"
                _z = qx + "镇"
                if qx in city_data[s] or _h in city_data[s] or _x in city_data[s] or _z in city_data[s]:
                    return s
        # print("未找到该地区所在省份")
        return None

    def handle_zhibo(self):
        """src: 编号 用户昵称 勋章等级 动作 抖音号 sec_uid uid 简介 粉丝 关注 性别 地区 精准 时间
            dct: 编号 用户昵称 勋章等级 动作 抖音号 sec_uid uid 简介 粉丝 关注 性别 地区 精准 时间 创建时间 主播昵称 省份
            42(10002),修油缸气缸,7,进入直播间,2027451038,MS4wLjABAAAAlC5jq0Db2nz58qZdzVs1DHCDXK6 - bbIpf - RL5KPfZ7Q,98425843564,修油缸气缸18852041880,771,484,男 ,18852041880,2024 - 12 - 2814: 51:33
            :return: [[],[]]
            """
        all_data: list = []
        for f in self._data:
            # TODO 数据处理部分
            # 新增 省份 创建时间 主播昵称
            # 过滤查询手机号归属地，并设置
            if f[12] is not None:
                if ',' in f[12]:
                    f[12] = f[12].removeprefix(',')
                if f[11] is None:
                    f[11] = self.get_place(f[12])
                    print(f[11])

                s_result = self.qx_to_s(f[11])
                # 处理用户主页sec——uid
                f[5] = "https://www.douyin.com/user/" + f[5]

                # 创建时间
                f.append(self.create_time)

                # 主播昵称
                if "10002" in f[0] or "10005" in f[0] or "10008" in f[0] or "10014" in f[0]:
                    f.append("猎鹰蒸汽喷抽清洗机厂家")
                else:
                    f.append("猎鹰热清洗设备厂家")
                # 省份
                if s_result is None:
                    f.append("其他地区")
                else:
                    f.append(s_result)
            all_data.append(f)
        return all_data

    def handler_fensi(self, from_data, create_time=None):
        """
            昵称	UID	简介	SECUID	抖音号	精准	蓝V认证	粉丝数 创建时间 from
            粉丝关注列表数据处理
            :return: [[],[]]
        """
        if not create_time:
            create_time = self.create_time
        all_data = []
        for i in self._data:
            i[4] = "https://www.douyin.com/user/" + i[4]
            i.pop(0)
            i.append(create_time)
            i.append(from_data)
            all_data.append(i)
        return all_data

    def handle_pinglun(self):
        """视频链接,时间,昵称,评论内容,uid,抖音号,性别,简介,粉丝,关注,精准,头像 ,sec_uid,创建时间,地区"""
        all_data = []
        for i in self._data:
            i[14] = "https://www.douyin.com/user/" + i[14]
            i.append(time.strftime('%Y-%m-%d %H:%M:%S'))
            # i.append(i[8])
            i.pop(0)
            all_data.append(i)
        return all_data

    def douyin_live_clean(self):
        # sq = """SELECT 用户昵称,简介,动作,抖音号,sec_uid,uid FROM "main"."zhibo" GROUP BY "UID"
        # """
        # s = Select(sql_code=sq)
        # date = s.get_all_data()
        print(len(self._data))
        temp = []
        words = ['清', '洗', '什么', '油', '烟', '多', '少', '价', '米', '地址', '位置', '汽', '美', '车', '洁', '膜',
                 '修']
        with open('uid.txt', 'w') as f:
            for i in self._data:
                d = str(i[0]) + str(i[1]) + str(i[2])
                for a in words:
                    if a in d:
                        temp.append(i)
                        f.write(i[-1] + "\n")
        print(len(temp))

    def dy_fans_clean(self):
        clean_filed = ['车', '洗', '高压', '清', '油', '烟', '厨', '管', '道', '机', '结']
        clean_data = []
        with open('secuid.txt', 'w') as f:
            for i in self._data:
                d = str(i[0]) + str(i[1])
                for a in clean_filed:
                    if a in d:
                        clean_data.append(i)
                        f.write(i[-1] + "\n")
        print(clean_data)

    def dy_fans_json2xsl(self, fans_info):
        data_list = []
        now_time = time.strftime('%y-%m-%d')
        if os.path.isdir(fans_info):
            for i in os.listdir(fans_info):
                if i.endswith('.txt') and os.path.isfile(os.path.join(fans_info, i)):
                    with open(os.path.join(fans_info, i), 'r') as f:
                        jsd = f.readlines()
                        for x in jsd:
                            x = json.loads(x)
                            data = [x['nickname'], x['uid'], x['signature'], x['sec_uid'], x['unique_id'], '',
                                    x['is_biz_account'], x['follower_count'], now_time]
                            data_list.append(data)

        if data_list:
            ex = Write('uid.xlsx', FILED_FenSi, data_list)
            ex.write_fensi_data()

    @staticmethod
    def clean_txt(fans_info):
        clean_data = []
        clean_filed = ['车', '洗', '高压', '清', '油', '烟', '厨', '管', '道', '机', '结']
        if os.path.isdir(fans_info):
            files = [os.path.join(fans_info, i) for i in os.listdir(fans_info) if i.endswith('.txt')]
            for i in files:
                with open(i, 'r') as f:
                    da = f.readlines()
                    for x in da:
                        js = json.loads(x)
                        if js['uid'] not in clean_data:
                            d = str(js['nickname']) + str(js['sec_uid'])
                            for a in clean_filed:
                                if a in d:
                                    with open('json2excel.txt', 'a+') as f:
                                        f.write(x)
                                    clean_data.append(i)

if __name__ == '__main__':
    start = time.time()
    sql_code = """
    SELECT 昵称,简介,sec_uid FROM "main"."fensi"  GROUP BY "UID";
    """
    # s = Select(sql_code=sql_code)
    # data = s.get_all_data()
    hd = DataHandle([])
    hd.dy_fans_json2xsl(fans_info='source/temp')

    print("执行时间：", time.time() - start)
