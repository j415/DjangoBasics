"""
特点：把参数进行打包，单独传输


优点：数量大，安全(当对服务器数据进行修改时建议使用post)

缺点：速度慢


"""


import urllib.request
import  urllib.parse



url = "http://119.23.23.50:8000/user/login/?from=/blog/"

# 将要发送的数据合成一个字典
# 字典的键去网址里找，一般为input标签的name属性的值
data = {
    "username_or_email":"aspiring",
    "password":"meiyoumima",
}


# 对要发送的数据进行打包,记住编码
postData = urllib.parse.urlencode(data).encode('utf-8')

# 请求体
req = urllib.request.Request(url, data=postData)

# 请求
req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.3.4000 Chrome/30.0.1599.101 Safari/537.36")


response = urllib.request.urlopen(req)
print(response.data().decode('utf-8'))















