# TODO 重构代码
import os.path
import xlwings as xw

# TODO get_excel_file_path_list
def get_excel_files_list(excel_file_dir_path="C:\\Users\ly\Desktop\work\handle"):
    if os.path.isdir(excel_file_dir_path):
        return [t for t in [os.path.join(excel_file_dir_path, excel_file_name) for excel_file_name in os.listdir(excel_file_dir_path)] if t.endswith('.xlsx')]
    else:
        print("excel file path is error:",excel_file_dir_path)
        exit(0)


# TODO excel读取函数
def read_excel(excel_file_path_list):
    all_data = []
    app = xw.App(visible=False, add_book=False)
    app.display_alerts = False
    app.screen_updating = False
    for f in excel_file_path_list:
        wb = app.books.open(f)
        wb.activate()
        sht = wb.sheets(1)
        all_data += sht.range('a2').expand('table').value
        wb.save()
        wb.close()
    app.quit()
    # print(all_data)
    return all_data


#TODO 数据处理函数
# 1. 抖音直播间
#   ["编号","用户昵称","勋章等级","动作","抖音号","sec_uid","uid","简介","粉丝","关注","性别","地区","精准","时间"]
#   ["1(10002)","热水高压清洗机厂家-张 2","点赞","13339936903Ly","MS4wLjABAAAAAFU8a-rlNIW3l8Ufnv1xuvE8pAIMRyH5473WOtSEmsxkdyuGn6l3aqPWwH61J1r-","2598852776955075","环境清洁综合解决方案服务商，专注于以物理方法解决表面深度清洁问题和持续改善环境质量等专业技术领域，致力规范行业专业可持续成长，打造高效、环保、节能、和谐的清洁行业生态圈。","2262","4439","女","武汉","2024-12-27","14:30:49"]
# 2. 抖音粉丝关注列表
#   ["编号","昵称","UID","简介","SECUID","抖音号","精准","蓝V认证","粉丝数"]
#   ["1","China赵哥","83773987928","怀念青春","MS4wLjABAAAARm5zZpjouaK6OmJbCrQsH88GN_7hbfwINMHWjFXmJTs","180317192","-","241"]
# 3. 抖音主页视频列表 关联 视频评论
#   ["编号","作者","标题","视频链接","发布时间▲","分享数▲","收藏数▲","评论数▲","UID"]
#   ["1","家美扫天下","这样的清洗方法很多进油烟管道清洗工人都要下岗了#厨房油烟竖管清洗神器#竖管清洗方案#油烟行业清洗油烟管道#一线自动清洗法清洗油烟管道#家美扫天下专用技术","https://www.douyin.com/channel/300203?modal_id=7453068664078650660","2024-12-27 20:33:24","12","1","3","2","104423938768"]
# 4. 抖音视频评论区
#   ["编号","视频链接","时间▲","昵称","评论内容","UID","抖音号","性别","地区","简介","粉丝▲","关注▲","精准","头像","SECUID"]
#   ["1","https://www.douyin.com/channel/300203?modal_id=7423055239663734051","2024-12-03 06:21:09","王大发专业清洗油烟管道","说的都是事实[赞][赞][赞]","2251407980767406","wangdafazhua","男","北京","专业清洗和维修，大型油烟机，风机，净化器，提供资质","423","731","https://p26.douyinpic.com/aweme/100x100/aweme-avatar/tos-cn-i-0813_9fb7d63f9d6149688b294c4747c6a260.jpeg?from=3067671334","MS4wLjABAAAAdJBpPp7ehiquidw84g-ZZEUlTLyZq30sB2bz3FNkJBwuimdVAgu_FIggLS6R1R98"]

def data_handle(handle):
    new_data = []
    print(handle())

    return

# TODO 获取数据 返回数据
# @data_handle
def get_datas():
    return read_excel(get_excel_files_list(excel_file_dir_path=TEST_EXCEL_DIR))



# TODO excel写入函数
def write_excel(all_data):
    pass


# TODO sql执行函数
# 传入sql语句、数据库路径
# 有数据 | 执行成功返回 None
def sql_operate(sql_sentence, db_path):
    pass
