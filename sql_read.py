import sqlite3,sys,time,os,re
import xlwings as xw

# 根据uid查询，去重
sql__all = """
SELECT * FROM "main"."zhibo2"  GROUP BY "Uid";
"""
# 指定日期查询
sql__date = """
SELECT "_rowid_",* FROM "main"."zhibo2" WHERE "时间" REGEXP '2024-12-1[6789]' GROUP BY "Uid"
UNION
SELECT "_rowid_",* FROM "main"."zhibo2" WHERE "时间" REGEXP '2024-12-2[01234]' GROUP BY "Uid" ORDER BY "主播昵称";
"""

def regexp(expr, item):
    reg = re.compile(expr)
    return reg.search(item) is not None




def read_sql(db_name='C:\\Users\\ly\\Desktop\\pro\\data_\\douyin.db',sql_ = sql__all):
    conn = sqlite3.connect(db_name)
    conn.create_function('REGEXP',2,regexp)
    cursor = conn.cursor()
    all_d = cursor.execute(sql_)
    d = [list(i) for i in all_d]
    conn.commit()
    conn.close()
    return d


# 保存数据到excel
def saveResult(data):
    result_app = xw.App(visible=False, add_book=False)
    result_wb = result_app.books.add()

    # TODO 数据处理建表
    s_list = [x[-1] for x in data]
    s_set = set(s_list)
    sht_list = [result_wb.sheets.add(x) for x in s_set]
    list_set_dict = dict(zip(s_set, sht_list))
    for i in data:
        sht = list_set_dict[i[-1]]
        sht_info = sht.used_range
        insert_site = "A" + str(sht_info.last_cell.row + 1)
        print(insert_site)
        i.pop(0)
        sht.range(insert_site).options(expand='down').value = i
        head = ["序号", "主播昵称", "时间", "用户昵称", "动作", "内容", "Uid", "抖音号", "性别", "地区", "简介", "等级",
                "粉丝", "关注", "精准", "Secid", "qurl", "私密", "蓝V", "作品链接", "创建时间","省份"]
        sht.range('A1').options(expand='right').value = head

    result_wb.save(time.strftime("%y-%m-%d.%H-%M-%S") + '.xlsx')
    result_wb.close()
    result_app.quit()

saveResult(read_sql())
