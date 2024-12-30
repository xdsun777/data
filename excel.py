from openpyxl import Workbook, load_workbook
# import itertools
import os.path
import time

FILED_ZhiBo =['id','主播昵称','时间', '用户昵称',  '简介','精准',  '动作','uid','sec_uid', '抖音号', '性别', '地区','勋章等级','粉丝', '关注', '创建时间','省份']

class Read:
	def __init__(self, excel_path: str):
		self.excel_file_path = ''
		self.excel_files_dir_path = ''
		self.excel_files_path_list = []
		self.wb = None

		if os.path.isdir(excel_path):
			self.excel_files_dir_path = excel_path
			self.excel_files_path_list = [f for f in os.listdir(excel_path) if f.endswith('.xlsx') and f[0] != '.']
		else:
			if excel_path.endswith('xlsx'):
				self.excel_file_path = excel_path
				self.wb = load_workbook(self.excel_file_path)

	def get_all_sheet(self) -> list:
		return self.wb.sheetnames

	def get_all_data(self) -> list[list]:
		if self.wb is not None:
			sheet = self.wb.active
			temp = [list(row) for row in sheet.iter_rows(values_only=True)]
			temp.pop(0)
			return temp
		else:
			return self.get_multi_file_all_data()

	def get_multi_file_all_data(self) -> list[list]:
		all_data: list = []
		for f in self.excel_files_path_list:
			f = os.path.join(os.path.join(self.excel_files_dir_path, f))
			self.wb = load_workbook(f)
			all_data += self.get_all_data()
		# return list(itertools.chain.from_iterable(all_data))
		return all_data

class Write:
	def __init__(self, excel_file_name:str=None, filed:list=None,data:list=None):
		if type(data) is list:
			self.data = data
			# print(self.data)
		else:
			print("无效数据")
			exit(-1)

		if type(filed) is list or type(filed) is tuple:
			self.filed = filed
		else:
			print("无效字段")
			exit(-1)

		if excel_file_name is None:
			self.save_file_name = time.strftime("%y-%m-%d.%H-%M-%S") + '.xlsx'
		else:
			self.save_file_name = excel_file_name

		self.wb = Workbook()
		self.sheet = self.wb.active


	def write_table_all_data(self):
		self.sheet.append(self.filed)
		for data_list in self.data:
			self.sheet.append(data_list)
		self.wb.save(self.save_file_name)


if __name__ == '__main__':
	# from sql import Sql, GET_ZhiBo_ALL_DATA, Select
	# 读和写都 需要 传入或传出 双层list
	e = Read('test_data/直播间采集.xlsx')
	# e = Read('test_data')
	s_d = e.get_all_data()
	# print(s_d)
	w = Write(filed=FILED_ZhiBo,data=s_d)
	w.write_table_all_data()