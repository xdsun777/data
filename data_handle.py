from excel import FILED_ZhiBo
from sql import GET_ZhiBo_ALL_DATA
from temp_data import city_data
import requests,time
import excel,sql


class DataHandle:
	def __init__(self,origin_data):
		if type(origin_data) is list and type(origin_data[0]) is list:
			self._data = origin_data
		else:
			print("数据必须是二维list类型")
			exit(-1)
		self._final_data = None
		self._temp_data = None
		self.table_head_data = None

	# 获取手机号归属地
	def get_place(self,phone):
		url = 'https://cx.shouji.360.cn/phonearea.php?number=18942955144' + phone
		rs = requests.get(url)
		d = rs.json().get('data')
		try:
			# return 市
			return d.get('city')
		except AttributeError:
			print("data没有city属性，返回空")
			return None

	# 市县区 转 省
	def qx_to_s(self,qx):
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
		# 42(10002),修油缸气缸,7,进入直播间,2027451038,MS4wLjABAAAAlC5jq0Db2nz58qZdzVs1DHCDXK6 - bbIpf - RL5KPfZ7Q,98425843564,修油缸气缸18852041880,771,484,男 ,18852041880,2024 - 12 - 2814: 51:33
		# src 编号 用户昵称 勋章等级 动作 抖音号 sec_uid uid 简介 粉丝 关注 性别 地区 精准 时间
		# dct 编号 用户昵称 勋章等级 动作 抖音号 sec_uid uid 简介 粉丝 关注 性别 地区 精准 时间 创建时间 主播昵称 省份
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
				f.append(time.time())

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



# 抖音一条龙
def dy_live(file_dir="./test.xlsx"):
	read_data = excel.Read(file)
	dh = DataHandle(origin_data=read_data.get_all_data())
	i=sql.Insert(insert_data=dh.handle_zhibo())
	i.insert_dy_live_data()
	del i

	s = sql.Select(sql_code=GET_ZhiBo_ALL_DATA)
	clean_data = s.get_all_data()
	w = excel.Write(excel_file_name="test.xlsx", filed=FILED_ZhiBo, data=clean_data)
	w.write_table_all_data()


if __name__ == '__main__':
	start = time.time()
	dy_live(file_dir="C:\\Users\\ly\\Desktop\\work\\source\\ly直播采集")

	print(time.time()-start)