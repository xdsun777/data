import excel,sql,time
start = time.time()
def test_dy_live():
    """
        抖音直播间数据测试
    """
    e = excel.Read('./test_data/直播间采集.xlsx')
    print(e.get_all_data())
    a = [('117(10002)', '我还是我', '4', '进入直播间', '1039182390.',
          'MS4wLjABAAAAIxFkAHLiRiCKvHyo4Kn0jZqeDJMQxTcUbNCuJr2-m8E', '51999910902', '我就是我', '121', '44', '男',
          '贺州',
          '', '2024-12-28 17:24:30', "test", "test", "test")]

    # i = sql.Insert(insert_data=a)
    # i.insert_dy_live_data()
    # del i

def test_fensi():
    """
        粉丝数据测试
    """
    e = excel.Read('test_data/1228家美扫天下粉丝关注数据.xlsx')
    print(e.get_all_sheet())


test_fensi()











print(time.time()-start)