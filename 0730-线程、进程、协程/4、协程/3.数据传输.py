def run():
    # 空变量,存储的作用,data始终为空
    data = "<->"
    r = yield "00"
    # r = a
    print(1, r, data)
    r = yield "aa"
    # r = b
    print(2, r, data)
    r = yield "bb"
    # r = c
    print(3, r, data)
    r = yield "cc"




m = run()
# 启动m


print(m.send(None))
print(m.send("a"))
print(m.send("b"))
print(m.send("c"))
print("******")

