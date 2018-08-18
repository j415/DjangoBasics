import urllib.request
import random

url = "http://www.baidu.com"

"""

# 模拟请求头
headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
}


# 设置一个请求体
req = urllib.request.Request(url,headers=headers)

# 发起请求
response = urllib.request.urlopen(req)
data = response.read().decode('utf-8')
print(data)

"""

agentsList = [
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.3.4000 Chrome/30.0.1599.101 Safari/537.36",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; SE 2.X MetaSr 1.0)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400) ",

]

agentStr = random.choice(agentsList)

req = urllib.request.Request(url)
# 向请求体里添加了User_Agent
req.add_header("User-Agent", agentStr)

response = urllib.request.urlopen(req)
data = response.read()
print(data)

with open(r'E:\all-workspace\qianfeng\0802-爬虫简介与json\file\filex.html', 'wb') as fi:
    fi.write(data)
