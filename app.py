from data_handle import *
from excel import *
from sql import *
import time


# 粉丝关注一条龙
def fensi(input_file="/*test_excel_dir*/",form_user='test'):
    FENSI = '''
    SELECT 昵称,UID,简介,sec_uid,抖音号,精准,蓝V认证,粉丝数,创建时间,form FROM "main"."fensi" WHERE "创建时间" LIKE '%2025-01-06%' ESCAPE '\\' ORDER BY "创建时间";
    '''
    # e = Read(excel_path=input_file)
    # d = e.get_all_data()
    #
    # h = DataHandle(d)
    # rs_d = h.handler_fensi(from_data=form_user)

    # i = Insert(insert_data=rs_d)
    # i.insert_dy_fensi_data()
    # del  i

    s = Select(sql_code=FENSI)
    s_d = s.get_all_data()
    w = Write(excel_file_name=f"{time.strftime('%m-%d')}.{form_user}粉丝关注列表采集.xlsx",filed=FILED_FenSi,data=s_d)
    w.write_fensi_data()


# 抖音直播一条龙
# noinspection PyUnusedLocal

def dy_live(input_files="/*test_excel_dir*/",out_file=f'{time.strftime("%Y-%m-%d")}直播采集.xlsx'):
    ZHIBO = f'SELECT id,主播昵称,用户昵称,勋章等级,动作,抖音号,sec_uid,uid,简介,粉丝,关注,性别,地区,精准,时间,创建时间,省份 FROM "main"."zhibo" WHERE "时间" LIKE "%2025-01-03%" ESCAPE "\\" GROUP BY "uid" ORDER BY "省份";'
    '''sql:自由组合'''
    read_data = Read(input_files)
    dh = DataHandle(origin_data=read_data.get_all_data())
    # i=Insert(insert_data=dh.handle_zhibo())
    # i.insert_dy_live_data()
    # del i
    s = Select(sql_code=ZHIBO)
    data = s.get_all_data()
    w = Write(excel_file_name=out_file, filed=FILED_ZhiBo, data=data)
    w.write_fensi_data()


def pinglun(input_files="/*test_excel_dir*/",out_file=f'{time.strftime("%Y-%m-%d")}评论.xlsx',form='test'):
    PINGLUN = f"""
    SELECT 	视频链接,时间,昵称,评论内容,uid,抖音号,性别,简介,粉丝,关注,精准,头像,sec_uid,创建时间,form,地区 FROM "main"."pinglun" WHERE "form" LIKE '%{form}%' ESCAPE '\\' ORDER BY "精准";
    """
    read_data = Read(input_files)
    dh = DataHandle(origin_data=read_data.get_all_data())
    i=Insert(insert_data=dh.handle_pinglun())
    i.insert_dy_pinglun_data(form=form)
    del i
    s = Select(sql_code=PINGLUN)
    data = s.get_all_data()
    w = Write(excel_file_name=f'{form}.{out_file}.xlsx', filed=FILED_PINGLUN, data=data)
    w.write_fensi_data()

if __name__ == '__main__':
    start = time.time()
    # dy_live(input_files='C:\\Users\\ly\\Desktop\\work\\source\\ly直播采集\\0104直播间采集结果.xlsx',out_file='20150104直播数据.xlsx')
    # fensi(input_file='C:\\Users\\ly\\Desktop\\work\\source\\张伦\\粉丝关注采集\\250104粉丝采集结果.xlsx', form_user='张伦')
    pinglun(input_files="C:\\Users\\ly\\Desktop\\work\\source\\丁羽欣\\视频评论采集",form='丁羽欣')

    print(time.time() - start)
    pass