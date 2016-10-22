# coding=utf-8
def bubbleSort(alist):
    '''
    冒泡排序
    通过数次交换将最大值放于最后
    '''
    for passnum in range(len(alist) - 1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
    return alist

if __name__ == '__main__':
    testlist = [9, 8, 4, 6, 2, 1, 3, 5, 0]
    print bubbleSort(testlist)
