import os
import re
import urllib.request


def imageCrawer(url, toPath):
    headers = {
        "User-Agent":"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; SE 2.X MetaSr 1.0)",
    }
    req = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(req)
    HtmlStr = response.read().decode('utf-8')
    # with open(r"E:\all-workspace\qianfeng\0802-爬虫简介与json\file\yhd.html", 'wb') as fi:
    #     fi.write(HtmlStr)

    pat = r'<img src="//(.*?)"/>'

    re_image = re.compile(pat, re.S)
    imagesList = re_image.findall(HtmlStr)
    num = 1
    for imageUrl in imagesList:
        path = os.path.join(toPath, str(num)+".jpg")
        num += 1
        #把图片下载到本地
        urllib.request.urlretrieve("https://"+imageUrl, filename=path)

    # print(imagesList)
    # print(len(imagesList))
    # print(imagesList[8])

url = "http://search.yhd.com/c3287-0-0/mbname-b/a-s1-v0-p1-price-d0-f0b-m1-rt0-pid-mid0-color-size-k/"

toPath = "E:\all-workspace\qianfeng\0802-爬虫简介与json\image"

imageCrawer(url, toPath)



# pat = r'<img style="width:230px;height:322px" (original)|(src)="//(.*?)">'