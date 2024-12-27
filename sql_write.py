import sqlite3, sys, os, time,requests
from typing import Any

import xlwings as xw
from temp_data import city_data

'''编号	用户昵称	勋章等级	动作	抖音号	sec_uid	uid	简介	粉丝	关注	性别	地区	精准	时间 省份 创建时间 主播昵称'''

data = ['1(10002)', '猎鹰蒸汽喷抽清洗机厂家市场部岳星', '0', '进入直播间', '75568354875',
        'MS4wLjABAAAAmfMkOm-Fz5O7Dga8Ty2F-o', '655758904793323',
        '家政、汽车精洗综合解决方案服务商，专注于以物理方法解决表面深度清洁问题，纯蒸汽高温高压清洁远离化学污染，有效杀菌除螨除异味，完整的服务流程和配套产品助您打造 属于您的特色服务项目！清洁热线18942955144【微信同号】',
        '875', '1996', '女', '武汉', ',18942955144', '2024-12-27 10:41:50']

# 获取手机号归属地
def get_place(phone):
    url = 'https://cx.shouji.360.cn/phonearea.php?number=18942955144' + phone
    rs = requests.get(url)
    d = rs.json().get('data')
    try:
        # return 市
        return d.get('city')
    except AttributeError:
        print("data没有city属性，返回空")
        return None

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


def write_sql(zhubonicheng, shijian, yonghunicheng, dongzuo, neirong, uid, douyinhao, xingbie, diqu, jianjie, dengji,
              fensi, guanzhu, jingzhun, sercid, qurl, simi,
              db_name='C:\\Users\ly\Desktop\data\_data\douyin.db'):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO zhibo (编号,用户昵称,勋章等级,动作,抖音号,sec_uid,uid,简介,粉丝,关注,性别,地区,精准,时间,省份,创建时间,主播昵称) VALUES (?, ?, ?,?, ?, ?,?, ?, ?,?, ?, ?,?, ?, ?,?, ?)",
        (zhubonicheng, shijian, yonghunicheng, dongzuo, neirong, uid, douyinhao, xingbie, diqu, jianjie, dengji, fensi,
         guanzhu, jingzhun, sercid, qurl, simi))
    conn.commit()
    conn.close()

['49(10002)', '乡下人', '13', '进入直播间', 'dyuee7g85unk', 'MS4wLjABAAAAbjSn9djMtfnxZAhtDLlS1s6QI6xWvCzW2XKrytlYajw', '110956384596', None, '174', '644', '-', None, None, '2024-12-27 09:26:57', '其他地区', 1735282536.0272715, '猎鹰蒸汽喷抽清洗机厂家']
def all_data_write_sql(all_data):
    for (i, data) in enumerate(all_data):
        try:
            write_sql(data[0],data[1], str(data[2]), data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10],
                      data[11], data[12], data[13], data[14], data[15], data[16])
            print("已写入：", i)
        except:
            print(data,"写入失败")


# 读取excel文件的数据

def get_data(file_list: list):
    app = xw.App(visible=False, add_book=False)
    app.display_alerts = False
    app.screen_updating = False
    a_data = []
    for f in file_list:
        wb = app.books.open(f)
        wb.activate()
        sht = wb.sheets(1)
        a_data += sht.range('A2').expand('table').value
        wb.save()
        wb.close()
    app.quit()
    return a_data


# 数据处理
def data_handle(a_data):
    all_data: list[Any] = []
    #TODO 数据处理部分
    # 新增 省份 创建时间 主播昵称
    for f in a_data:
        # 过滤查询手机号归属地，并设置
        if f[12] is not None:
            if ',' in f[12]:
                f[12] = f[12].removeprefix(',')
            if f[11] is None:
                f[11] = get_place(f[12])
                print(f[11])
        s_result = qx_to_s(f[11])
        # 省份
        if s_result is None:
            f.append("其他地区")
        else:
            f.append(s_result)
        # 创建时间
        f.append(time.time())
        # 主播昵称
        if "10002" in f[0] or "10005" in f[0]:
            f.append("猎鹰蒸汽喷抽清洗机厂家")
        if "10008" in f[0]:
            f.append("陕西绿霸高压清洗机")
        if "10011" in f[0]:
            f.append("巴诺德清洗机")
        if "10014" in f[0]:
            f.append("黑猫精英高压商用洗车机")
        if "10017" in f[0]:
            f.append("奔启洗车机—工厂")
        if "10020" in f[0]:
            f.append("KARCHER卡赫汽车用品旗舰店")

        # 处理用户主页sec——uid
        f[5] = "https://www.douyin.com/user/"+f[5]


        all_data.append(f)
    return all_data


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

        a_data = get_data(file_path)
        al_data = data_handle(a_data)
        all_data_write_sql(al_data)
