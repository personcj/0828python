# coding=utf-8
def selectionSort(alist):
    '''
    选择排序
    构建中间变量来存放每次比较所得的最值，然后将其至于合适的位置
    '''
    for passnum in range(len(alist), 0, -1):
        temp = alist[passnum - 1]
        for i in range(passnum - 1):
            if alist[i] < temp:
                temp = alist[i]
        alist.remove(temp)
        alist.append(temp)
    return alist

if __name__ == '__main__':
    testlist = [9, 8, 7, 6, 5, 1, 2, 4, 0]
    print selectionSort(testlist)
