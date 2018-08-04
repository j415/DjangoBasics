from pymongo import MongoClient

# 连接服务器
conn = MongoClient("localhost", 27017)

# 连接数据库
db = conn.mydb


# 获取集合
collection = db.student



# 更新
# collection.update({"name":"add1"}, {"$set":{"age":24}})
collection.remove({"name":"add1"})



#断开
conn.close()








