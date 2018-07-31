from multiprocessing import Process
# from time import sleep
import time

num = 100 # 全局变量

def test():
    print("测试开始")
    time.sleep(2.5)
    print("测试结束")

def run():
    print("子进程开始")
    # global关键字用来在函数或其他局部作用域中使用全局变量
    global num  # 等同于在子进程定义了一个新的num=100的变量
    num += 1
    print("子进程结束--%d" % num)

if __name__ == "__main__":
    print("父进程开始")

    p1 = Process(target=test) # 如果写成target=run() 就表示执行run方法的返回值
    p1.start()
    p1.join()

    p = Process(target=run)

    p.start()
    p.join()

    # 在子进程中修改全局变量对父进程中的全局变量没有影响
    # 在创建子进程时对全局变量做了一个备份，父进程中的与子进程中的num是完全不同的两个变量
    print("父进程结束--%d" %num)