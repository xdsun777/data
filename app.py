import json
import os

import excel
from data_handle import *
from excel import *
from sql import *
import time


# 粉丝关注一条龙
def fensi(input_file="/*test_excel_dir*/", form_user='test'):
    FENSI = '''
    SELECT 昵称,UID,简介,sec_uid,抖音号,精准,蓝V认证,粉丝数,创建时间 FROM "main"."fensi" WHERE "时间" LIKE '%2025-01-11%' ESCAPE '\\' ORDER BY "创建时间";
    '''
    e = Read(excel_path=input_file)
    d = e.get_all_data()

    h = DataHandle(d)
    rs_d = h.handler_fensi(from_data=form_user)

    i = Insert(insert_data=rs_d)
    i.insert_dy_fensi_data()
    del  i
    # FENSI = '''
    # SELECT 昵称,UID,简介,sec_uid,抖音号,精准,蓝V认证,粉丝数,创建时间 FROM "main"."fensi" GROUP BY "UID";
    # '''
    # s = Select(sql_code=FENSI)
    # s_d = s.get_all_data()
    # w = Write(excel_file_name=f"{time.strftime('%m-%d')}.{form_user}粉丝关注列表采集.xlsx", filed=FILED_FenSi, data=s_d)
    # w.write_fensi_data()


# 抖音直播一条龙
# noinspection PyUnusedLocal

def dy_live(input_files="/*test_excel_dir*/", out_file=f'{time.strftime("%Y-%m-%d")}直播采集.xlsx'):
    # ttime = time.strftime("%Y-%m-%d")
    ttime = '2025-01-15'  # SELECT "_rowid_",* FROM  "main"."zhibo2" WHERE "时间" REGEXP '2024-12-2[01234]' GROUP BY "Uid" ORDER BY "主播昵称";
    ZHIBO = f'SELECT id,主播昵称,用户昵称,勋章等级,动作,抖音号,sec_uid,uid,简介,粉丝,关注,性别,地区,精准,时间,创建时间,省份 FROM "main"."zhibo" WHERE "时间" REGEXP \'2025-01-1[6]\' GROUP BY "uid" ORDER BY "省份";'

    '''sql:自由组合'''
    # read_data = Read(input_files)
    # dh = DataHandle(origin_data=read_data.get_all_data())
    # i=Insert(insert_data=dh.handle_zhibo())
    # i.insert_dy_live_data()
    # del i
    s = Select(sql_code=ZHIBO)
    data = s.get_all_data()
    w = Write(excel_file_name=out_file, filed=FILED_ZhiBo, data=data)
    w.write_table_all_data()


def pinglun(input_files="/*test_excel_dir*/", out_file=f'{time.strftime("%Y-%m-%d")}评论.xlsx', form='张伦'):
    PINGLUN = f"""
    SELECT 	视频链接,时间,昵称,评论内容,uid,抖音号,性别,简介,粉丝,关注,精准,头像,sec_uid,创建时间,地区 FROM "main"."pinglun" WHERE "form" LIKE '%{form}%' ESCAPE '\\' AND "创建时间" LIKE '%{time.strftime("%Y-%m-%d")}%' ESCAPE '\\' ORDER BY "精准";
    """

    # read_data = Read(input_files)
    # dh = DataHandle(origin_data=read_data.get_all_data())
    # i=Insert(insert_data=dh.handle_pinglun())
    # i.insert_dy_pinglun_data(form=form)
    # del i
    s = Select(sql_code=PINGLUN)
    data = s.get_all_data()
    w = Write(excel_file_name=f'{form}.{out_file}', filed=FILED_PINGLUN, data=data)
    w.write_fensi_data()


def fans_insert_sql():
    txt_list = [os.path.join('fans_infobak', i) for i in os.listdir('fans_infobak') if '.txt' in i]
    now_time = time.strftime("%Y-%m-%d")
    for i in txt_list:
        if os.path.isfile(i):
            with open(i, 'r') as f:
                for x in f.readlines():
                    x = json.loads(x)
                    data = [x['nickname'], x['uid'], x['signature'], x['sec_uid'], x['unique_id'], '',
                            x['is_biz_account'], x['follower_count'], now_time, 'test']
                    # 昵称, UID, 简介, sec_uid, 抖音号, 精准, 蓝V认证, 粉丝数, 创建时间, form
                    ins = Insert(insert_data=data)
                    ins.insert_dy_fensi_data()
                    # del ins


def fans_export_excel():
    sq = """SELECT 昵称,简介,UID,sec_uid,抖音号,精准,蓝v认证,粉丝数 FROM "main"."fensi" GROUP BY "UID"
    """
    s = Select(sql_code=sq)
    data = s.get_all_data()
    print(len(data))
    clean_data = []
    words = ['清', '洗', '什','么', '油', '烟', '多', '少', '价', '米', '地','址','位', '置', '汽', '美', '车', '洁', '膜', '修',
             '车', '高','压', '清','厨', '管', '道', '机', '结']
    for i in data:
        d = str(i[0]) + str(i[1]) + str(i[2])
        for a in words:
            if a in d:
                clean_data.append(i)
                break

    print(len(clean_data))
    for i in range(0,5):

        d = clean_data[len(clean_data)//5*i:len(clean_data)//5*i+len(clean_data)//5]

        ex = excel.Write(excel_file_name=f'{str(i)}.xlsx',filed=['昵称','简介','UID','sec_uid','抖音号','精准','蓝v认证','粉丝数'],data=d)
        ex.write_fensi_data()

if __name__ == '__main__':
    start = time.time()
    # fans_export_excel()
    # dy_live(input_files=r'C:\Users\ly\Desktop\work\source\ly直播采集\20250117直播间采集结果.xlsx', out_file='20250116直播数据.xlsx')
    fensi(input_file='C:\\Users\\ly\\Desktop\\work\\source\\张伦\\粉丝关注采集', form_user='张伦')
    # pinglun(input_files="C:\\Users\\ly\\Desktop\\work\\source\\张伦\\视频评论采集\\20250114下陆区绿一源环保清洗经营部评论采集结果.xlsx",form='张伦')

    print("执行时间：", time.time() - start)
