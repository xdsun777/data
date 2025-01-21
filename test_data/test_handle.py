from openpyxl import Workbook, load_workbook
import os


def get_file(dir='input'):
    if os.path.isdir(dir):
        return [os.path.join(dir, i) for i in os.listdir(dir) if i.endswith('.xlsx')]


def read(file) -> list:
    wb = load_workbook(file)
    sheet = wb.active
    return [list(row) for row in sheet.iter_rows(values_only=True)]


def write(data_i: list, filename: str = 'output/result.xlsx'):
    try:
        wb = Workbook()
        sht = wb.active
        for i in data_i:
            sht.append(i)
        wb.save(filename)
    except:
        print("写入错误")
        exit(0)

def filter_data(data_i:list)->bool:
    if os.path.isfile('key.txt'):
        with open('key.txt','r') as f:
            keys = f.readlines()
        s = ''.join(data_i)
        for i in keys:
            if i.strip('\n') in s:
                return True
        else:
            return False
    else:
        print('没有key.txt文件,不会筛选数据')
        return False


if __name__ == '__main__':
    if not os.path.isdir('output'):
        os.mkdir('output')
    for f in get_file('.'):
        outfile = os.path.join('output', f)
        data = read(f)
        total = len(data)
        title = data.pop(0)
        uid_count = None
        jingzhun_count = None
        secuid_count = None
        for i, t in enumerate(title):
            if t == "精准":
                jingzhun_count = i
            if t == 'uid' or t == 'UID':
                uid_count = i
            if t == 'sec_uid' or t == 'SECUID':
                secuid_count = i
        temp = []
        temp_data = [title]
        for u in data:
            if u[uid_count] not in temp:
                # 去重后的数据处理
                if jingzhun_count is not None and "," in u[jingzhun_count]:
                    u[jingzhun_count] = u[jingzhun_count].removeprefix(',')
                if secuid_count is not None and "http" not in u[secuid_count]:
                    u[secuid_count] = "https://www.douyin.com/user/" + u[secuid_count]

                 # 筛选数据
                if os.path.isfile('key.txt'):
                    if filter_data(u):
                        temp.append(uid_count)
                        temp_data.append(u)
                else:
                    temp.append(uid_count)
                    temp_data.append(u)

                        # 写入数据
        write(temp_data, outfile)

        # 数据清洗部分 u

        print(f"{outfile}去重完毕:{len(temp)}/{total}")
