import urllib.request

url = "https://www.baidu.com"


#向指定的url地址发起请求，并返回服务器响应的数据(文件的对象)
response = urllib.request.urlopen(url)

# 读取文件的全部内容，会把读取到的数据赋值给一个字符串变量
data = response.read().decode('utf-8')
print(data)
print(type(data))


# 读取一行
# data = response.readline()

# 读取文件的全部内容，会把读取到的数据赋值给一个列表变量
# data = response.readlines()
"""

print(data)
print(type(data))
print(len(data))
print(type(data[100].decode('utf-8')))

"""


# 将爬取到的网页写入文件
# with open(r'E:\all-workspace\qianfeng\0802-爬虫简介与json\file\file1.html','wb') as f:
#     f.write(data)


# response 属性

#
# #返回当前环境的有关信息
# print(response.info())
#
# # 返回状态码
# print(response.getcode())
# if response.getcode() == 200 or response.getcode() == 304:
#     # 处理网页信息-*
#     pass
#
# # 返回当前正在爬取的url地址
# print(response.geturl())
#
# #
#
#



"""


url = r'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=baidu&wd=%E5%87%AF%E5%93%A5%E5%AD%A6%E5%A0%82&oq=%25E5%2587%25AF%25E5%2593%25A5&rsv_pq=ee810d0c000099c9&rsv_t=3df6PEvqvXzzHv%2FhcVViQnpO%2BRce%2FTd6AxbeU1BOb5tu02YWFDmRH0U%2F4J4&rqlang=cn&rsv_enter=1&inputT=2356&rsv_sug3=19&rsv_sug1=15&rsv_sug7=100&rsv_sug2=0&rsv_sug4=3803'

# 解码
newUrl = urllib.request.unquote(url)
print(newUrl)

# 编码
newUrl2 = urllib.request.quote(newUrl)
print(newUrl2)




"""




















