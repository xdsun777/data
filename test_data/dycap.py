import os.path

# 数据处理




# 运行配置
init_config = '''{
    "homeUrl": "",
    "status": 0,
    "count": 0,
    "total": 0,
    "context": []
}
'''
def config_init():
       pass


# 数据抓取



if __name__ == '__main__':
    url_is_exist = os.path.isfile('./url.txt')
    fans_is_exist = os.path.isfile('./fans.json')
    output_is_exit = os.path.isdir('./output')
