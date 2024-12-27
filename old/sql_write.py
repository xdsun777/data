import sqlite3,sys,os,time
import xlwings as xw
from temp_data import city_data
# 主播昵称	时间	用户昵称	动作	内容	Uid	抖音号	性别	地区	简介	等级	粉丝	关注	精准	Secid	qurl	私密	蓝V	作品链接 创建时间 省份

data = ['488', '猎鹰蒸汽喷抽清洗机厂家', '2024-12-20 11:30:30', '腾达名车维修服务@', '进房', None,
        '3747569272369885', 'tengdamingch', '-', '新乡', '汽车维修@关于车上面 的事儿请过来咨询了解。', '12', '167',
        '1107', None,
        'https://www.douyin.com/user/MS4wLjABAAAAX8vQV0eU_USQJIFtNNmaWR1E9Iw-LgIA6gBLvDYcFf7ihWfc7XWLTNN4bVHhLINy',
        'https://p11.douyinpic.com/aweme/100x100/aweme-avatar/tos-cn-avt-0015_a4b39520870beb238b6c103a0cc5f6b5.jpeg?from=3067671334',
        '×', None, None]

# 市县区 转 省
def qx_to_s(qx):
    for s in city_data:
        if qx is not None and type(qx) != 'NoneType':
            h = qx + "市"
            x = qx + "县"
            z = qx + "镇"
            if qx in city_data[s] or h in city_data[s] or x in city_data[s] or z in city_data[s]:
                return s
    # print("未找到该地区所在省份")
    return None


def write_sql(zhubonicheng,shijian,yonghunicheng,dongzuo,neirong,uid,douyinhao,xingbie,diqu,jianjie,dengji,fensi,guanzhu,jingzhun,sercid,qurl,simi,lanv,zuopinglianjie,creattime,shengfen,db_name='D:\data\douyin.db'):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO zhibo2 (主播昵称,时间, 用户昵称, 动作, 内容, Uid, 抖音号, 性别, 地区, 简介, 等级, 粉丝, 关注, 精准, Secid, qurl, 私密, 蓝V, 作品链接, 创建时间, 省份) VALUES (?, ?, ?,?, ?, ?,?, ?, ?,?, ?, ?,?, ?, ?,?, ?, ?,?, ?, ?)", (zhubonicheng,shijian,yonghunicheng,dongzuo,neirong,uid,douyinhao,xingbie,diqu,jianjie,dengji,fensi,guanzhu,jingzhun,sercid,qurl,simi,lanv,zuopinglianjie,creattime,shengfen))
    conn.commit()
    conn.close()

def all_data_write_sql(all_data):
    for (i,data) in enumerate(all_data):
        try:
            write_sql(data[1], str(data[2]), data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10],data[11], data[12], data[13], data[14], data[15], data[16], data[17], data[18], data[19], time.time(),qx_to_s(data[9]))
            print("已写入：",i)
        except:
            print(data)


# 读取excel文件的数据
# noinspection PyStatementEffect
def get_data(file_list: list):
    app = xw.App(visible=False, add_book=False)
    app.display_alerts = False
    app.screen_updating = False
    a_data = []
    for f in file_list:
        wb = app.books.open(f)
        wb.activate()
        sht = wb.sheets(1)
        # noinspection PyStatementEffect
        sht.activate

        if not f[4] or type(f[4]) == 'NoneType':
            f[4] = "未知名称"

        a_data += sht.range('A2').expand('table').value
        wb.save()
        wb.close()
    app.quit()
    return a_data




if __name__ == '__main__':
    arg = sys.argv

    if len(arg) == 2:
        # 传入需要处理的excel文件所在目录，进行批量处理
        file_path = []
        if os.path.isdir(arg[1]):
            data_file_path = arg[1]
            file = [os.path.join(data_file_path, file_path) for file_path in os.listdir(data_file_path)]
            for (i, t) in enumerate(file):
                if t.endswith('.xlsx'):
                    file_path.append(t)
        else:
            exit(0)

        all_data = get_data(file_path)
        # print(all_data)
        all_data_write_sql(all_data)



