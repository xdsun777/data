import sqlite3, re

GET_ZhiBo_ALL_DATA = """
SELECT id,主播昵称,时间, 用户昵称,  简介,精准,  动作,uid,sec_uid, 抖音号, 性别, 地区,勋章等级,粉丝, 关注, 创建时间,省份 FROM "main"."zhibo"  GROUP BY "uid";
"""


class Sql:
	def __init__(self, db_name='./_data/douyin.db'):
		def _regexp(expr, item):
			reg = re.compile(expr)
			return reg.search(item) is not None

		self._con = sqlite3.connect(db_name)
		self._con.create_function('REGEXP', 2, _regexp)
		self._cursor = self._con.cursor()

	def __del__(self):
		self._con.commit()
		self._con.close()


class Select(Sql):
	def __init__(self, db_name='./_data/douyin.db', sql_code=None):
		super().__init__(db_name=db_name)
		if sql_code:
			self.code_code = sql_code
		else:
			print("必须传入sql语句")
			exit(-1)

	def get_all_data(self):
		return [list(i) for i in self._cursor.execute(self.code_code)]


class Insert(Sql):
	def __init__(self, db_name='./_data/douyin.db', insert_data=None):
		super().__init__(db_name=db_name)
		if insert_data:
			self.data = insert_data
		else:
			self.data = None

	def insert_dy_live_data(self):
		for i in self.data:
			if type(i) == list:
				self._cursor.execute(
					"INSERT INTO zhibo (编号,用户昵称,勋章等级,动作,抖音号,sec_uid,uid,简介,粉丝,关注,性别,地区,精准,时间,创建时间,主播昵称,省份) VALUES (?, ?, ?,?, ?, ?,?, ?, ?,?, ?, ?,?, ?, ?,?, ?)",
					(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12], i[13], i[14],
					 i[15], i[16]))


if __name__ == '__main__':
	# s = Select(sql_code=GET_ZHIBO_ALL_DATA)
	# print(s.get_all_data())
	pass
