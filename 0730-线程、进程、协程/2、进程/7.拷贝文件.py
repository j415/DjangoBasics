import os, time
from multiprocessing import Pool


def copyFile(rPath, wPath):
    fr = open(rPath, 'rb')
    fw = open(wPath, 'wb')

    context = fr.read()
    fw.write(context)

    fr.close()
    fw.close()


path = r'E:\all-workspace\qianfeng\0730-线程、进程\2、进程\file'
toPath = r'E:\all-workspace\qianfeng\0730-线程、进程\2、进程\toFile'

# 读取path下的所有文件
filesList = os.listdir(path)

# 启动for循环处理每一个文件

start = time.time()
for fileName in filesList:
    copyFile(os.path.join(path, fileName), os.path.join(toPath, fileName))
end = time.time()
print("总耗时：{:.2f}".format(end - start))
