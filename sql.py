import os.path
import sqlite3, re,time
from datetime import datetime

from soupsieve import select

GET_ZhiBo_ALL_DATA = """SELECT id,主播昵称,时间, 用户昵称,  简介,精准,  动作,uid,sec_uid, 抖音号, 性别, 地区,勋章等级,粉丝, 关注, 创建时间,省份 FROM "main"."zhibo"  GROUP BY "uid";
"""
"""sql语句:获取直播所有数据"""
GET_ZhiBo_NOW_DATA = f"SELECT '_rowid_',* FROM 'main'.'zhibo' WHERE '时间' REGEXP '{time.strftime('%Y-%m-%d')}' GROUP BY 'uid' ORDER BY '主播昵称';"
"""sql语句:获取直播当天数据"""
GET_FENSI_ALL_DATA = """
SELECT 昵称,UID,简介,sec_uid,抖音号,精准,蓝V认证,粉丝数,创建时间,form FROM "main"."fensi" GROUP BY "UID"
"""
"""sql语句:获取粉丝关注所有数据"""
GET_FENSI_NOW_DATA = """
SELECT 昵称,UID,简介,sec_uid,抖音号,精准,蓝V认证,粉丝数,创建时间,form FROM "main"."fensi" WHERE '时间' REGEXP '{time.strftime('%Y-%m-%d')}'  GROUP BY "UID"
"""
"""sql语句:获取粉丝关注所有数据"""



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

class HandleTool(Sql):
    def __init__(self,db_name='./_data/douyin.db',table_name=None):
        if not os.path.isfile(db_name) or table_name is None:
            exit(-1)
        self._db_name = db_name
        self._table_name = table_name
        super().__init__(db_name=self._db_name)

    def time_to_convert(self):
        cha_code = f'SELECT id,创建时间 FROM "main"."{self._table_name}"  ORDER BY "uid";'
        s = Select(db_name=self._db_name,sql_code=cha_code)
        s_d = s.get_all_data()
        print(s_d[0])
        if "-" in str(s_d[0][1]) and ":" in str(s_d[0][1]) or type((s_d[0][0])) is not int:
            print("不符合规范")
            exit(-1)
        for i in s_d:
            change_time = datetime.fromtimestamp(float(i[1])).strftime('%Y-%m-%d %H:%M:%S')
            update = f'UPDATE "main"."{self._table_name}" SET 创建时间 = "{change_time}" WHERE id = "{int(i[0])}";'
            print(update)
            self._cursor.execute(update)


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
            self._data = insert_data
        else:
            self._data = None

    def insert_dy_live_data(self):
        for i in self._data:
            if type(i) == list:
                self._cursor.execute(
                    "INSERT INTO zhibo (编号,用户昵称,勋章等级,动作,抖音号,sec_uid,uid,简介,粉丝,关注,性别,地区,精准,时间,创建时间,主播昵称,省份) VALUES (?, ?, ?,?, ?, ?,?, ?, ?,?, ?, ?,?, ?, ?,?, ?)",
                    (i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12], i[13], i[14],
                     i[15], i[16]))

    def insert_dy_fensi_data(self):
        for i in self._data:
            if type(i) == list:
                self._cursor.execute(
                    "INSERT INTO fensi (昵称,UID,简介,sec_uid,抖音号,精准,蓝V认证,粉丝数,创建时间,form) VALUES (?,?,?,?,?,?,?,?,?,?)",
                    (i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9],)
                )



def changer_time():
    ht = HandleTool(table_name="zhibo")
    ht.time_to_convert()
    del ht

    ht = HandleTool(table_name="zhibo2")
    ht.time_to_convert()
    del ht

    ht = HandleTool(table_name="fensi")
    ht.time_to_convert()
    del ht


if __name__ == '__main__':
    # print(GET_ZhiBo_NOW_DATA)
    # s = Select(sql_code=GET_ZhiBo_NOW_DATA)
    # print(s.get_all_data())
    start = time.time()
    changer_time()

    print(time.time() - start)

    pass
