# coding=utf-8
def insertSort(alist):
    '''
    插入排序
    从最初始的两个元素开始排列每次插入一个元素
    当确定元素处于正确位置时跳出
    '''
    for passnum in range(1, len(alist)):
        position = passnum
        while position > 0 and alist[position - 1] > alist[position]:
            alist[position - 1], alist[position] = alist[position], alist[position - 1]
            if alist[position - 2] < alist[position - 1]:
                break
            position -= 1
if __name__ == '__main__':
    testlist = [9, 8, 7, 6, 5, 1, 2, 4, 0]
    insertSort(testlist)
    print testlist
