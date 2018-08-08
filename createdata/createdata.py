# -*- coding: utf-8 -*-
import random
import pandas as pd

# def getdataTitleList():
titles = {"prod_inst_num","gender","age","evening_station"}
    # return title_list

add_list = {"1":"宝山区",
            "2":"崇明县",
            "3":"奉贤区",
            "4":"虹口区",
            "5":"黄浦区",
           "6":"嘉定区",
           "7":"金山区",
           "8":"静安区",
           "9":"闵行区",
           "10":"浦东新区",
           "11":"普陀区",
           "12":"青浦区",
           "13":"松江区",
           "14":"徐汇区",
           "15":"杨浦区",
           "16":"闸北区",
           "17":"长宁区"}
sex_list = {"1":"男","2":"女"}

def getdata():
    list_info = []
    # age = random.randint(18,80)
    phone = random.randint(10000000000, 99999999999)
    list_info.append(phone)
    sex = sex_list[str(random.randint(1,2))]
    list_info.append(sex)
    age = random.randint(18, 80)
    list_info.append(age)
    address =  add_list[str(random.randint(1, 16))]
    list_info.append(address)
    return list_info
    
    
    
    
    
    
    
if __name__ == '__main__':
    list_content = []
    fileName = "D:/data.csv"
    for item in range(1,1000000):
        # print(add_list[str(random.randint(0,10))])
        list = getdata()
        list_content.append(list)
        print(list)
        # print(getdata())
    # print(sex_list[str(random.randint(1,2))])

    print("写入cvs格式文件")
    print('评论数：', list_content.__len__())
    test = pd.DataFrame(columns=titles, data=list_content)
    test.to_csv(fileName)
