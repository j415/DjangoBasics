import threading

def run():
    print("aspiring ----")




t= threading.Timer(5, run)
t.start()
t.join()

print("父线程结束")
