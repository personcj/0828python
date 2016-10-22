#coding=utf-8
def quickSort(alist):
    '''
    快速排序，运用递归与分治的思想实现排序。
    首先定义跳出（列表长度等于一时）
    然后定义递归的值由三部分组成（比中间值小的数＋中间值＋比中间值大的数）

    '''
    if len(alist) <= 1:
        return alist
    else:
        sleft = []
        sright = []
        pivot = alist[0]
        for x in alist[1:]:
            if x < pivot:
                sleft.append(x)
            else:
                sright.append(x)
        return quickSort(sleft) + [pivot] + quickSort(sright)
'''
pivot = alist[0]
return quickSort([x for x in alist[1:] if x < pivot]) + \
   [pivot] + \
   quickSort([x for x in alist[1:] if x >= pivot])
'''

if __name__ == '__main__':
    testlist = [3, 9, 8, 7, 6, 5, 1, 2, 4, 0]
    print quickSort(testlist)