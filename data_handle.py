from time import sleep


class DataHandle:
	def __init__(self,origin_data):
		if type(origin_data) is list:
			self._data = origin_data
		self._final_data = None
		self._temp_data = None

	def remove_head(self):
		for table in self._data:
			table.pop(0)
			for tuple_data in table:
				print(tuple_data)

	def final_data(self):
		d = self._data
		return d

import excel
read_data = excel.Read("./test_data")
data = read_data.get_all_data()
d = DataHandle(origin_data=data)
d.remove_head()
