from multiprocessing import Process
from time import sleep
import os

def stop(str):
    print("子进程启动-2")
    sleep(3)
    print("子进程结束-2")

def run(str):
    print("子进程启动")
    sleep(3)
    print("子进程结束")




if __name__ == "__main__":
    print("父进程启动")
    # 创建子进程
    # target说明进程执行的任务
    p = Process(target=run, args=("perseverance",))
    # 启动进程
    p.start()
    p2 = Process(target=stop, args=("perseverance",))
    # 启动进程
    p2.start()

    # 父进程的结束不能影响子进程，让父进程等待子进程结束再执行父进程
    p.join()
    # p2.join()


    print("父进程结束")