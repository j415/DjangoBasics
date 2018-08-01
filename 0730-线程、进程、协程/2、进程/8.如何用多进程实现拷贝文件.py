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

if __name__ == "__main__":
    # 读取path下的所有文件
    filesList = os.listdir(path)

    start = time.time()
    pp = Pool(4)
    for fileName in filesList:
        pp.apply_async(copyFile, args=(os.path.join(path, fileName), os.path.join(toPath, fileName)))
    pp.close()
    pp.join()
    end = time.time()
    print("多线程所耗时：{:.2f}".format(end-start))