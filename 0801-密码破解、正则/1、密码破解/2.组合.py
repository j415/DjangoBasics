import itertools

"""
组合（combination）是一个数学名词。一般地，从n个不同的元素中，任取m（m≤n）个元素为一组，叫作从n个不同元素中取出m个元素的一个组合。我们把有关求组合的个数的问题叫作组合问题。
"""



mylist = list(itertools.combinations([1,2,3,4,5],1))
print(mylist)
print(len(mylist))

"""
5 - 5  1
5 - 4  5
5 - 3  10
5 - 2  10
5 - 1  5

120/120(n-m)!
120/24(n-m)!
120/6(n-m)!
n!/(m!(m-n)!)


"""
