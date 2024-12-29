from openpyxl import Workbook, load_workbook
import os.path
import time



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
			return [[row for row in sheet.iter_rows(values_only=True)]]
		else:
			return self.get_multi_file_all_data()

	def get_multi_file_all_data(self) -> list[list]:
		all_data: list = []
		for f in self.excel_files_path_list:
			f = os.path.join(os.path.join(self.excel_files_dir_path, f))
			self.wb = load_workbook(f)
			all_data +=self.get_all_data()
		return all_data


class Write:
	def __init__(self, excel_file_name=None, filed=None,data=None):
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


	def table_head_handle(self):
		pass

	def write_table_all_data(self):
		for data_list in self.data:
			for i in data_list:
				self.sheet.append(i)

		self.wb.save(self.save_file_name)
		pass


if __name__ == '__main__':

	# e = Read('test_data/1228家美扫天下粉丝关注数据.xlsx')
	e = Read('test_data')
	s_d = e.get_all_data()
	# print(s_d)
	a = Write(excel_file_name="test.xlsx",data=s_d,filed=('编号', '昵称', 'UID', '简介', 'SECUID', '抖音号', '精准', '蓝V认证', '粉丝数'))
	a.write_table_all_data()