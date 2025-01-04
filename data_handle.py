from temp_data import city_data
# noinspection PyUnresolvedReferences
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
        self.table_head_data = None

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
                f.append(self.create_time)

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


    def handler_fensi(self,from_data,create_time=None):
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



# 粉丝关注一条龙
def fensi(input_file="/*test_excel_dir*/",form_user='test'):
    e = Read(excel_path=input_file)
    d = e.get_all_data()

    h = DataHandle(d)
    rs_d = h.handler_fensi(from_data=form_user)

    i = Insert(insert_data=rs_d)
    i.insert_dy_fensi_data()
    del  i
    s = Select(sql_code=GET_FENSI_ALL_DATA)
    s_d = s.get_all_data()
    w = Write(excel_file_name=f"{time.strftime('%m-%d')}.{form_user}粉丝关注列表采集.xlsx",filed=FILED_FenSi,data=s_d)
    w.write_fensi_data()




# 抖音直播一条龙
# noinspection PyUnusedLocal
def dy_live(input_files="/*test_excel_dir*/",out_file=f'{time.strftime("%Y-%m-%d")}直播采集.xlsx'):
    # read_data = Read(input_files)
    # dh = DataHandle(origin_data=read_data.get_all_data())
    # i=Insert(insert_data=dh.handle_zhibo())
    # i.insert_dy_live_data()
    # del i

    s = Select(sql_code=Free)
    data = s.get_all_data()
    w = Write(excel_file_name=out_file, filed=FILED_ZhiBo, data=data)
    w.write_table_all_data()


if __name__ == '__main__':
    start = time.time()
    # dy_live(input_files="C:\\Users\\ly\\Desktop\\work\\source\\ly直播采集\\0103直播间采集结果.xlsx")
    # fensi(input_file="C:\\Users\\ly\\Desktop\\work\\source\\张伦\\粉丝关注采集",form_user='张伦')
    print(time.time()-start)