import re


# r表示原生字符，也就是说不转义字符，不需要再次被转义

print('--------------匹配单个字符与数字---------------------')

r"""

.               匹配除换行符以外的任意字符
[0123456789]    []是字符集和，表示匹配方括号中所包含的任意一个字符
[aspiring]      匹配'a','s','p','i','r','i','n','g'中任意一个字符   
[a-z]           匹配任意小写字母
[A-Z]           匹配任意大写字母
[0-9]           匹配任意数字，类似[0123456789]
[0-9a-zA-Z]     匹配任意的数字和字母
[0-9a-zA-Z_]    匹配任意的数字、字母和下划线
[^aspiring]     匹配除了aspiring这几个字母以外的所有字符，中括号里的^称为脱字符，表示不匹配集合中的字符
[^0-9]          匹配所有的非数字字符
\d              匹配数字，效果等同[0-9]
\D              匹配非数字字符，效果等同[^0-9]
\w              匹配数字、字母和下滑线，效果等同[0-9a-zA-Z_]
\W              匹配非数字、字母和下滑线，效果等同[^0-9a-zA-Z_]
\s              匹配任意的空白符(空格，换行，回车，换页，制表)，效果等同[ \f\n\r\t]
\S              匹配任意的非空白符(空格，换行，回车，换页，制表)，效果等同[^ \f\n\r\t]

"""




print(re.findall('.', 'aspiring is a good man \n 1 2 3',flags=re.S))

print('---')

print(re.findall('[^</p>]',"<p>test</p>"))


print("---------------锚字符(边界字符)---------------------")

'''

^               行首匹配，和在[]里的^不是一个意思
$               行尾匹配

\A              匹配字符串开始，它和^的区别是，\A只匹配整个字符串的开头，即使在re.M模式下也不会匹配它行的行首
\Z              匹配字符串结束，它和$的区别是，\Z只匹配整个字符串的结束，即使在re.M模式下也不会匹配它行的行尾

\b              匹配一个单词的边界，也就是单词和空格间的位置
                'er\b'可以匹配never，不能匹配nerve

\B              匹配非单词的边界

'''


print(re.search('^aspiring','aspiring is a good man'))
# print(re.search('man$','aspiring is a good man'))


print(re.findall('^aspiring','aspiring is a good man\naspiring is a nice man',flags=re.M))
print(re.findall('\Aaspiring','aspiring is a good man\naspiring is a nice man',flags=re.M))



print(re.findall('man$','aspiring is a good man\naspiring is a nice man',flags=re.M))
print(re.findall('man\Z','aspiring is a good man\naspiring is a nice man',flags=re.M))




print(re.search(r'er\b', 'never'))
print(re.search(r'er\b', 'nerve'))
print(re.search(r'er\B', 'never'))
print(re.search(r'er\B', 'nerve'))



print('---------------匹配多个字符---------------------')


'''
说明：下方的x、y、z均为假设的普通字符，不是正则表达式的元字符(xyz)，n、m（非负整数）   匹配小括号内的xyz(作为一个整体去匹配)


x?          匹配0个或者1个x
x*          匹配0个或者任意多个x（.*表示匹配0个或者任意多个字符(换行符除外)）
x+          匹配至少一个x
x{n}        匹配确定的n个x(n是一个非负整数)
x{n,}       匹配至少n个x
x{m,n}      匹配至少m个最多n个x。注意：m <= n
x|y         |表示或，匹配的是x或y

'''

print(re.findall(r'(aspiring)', 'aspiringgood is a good man,aspiring is a nice man'))
print(re.findall(r'a?', 'aaaagaaaa'))   #非贪婪匹配(尽可能少的匹配)
print(re.findall(r'a*', 'aaaabaaaa'))   #贪婪匹配(尽可能多的匹配)
print(re.findall(r'a+', 'aaaabaaaa'))   #贪婪匹配(尽可能多的匹配)
print(re.findall(r'a{3}', 'aaabaa'))
print(re.findall(r'a{3,}', 'aaaaabaaa'))   #贪婪匹配(尽可能多的匹配)
print(re.findall(r'a{3,5}', 'aaaaaabaabaaa'))   #贪婪匹配(尽可能多的匹配)
print(re.findall(r"((a|A)spiring)",'aspiring--Aspiring'))

# 需求，提取aspiring……man,

str = "aspiring is a good man! aspiring is a nice man! aspiring is a very handsome man"

print(re.findall(r'^aspiring.*?man$',str))


print('------------------特殊---------------------')

'''

*?   +?    x?       最小匹配，通常都是尽可能多的匹配，可以使用这种解决贪婪匹配
(?:x)               类似(xyz)，但不表示一个组

'''

# 注释：    /*   part1   */     /*     part2      */



print(re.findall(r"//*.*?/*/", r"/*   part1   */     /*     part2      */"))






print('------------------勿扰---------------------')



str = '<p>aspiring:to forge ahead</p>'

print(re.findall(r'<p>.*</p>', str))
# 括号表示将匹配到的字符串 括号里面的内容取出来
print(re.findall(r'<p>(.*)</p>', str))

print(re.search(r'(aspiring)', str))



