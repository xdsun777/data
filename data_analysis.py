from matplotlib.font_manager import FontProperties
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import time
from sql import *

font = FontProperties(fname="./wqy-zenhei.ttc", size=14)
plt.rcParams.update({
    'axes.unicode_minus': False,
    'font.size': 20
})


def get_all_data():
    datas = {}
    # 设定起始日期
    start_date = datetime(2024, 11, 25)
    # 设定结束日期
    end_date = datetime.now()
    # 生成日期序列
    dates = [start_date + timedelta(days=i) for i in range(0, (end_date - start_date).days + 1)]
    # 打印日期序列
    for d in dates:
        de = d.strftime('%Y-%m-%d')
        zhibo = f'SELECT id,主播昵称,用户昵称,勋章等级,动作,抖音号,sec_uid,uid,简介,粉丝,关注,性别,地区,精准,时间,创建时间,省份 FROM "main"."zhibo" WHERE "时间" LIKE "%{de}%" ESCAPE "\\" AND "主播昵称" LIKE "%猎鹰蒸汽喷抽清洗机厂家%" ESCAPE "\\" GROUP BY "uid" ORDER BY "省份";'
        s = Select(sql_code=zhibo)
        datas[de[5:]] = s.get_all_data()
    return datas


# 每日新增观看人数
def get_growth_data(d):
    growth_data = {}
    old_data = {}
    temp = []
    for i in d:
        d_temp = []
        oldd_temp = []
        if d[i]:
            for x in d[i]:
                if x[7] not in temp:
                    temp.append(x[7])
                    d_temp.append(x)
                else:
                    oldd_temp.append(x)
        old_data[i] = oldd_temp
        growth_data[i] = d_temp
    return [growth_data, old_data]


# 0 438 742 0 798 207 0 576 190 218 0 14 0


def zhexian():
    # 获取数据
    g1 = get_all_data()
    b = get_growth_data(g1)
    x1 = g1.keys()
    y1 = [len(g1[i]) for i in g1]
    x2 = b[0].keys()
    y2 = [len(b[0][i]) for i in b[0]]
    x3 = b[1].keys()
    y3 = [len(b[1][i]) for i in b[1]]

    # 创建画布
    plt.figure("All and growth", figsize=(100, 100), dpi=100)
    plt.grid(True, linestyle='--', alpha=0.5)  # alpha表示透明度，0最浅
    plt.xlabel("日期", fontproperties=font)
    plt.ylabel("人数", fontproperties=font)
    plt.title("每日观看直播人数统计图", fontproperties=font)

    # 绘制图像
    plt.plot(x1, y1, color='g', linestyle=':', label='Total')
    plt.plot(x2, y2, color='r', linestyle="-.", label="Growth")

    for i, t in enumerate(g1):
        plt.text(t, len(g1[t]), '%d' % len(g1[t]), ha='center', va='bottom', color='g')
    for i, t in enumerate(b[0]):
        plt.text(t, len(b[0][t]), '%d' % len(b[0][t]), ha='center', va='bottom', color='r')
    plt.legend(loc='best')
    plt.savefig("allGrowth.png")

    plt.figure("老客户", figsize=(100, 100))
    plt.bar(x3, y3, label="Old")
    for i, t in enumerate(b[1]):
        plt.text(t, len(b[1][t]), '%d' % len(b[1][t]), ha='center', va='bottom', color='b')

    plt.legend(loc='best')
    # 显示图像
    plt.savefig('old.png')
    # plt.show()


if __name__ == '__main__':
    start = time.time()
    zhexian()

    print(time.time() - start)
