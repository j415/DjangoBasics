"""

muliprocessing 库
跨平台版本的多进程模块，提供了一个Process类来代表一个进程对象


"""

from multiprocessing import Process
from time import sleep
import os


# 子进程需要执行的代码
def run(str):
    while True:
        print("aspiring %s --%s--%s"%(str, os.getpid(),os.getppid()))
        sleep(1.2)


if __name__ == "__main__":
    print("主(父)进程启动--%s"%(os.getpid()))
    # 创建子进程
    # target说明进程执行的任务
    p = Process(target=run, args=("perseverance",))
    # 启动进程
    p.start()

    while True:
        print("aspiring does not admit defeat")
        sleep(1)
