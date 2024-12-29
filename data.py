

class DataHandle:
	def __init__(self,origin_data):
		self._data = origin_data
		pass

	def result_data(self):
		d = self._data
		return d


d = DataHandle("asd")
print(d.result_data())
