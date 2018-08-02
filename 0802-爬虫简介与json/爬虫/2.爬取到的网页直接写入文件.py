

import  urllib.request

urllib.request.urlretrieve("http://www.baidu.com",filename=r'E:\all-workspace\qianfeng\0802-爬虫简介与json\file\file2.html')

# urlretrieve 在执行的过程当中，会造成一些缓存
# 清除缓存
urllib.request.urlcleanup()










