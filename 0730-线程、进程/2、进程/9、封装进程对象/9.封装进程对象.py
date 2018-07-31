from aspiringProcess import AspiringProcess


if __name__ == "__main__":
    print("父进程启动")


    #创建子进程
    p = AspiringProcess('test')
    #自动调用p进程的run方法
    p.start()
    p.join()

    print("父进程结束")
