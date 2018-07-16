# # import urllib2
# import urllib
# import json
# import time
# import datetime
# import threading
# import queue
# import sys
# #
# # reload(sys)
# # sys.setdefaultencoding("utf-8")
#
#
# def get_response(url):
#     for a in range(3):
#         try:
#             request = urllib2.Request(url)
#             response = urllib2.urlopen(request)
#             result = response.read()
#
#             return result
#
#         except Exception, e:
#             print
#             e
#             time.sleep(2)
#             continue
#
#
# class ThreadCity(threading.Thread):
#     def __init__(self, queue_zq_citys):
#         threading.Thread.__init__(self)
#         self.queue_zq_citys = queue_zq_citys
#
#     def run(self):
#
#         sql = 'select cityid,cname from  table '
#         citylist = DBHelper.SqlHelper.ms.ExecQuery(sql)
#
#         for c in citylist:
#             try:
#                 # 根据搜索城市名称获取城市
#                 qm_cname = c[1]
#                 data = urllib.urlencode({'q': qm_cname})
#                 url = 'xxx.xxx.com/ajax.do?' % data
#                 result = get_response(url)
#                 cjson = json.loads(result.decode('gb2312', 'ignore'))  # json格式字符串转换为python对象
#                 cityId = cjson["id"]
#                 cityname = cjson["cName"]
#
#                 # 加入队列
#                 self.queue_zq_citys.put({'cityid': cityId, 'cityname': cityname})
#                 time.sleep(1)
#
#             except Exception, e:
#                 pass
#
#
# class ThreadCityDB(threading.Thread):
#     def __init__(self, queue_zq_citys):
#         threading.Thread.__init__(self)
#         self.queue_zq_citys = queue_zq_citys
#
#     def run(self):
#         while True:
#             try:
#                 if self.queue_zq_citys.empty():  # 队列为空
#                     pass
#                 else:
#                     citys = self.queue_zq_citys.get()  # 从队列中取出数据
#                     if citys is not None:
#                         sql = "insert into Table(cityid,cityname) values(%s,'%s')" % (
#                             citys['cityid'], citys['cityname'])
#                         # print  sql
#                         DBHelper.SqlHelper.ms.ExecNonQuery(sql.encode('utf-8'))
#                         self.queue_zq_citys.task_done()  # 告诉线程我完成了这个任务 是否继续join阻塞 让线程向前执行或者退出
#                     else:
#                         pass
#             except Exception, e:
#                 pass
#
#
# def main():
#     try:
#
#         queue_zq_citys = Queue.Queue()  # 实例化存放抓取到的城市队列
#
#         # 创建线程
#         city = ThreadCity(queue_zq_citys)  # 抓取线程 入队操作
#         cityDB = ThreadCityDB(queue_zq_citys)  # 出队操作 存入数据库
#
#         # 启动线程
#         city.start()
#         cityDB.start()
#
#         # 阻塞等待子线程执行完毕后再执行主线程
#         city.join()
#         cityDB.join()
#     except Exception, e:
#         pass
#
#
# if __name__ == '__main__':
#     main()