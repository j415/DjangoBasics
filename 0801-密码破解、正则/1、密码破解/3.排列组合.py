import itertools

mylist = list(itertools.product("0123456789qwertyuiopasdfghjklzcvbnmQWERTYUIOPASDFGHJKLZXCVBNM", repeat=4))
# print(mylist)
print(len(mylist))
