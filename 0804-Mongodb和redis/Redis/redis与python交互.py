import redis


# 连接
r = redis.StrictRedis(host="localhost", port=6379, password="15111202020")



# 方法1：根据数据类型不同，调用不同的响应方法

# 写
# r.set("p1", "good")

# 读
# print(r.get("p1"))


# 方法2：pipeline
# 缓冲多条命令，然后依次执行，减少服务器-客户端之间的TCP数据包

pipe = r.pipeline()
pipe.set("p2", "nice")
pipe.set("p3", "stupid")
pipe.set("p4", "heheda")
pipe.set("p5", "fool")
pipe.execute()

# 读(一样)
print(r.get("p2"))
print(r.get("p3"))
print(r.get("p4"))
print(r.get("p5"))

