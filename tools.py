#TODO 工具类 负责清理数据
# 手机号归属地 phone2qs(phone)->{qxs、s}
# 区县市 转省份 qxs2s(qxs)-> s
# excel目录处理函数 get_excel_files(dir_path)->excel_files_list
from temp_data import city_data
import requests

class Tools:
    def __init__(self,data):
        self.data:[[]] = data
        self.return_data:[] = []
        self.city_data = city_data

    # 获取手机号归属地
    def get_phone_place(phone):
        url = 'https://cx.shouji.360.cn/phonearea.php?number=18942955144' + phone
        rs = requests.get(url)
        d = rs.json().get('data')
        try:
            # return 市
            print(rs.json())
            return d.get('city')
        except AttributeError:
            print("data没有city属性，返回空")
            return None


    def phone2qs(self, phone):
        qs = {"qxs": "", "s": ""}
        return qs


    def qxs2s(self, qxs):
        pass


    def get_excel_files(self, dir_path):
        excel_files_list = []
        return excel_files_list
