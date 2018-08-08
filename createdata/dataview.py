# -*- coding: utf-8 -*-
import pandas as pd

# f = open('data.txt','r',encoding = "utf-8").read()
# 18-25岁	26-28岁	28-30岁	31-35岁	36-40岁	41-45岁	46-50岁	51-55岁	56-60岁	61-65岁	66-70岁	71-75岁	76-80岁
list_18_25 = []
list_26_28 = []
list_28_30 = []
list_31_35 = []
list_36_40 = []
list_41_45 = []
list_46_50 = []
list_51_55 = []
list_56_60 = []
list_61_65 = []
list_66_70 = []
list_71_75 = []
list_76_80 = []

add_list = {"1": "宝山区",
            "2": "崇明县",
            "3": "奉贤区",
            "4": "虹口区",
            "5": "黄浦区",
            "6": "嘉定区",
            "7": "金山区",
            "8": "静安区",
            "9": "闵行区",
            "10": "浦东新区",
            "11": "普陀区",
            "12": "青浦区",
            "13": "松江区",
            "14": "徐汇区",
            "15": "杨浦区",
            "16": "闸北区",
            "17": "长宁区"}
sex_list = {"1": "男", "2": "女", "3": "男", "4": "女"}


def dataToline_alllist(line):
    line_list = str(line).replace("\n", "").split('\t')
    # sex = str(line_list[1])
    num = int(line_list[2])
    # address = str(line_list[3])
    # print(sex,num,addres)
    if num >= 18 and num <= 25:
        list_18_25.append(line_list)
    elif num >= 26 and num < 28:
        list_26_28.append(line_list)
    elif num >= 28 and num <= 30:
        list_28_30.append(line_list)
    elif num >= 31 and num <= 35:
        list_31_35.append(line_list)
    elif num >= 36 and num <= 40:
        list_36_40.append(line_list)
    elif num >= 41 and num <= 45:
        list_41_45.append(line_list)
    elif num >= 46 and num <= 50:
        list_46_50.append(line_list)
    elif num >= 51 and num <= 55:
        list_51_55.append(line_list)
    elif num >= 56 and num <= 60:
        list_56_60.append(line_list)
    elif num >= 61 and num <= 65:
        list_61_65.append(line_list)
    elif num >= 66 and num <= 70:
        list_66_70.append(line_list)
    elif num >= 71 and num <= 75:
        list_71_75.append(line_list)
    elif num >= 76 and num <= 80:
        list_76_80.append(line_list)
    else:
        print(" data is erro !")
        # print(line_list)
        # i = int(i) + 1
        # return


# 加载到 大集合  年龄分段
def add_all_list():
    list = []
    list.append(list_18_25)
    list.append(list_26_28)
    list.append(list_28_30)
    list.append(list_31_35)
    list.append(list_36_40)
    list.append(list_41_45)
    list.append(list_46_50)
    list.append(list_51_55)
    list.append(list_56_60)
    list.append(list_61_65)
    list.append(list_66_70)
    list.append(list_71_75)
    list.append(list_76_80)
    return list
    
    # print(line_list)


#  读取结果txt  返回 字典
#  "第n行":"数据"
def getResultTxt(num):
    result_dict = {}
    file_object = open('ture_' + str(num) + '.txt', 'r', encoding="utf-8")
    try:
        for index, line in zip(range(1, 18), file_object):
            result_dict.__setitem__(index, line.replace("\n", "").split('\t'))
    
    finally:
        file_object.close()
    return result_dict
    # for index in range(1,18):
    #     result_dict.__setitem__(index,line)


all_user_info = []


def getResultToSexAndAddressAndAge(result_dict, add_all_list, sex_item):
    # 结果格式
    # 年龄分段  x x x x x x x x x x x x x
    # 地区：    0 0 1 2 2 2 2 2 2 2 1 1 0
    
    SEX = sex_list[str(sex_item)]
    # 按地区 外层
    for address_index in range(1, 18):
        # 得到对应 结果行
        result_list = result_dict[address_index]
        address_temp = add_list[str(address_index)]
        
        # 结果集：      0 0 1 2 2 2 2 2 2 2 1 1 0
        # 迭代 年龄list list_18_25 list_26_28..
        # 结果集 对应年龄段
        print(result_list)
        for age_list_temp, result_item in zip(add_all_list, result_list):
            print("131", result_item)
            if int(result_item) != 0:
                user_info = []
                # for age_list_temp in add_all_list:
                # print()
                for age_list_item in age_list_temp:
                    #    TODO: 年龄每组人:  73222347590	男	77	闵行区
                    if user_info.__len__() >= int(result_item):
                        print("erro")
                        break
                    else:
                        if str(age_list_item[1]).__eq__(SEX) and str(age_list_item[3]).__eq__(address_temp):
                            user_info.append(age_list_item)
                            print("list len", user_info.__len__(), "---- 结果：", result_item)
                            user_info_temp = []
                            user_info_temp.append(age_list_item[0])
                            user_info_temp.append(age_list_item[1])
                            user_info_temp.append(age_list_item[2])
                            user_info_temp.append(age_list_item[3])
                            # user_info.append(list_item[])
                            all_user_info.append(user_info_temp)
                            # print(all_user_info)
                        # break
                        # else:
                        # print("-----------------------------")
                        # break
        else:
            print("result_item is 0")
            # break
    return all_user_info
    # 年龄分组
    # list_18_25 list_18_25
    # for ages_list_item in add_all_list:
    #     # 结果集：    0 0 1 2 2 2 2 2 2 2 1 1 0
    #     for result_item in result_list:
    #         print("130",result_item)
    #         if int(result_item) != 0:
    #             #    TODO: 年龄每组人:  73222347590	男	77	闵行区
    #             for list_item in ages_list_item:
    #                 user_info = []
    #                 if user_info.__len__() <= int(result_item):
    #                     if str(list_item[1]).__eq__(SEX) and str(list_item[3]).__eq__(address_temp):
    #                         user_info.append(list_item)
    #                         user_info_temp = []
    #                         user_info_temp.append(list_item[0])
    #                         user_info_temp.append(list_item[1])
    #                         user_info_temp.append(list_item[2])
    #                         user_info_temp.append(list_item[3])
    #
    #                         # user_info.append(list_item[])
    #                         all_user_info.append(user_info_temp)
    #                         print(all_user_info)
    #                     else:
    #                         print(" list_item is invalid data !")
    #                         # break
    #                 else:
    #                     print(" result_item is invalid data !")
    #                     # break
    #         else:
    #             print("result_item is 0")
    #             break


def run():
    file_object = open('data.txt', 'r', encoding="utf-8")
    try:
        for line in file_object:
            dataToline_alllist(line)
    finally:
        file_object.close()
        # add_all_list()


if __name__ == '__main__':
    
    # print(getResultTxt(1))
    
    titles = {"prod_inst_num", "gender", "age", "evening_station"}
    fileName = "D:/alldata.csv"
    run()
    all_list = add_all_list()
    for item in range(1, 3):
        result_dict = getResultTxt(item)
        all_list_temp = getResultToSexAndAddressAndAge(result_dict, all_list, item)
        print(all_list_temp)
    print("写入cvs格式文件")
    print('评论数：', all_list_temp.__len__())
    test = pd.DataFrame(columns=titles, data=all_list_temp)
    test.to_csv(fileName)
    # print(getResultTxt(1)[1])
    # print(result_dict[1])
    # run()
    # print("18", list_18_25.__len__())
    # print("26", list_26_28.__len__())
    # print("28", list_28_30.__len__())
    # print("31", list_31_35.__len__())
    # print("36", list_36_40.__len__())
    # print("41", list_41_45.__len__())
    # print("46", list_46_50.__len__())
    # print("51", list_51_55.__len__())
    # print("56", list_56_60.__len__())
    # print("61", list_61_65.__len__())
    # print("66", list_66_70.__len__())
    # print("71", list_71_75.__len__())
    # print("76", list_76_80.__len__())
    #
    # add_list = add_all_list()
    # print(add_list.__len__())
    # print(add_list)
