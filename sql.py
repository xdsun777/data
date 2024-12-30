import sqlite3,re

class Sql:
    def __init__(self,db_name='C:\\Users\ly\Desktop\data\_data\douyin.db'):
        def _regexp(expr, item):
            reg = re.compile(expr)
            return reg.search(item) is not None

        self.con = sqlite3.connect(db_name)
        self.con.create_function('REGEXP', 2, _regexp)
        self.cursor = self.con.cursor()


    def __del__(self):
        print("被雄安回来")


s = Sql()
del s