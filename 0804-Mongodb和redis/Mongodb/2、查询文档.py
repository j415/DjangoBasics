import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId    # 用于ID查询


# 连接服务器
conn = MongoClient("localhost", 27017)

# 连接数据库
db = conn.mydb


# 获取集合
collection = db.student



# 查询部分文档
"""
res = collection.find({"age":{"$gt":18}})
for row in res:
    print(row)
    print(type(row))   
"""

# 查询所有文档

"""
res = collection.find()
for row in res:
    print(row)
    print(type(row))
"""

# 统计查询

"""
res = collection.find({"age":{"$gt":18}}).count()
print(res)
"""

# 根据id查询

"""
res = collection.find({"_id":ObjectId('5b6515dbb2e0dde58e2fc46d')})
print(res[0])
"""

# 排序查询

"""
# res = collection.find().sort("age") # 升序
res = collection.find().sort("age", pymongo.DESCENDING) # 降序
for row in res:
    print(row)
    print(type(row))
"""


# 分页查询

res = collection.find().skip(3).limit(5)
for row in res:
    print(row)







#断开
conn.close()








