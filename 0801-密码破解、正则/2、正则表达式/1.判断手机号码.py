import re
"""
给你一个字符串，判断这是否是手机号码

"""
def checkPhone(str):
    if len(str) != 11:
        print(str ,"a", end="--")
        return False
    elif str[:1] != "1":
        print(str ,"b", end="--")
        return False
    elif str[1:3] != "39" and str[1:3] != '31':
        print(str ,"c", end="--")
        return False

    for i in range(3, 11):
        if str[i] < '0' or str[i] > '9':
            print(str, "d", end="--")
            return False
    else:
        return True


def checkPhone2(str):
    #13912345678
    pat = r'^1(([3578]\d)|(47))\d{8}$'
    res = re.match(pat,str)
    print(res)


#
# print(checkPhone2("13912345678"))
# print(checkPhone2("139123456785"))
# print(checkPhone2("13912345a78"))
# print(checkPhone2("14712345778"))
# print(checkPhone2("19012345678"))
# print(checkPhone2("35912345678"))

def checkPhone3(str):
    #13912345678
    pat = r'(1(([3578]\d)|(47))\d{8})'
    res = re.match(pat,str)
    return res



print(checkPhone3("fjfafdjadfjsafdjsafssd13945645645dddddsssaaa14788889999"))



"""

QQ                  6666-1234567890
mail                1720049083@qq.com
phone               010-56747894
user                6到12位
passwd
ip
url


"""

re_QQ = re.compile(r'^[1-9]\d{5,9}$')

print(re_QQ.search('123456746'))
print(re_QQ.search('12345a746'))
print(re_QQ.search('0123458746'))

print(re_QQ.search('123456700046'))



re_mail = re.compile(r'^[1-9a-zA-Z][0-9a-zA-Z]+@[0-9a-zA-Z]{0,4}.[0-9a-zA-Z]{1,9}')

print(re_mail.search('1720049083@qq.com'))
print(re_mail.search('aspiring@360.jiang'))







