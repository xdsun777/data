from json import JSONDecodeError
import json, os

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


def init_config(config=init_config):
    with open('./fans.json', 'w', encoding='utf-8') as f:
        f.write(config)


def get_urls(file='./url.txt'):
    try:
        with open(file, 'r', encoding='utf-8') as f:
            return [i.strip('\n') for i in f.readlines()]
    except:
        return False


def get_config(file='./fans.json'):
    if os.path.isfile(file):
        with open(file, 'r', encoding='utf-8') as f:
            info = f.read()
        try:
            return json.loads(info)
        except JSONDecodeError as e:
            raise e
    else:
        return False


# 数据抓取

    url_is_exist = os.path.isfile('./url.txt')
    fans_is_exist = os.path.isfile('./fans.json')
    output_is_exit = os.path.isdir('./output')
def main():
    # 运行条件： url.txt    fans.json     key.txt
    # 优先运行fans.json,随后运行url.txt,key.txt用于过滤筛选数据
    if os.path.isfile('fans.json'):



if __name__ == '__main__':
    pass
