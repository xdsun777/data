from sql import *
code="""

"""
# s = Select(sql_code=code)


from datetime import datetime, timedelta

# 设定起始日期
start_date = datetime(2023, 1, 1)
# 设定结束日期
end_date = datetime(2023, 1, 10)

# 生成日期序列
dates = [start_date + timedelta(days=i) for i in range(0, (end_date - start_date).days + 1)]

# 打印日期序列
for date in dates:
    print(date.strftime('%Y-%m-%d'))