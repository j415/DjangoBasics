import urllib.request
import ssl
import re
import os
from collections import deque


def writeFileBytes(htmlBytes, toPath):
    with open(toPath, "wb") as f:
        f.write(htmlBytes)


def writeFileStr(htmlBytes, toPath):
    with open(toPath, 'w', encoding='utf-8') as f:
        f.write(htmlBytes.decode('utf-8'))


def getHtmlBytes(url):
    headers = {
        "User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; SE 2.X MetaSr 1.0)",
    }
    req = urllib.request.Request(url, headers=headers)
    context = ssl._create_unverified_context()
    response = urllib.request.urlopen(req, context=context)
    return response.read()


def qqCrawer(url, toPath):
    htmlBytes = getHtmlBytes(url)

    htmlStr = str(htmlBytes)

    pat1 = r'(((http|https|ftp)://)(([a-zA-Z0-9\._-]+\.[a-zA-Z]{2,6})|([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}))(:[0-9]{1,4})*(/[a-zA-Z0-9\&%_\./-~-]*)?)'
    re_url = re.compile(pat1)
    urlsList = re_url.findall(htmlStr)
    urlsList = list(set(urlsList))

    pat = r"[1-9]\d{4,9}"
    re_qq = re.compile(pat)

    qqsList = re_qq.findall(htmlStr)
    # 去重
    qqsList = list(set(qqsList))
    f = open(toPath, 'a')
    for qqStr in qqsList:
        f.write(qqStr + "\n")

    return urlsList


def center(url, toPath):
    queue = deque()

    queue.append(url)

    while len(queue) != 0:
        targetUrl = queue.popleft()
        urlList = qqCrawer(targetUrl, toPath)
        for item in urlList:
            tempUrl = item[0]
            queue.append(tempUrl)

url = "https://www.douban.com/group/topic/17359302/"
toPath = r"E:\all-workspace\qianfeng\0802-爬虫简介与json\爬虫\爬取网络中的QQ号码\qqFile.txt"


center(url, toPath)






            # writeFileBytes(htmlBytes, r"E:\all-workspace\qianfeng\0802-爬虫简介与json\爬虫\爬取网络中的QQ号码\file1.html")
            # writeFileStr(htmlBytes, r"E:\all-workspace\qianfeng\0802-爬虫简介与json\爬虫\爬取网络中的QQ号码\file2.txt")



qqCrawer(url, toPath)
