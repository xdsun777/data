import os
import requests
import sys
import time
import xlwings as xw

from temp_data import city_data


# TODO visible=False

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
        sht.activate
        a_data += sht.range('a1').expand('table').value
        wb.save()
        wb.close()
    app.quit()
    return a_data


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
        sht.range(insert_site).options(expand='down').value = i
        head = ["序号", "主播昵称", "时间", "用户昵称", "动作", "内容", "Uid", "抖音号", "性别", "地区", "简介", "等级",
                "粉丝", "关注", "精准", "Secid", "qurl", "私密", "蓝V", "作品链接"]
        sht.range('A1').options(expand='right').value = head
    result_wb.save(time.strftime("%y-%m-%d.%H-%M-%S") + '.xlsx')
    result_wb.close()
    result_app.quit()


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


# TODO
#  1.根据表头筛选以进行操作
#  2.数据类型转换
#  3.数据去重、分类
#

def data_handle(origin_data):
    # 返回一个 列表
    # 中间数据
    result_data = []
    # TODO 返回的数据应是[[],[],[]]
    qx_sort = []
    # 一个存储数据的临时列表
    temp_data = []
    # 循环二维数组数据 方便处理
    for (i, t) in enumerate(origin_data):
        # 检测uuid是否在临时数组中，不在就进入判断
        if t[6] not in temp_data:
            # 设置id 根据临时数组递增
            t[0] = len(temp_data)
            # 将uuid加入临时数组
            temp_data.append(t[6])
            # 去掉表头
            if i != 0:
                # 查询手机号归属地，并设置
                if t[9] is None and t[14] is not None:
                    t[9] = get_place(t[14])
                    print(t[9])
            result_data.append(t)

    # 遍历二维数组，将 信息 作区分 ， 增加省份 字段
    for w in result_data:
        s_result = qx_to_s(w[9])
        if s_result is None:
            w.append("其他地区")
        else:
            w.append(s_result)
        qx_sort.append(w)
    # print(qx_sort)
    return qx_sort


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
        clean_data = data_handle(all_data)
        saveResult(clean_data)
        # print(clean_data)
