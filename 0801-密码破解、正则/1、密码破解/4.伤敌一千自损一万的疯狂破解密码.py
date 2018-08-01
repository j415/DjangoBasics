import itertools
import time

# mylist = list(itertools.product("0123456789", repeat=4))
passwd = ("".join(x) for x in itertools.product("0123456789", repeat=8))
# print(mylist)
# print(next(passwd))
# print(next(passwd))
# print(next(passwd))
# print(next(passwd))
# print(next(passwd))

while True:
    try:
        # time.sleep(0.5)
        str1 = next(passwd)
        print(str1)

    except StopIteration as e:
        break
