from temp_data import city_data
import requests,time
from excel import *
from sql import *

class DataHandle:
    """数据处理类"""
    def __dir__(self):
        pass
    def __init__(self,origin_data):
        if type(origin_data) is list and type(origin_data[0]) is list:
            self._data = origin_data
        else:
            print("数据必须是二维list类型")
            exit(-1)
        self._final_data = None
        self._temp_data = None


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
                h = qx + "市"
                x = qx + "县"
                z = qx + "镇"
                if qx in city_data[s] or h in city_data[s] or x in city_data[s] or z in city_data[s]:
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
                f.append(time.strftime("%Y-%m-%d %H:%M:%S"))

                # 主播昵称
                if "10002" in f[0] or "10005" in f[0]:
                    f.append("猎鹰蒸汽喷抽清洗机厂家")
                if "10008" in f[0]:
                    f.append("陕西绿霸高压清洗机")
                if "10011" in f[0]:
                    f.append("巴诺德清洗机")
                if "10014" in f[0]:
                    f.append("黑猫精英高压商用洗车机")
                if "10017" in f[0]:
                    f.append("奔启洗车机—工厂")
                if "10020" in f[0]:
                    f.append("KARCHER卡赫汽车用品旗舰店")
                # 省份
                if s_result is None:
                    f.append("其他地区")
                else:
                    f.append(s_result)
            all_data.append(f)
        return all_data


    def handler_fensi(self,from_data,create_time=time.strftime('%Y-%m-%d %H:%M:%S')):
        """
            昵称	UID	简介	SECUID	抖音号	精准	蓝V认证	粉丝数 创建时间 from
            粉丝关注列表数据处理
            :return: [[],[]]
        """
        all_data = []
        for i in self._data:
            i[4] = "https://www.douyin.com/user/" + i[4]
            i.pop(0)
            i.append(create_time)
            i.append(from_data)
            all_data.append(i)
        return all_data

    def handle_pinlun(self):
        ['1', 'https://www.douyin.com/channel/300203?modal_id=7453068664078650660', '2024-12-27 23:33:55',
         '家美扫天下（郴州）', '这样洗能洗干净吗？', '4073058105819598', '42279691464', '男', '湖南',
         '.我是一个拿扫把扫地的家政人\n??分享酒店大型油烟系统清洗技术\n??分享酒店集中空调体系清洗技术\n?分享酒店大型水晶灯免拆洗技术\n????创业十年从一个小白到行业导师\n????经历了人生的酸甜苦辣精辟独到\n????能解决各种难题各种清洗技术拓客思维',
         '69', '43', '',
         'https://p26.douyinpic.com/aweme/100x100/aweme-avatar/tos-cn-i-0813c001_ogoCA9FbDqOleAAIEncK9iVngD4ACWAcVf6JIA.jpeg?from=3067671334',
         'MS4wLjABAAAA_boATy3tzd89bbfKSE282OHjsGbLoa5V6_3m-8yO4eWvSXnDYaqp9A_OVU9aEPxm']
        temp = ''
        for i in self._data:
            i[14] = "https://www.douyin.com/user/"+i[14]
            print(i)




# 粉丝关注一条龙
def fensi(file_dir="test_data/1228家美扫天下粉丝关注数据.xlsx",form_user='test'):
    e = Read(excel_path=file_dir)
    d = e.get_all_data()

    h = DataHandle(d)
    rs_d = h.handler_fensi(from_data=form_user)

    i = Insert(insert_data=(rs_d))
    i.insert_dy_fensi_data()
    del  i
    s = Select(sql_code=GET_FENSI_ALL_DATA)
    s_d = s.get_all_data()
    w = Write(excel_file_name=f"source/张伦/result/{form_user}粉丝关注列表数据{time.strftime('%m-%d')}.xlsx",filed=FILED_FenSi,data=s_d)
    w.write_fensi_data()
    pass




# 抖音直播一条龙
def dy_live(file_dir="test_excel_dir"):
    read_data = Read(file_dir)
    dh = DataHandle(origin_data=read_data.get_all_data())
    i=Insert(insert_data=dh.handle_zhibo())
    i.insert_dy_live_data()
    del i

    s = Select(sql_code=GET_ZhiBo_ALL_DATA)
    clean_data = s.get_all_data()
    w = Write(excel_file_name=os.path.join("source/ly直播采集/result",f'{time.strftime("%Y-%m-%d")}直播采集.xlsx'), filed=FILED_ZhiBo, data=clean_data)
    w.write_table_all_data()



if __name__ == '__main__':
    start = time.time()
    # dy_live(file_dir="source/ly直播采集/temp")
    # fensi(file_dir='source/张伦/粉丝关注采集',form_user='张伦')
    r = Read('test_data/评论区采集.xlsx')
    data = r.get_all_data()
    h = DataHandle(origin_data=data)
    h.handle_pinlun()
    print(time.time()-start)