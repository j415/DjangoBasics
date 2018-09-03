
"""
def insert_sort(alist):
    # 从第二个位置，即下标为1的元素开始向前插入
    for i in range(1, len(alist)):
        # 从第i个元素开始向前比较，如果小于前一个元素，交换位置
        for j in range(i, 0, -1):
            if alist[j] < alist[j-1]:
                alist[j], alist[j-1] = alist[j-1], alist[j]

alist = [54,26,93,17,77,31,44,55,20]
insert_sort(alist)
print(alist)
"""

def insert_sort(alist):
    """插入排序"""

    n = len(alist)
    # 从右边得无序序列中取出多少个执行这样的过程
    for j in range(1, n):
        # j = [1, 2, 3,...,n-1]
        # i 代表内层循环起始值
        i = j
        # 执行从右边的无需序列中取出第一个元素，即i位置的元素，然后将其插入到前面的正确位置中
        while i > 0:
            if alist[i] < alist[i-1]:
                alist[i], alist[i-1] = alist[i-1], alist[i]
                i -= 1
            else:
                break
        # i=j j-1 j-2 ...1
        #       range(j, 0, -1)

if __name__ == "__main__":
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    insert_sort(li)
    print(li)