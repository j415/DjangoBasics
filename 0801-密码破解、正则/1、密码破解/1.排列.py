import itertools
# 从n个不同元素中取出m(m<=n)个元素，按照一定的顺序排成一列，叫做从n个元素中取出m个元素的一个排列(Arrangement)。特别的，当m=n时，这个排列被称作全排列(Permutation)。

"""
1      2      3      4


4种可能 3种可能 2种可能 1中可能

"""


mylist = list(itertools.permutations([1,2,3,4],3))
print(mylist)
print(len(mylist))


"""
4 - 3  24
4 - 2  12
4 - 1  6

"""