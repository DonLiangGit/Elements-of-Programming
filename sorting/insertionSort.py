'''
Created on May 26, 2014

@author: Don Liang
'''

def insertionSort(alist):
    pivot = alist[0]
    i = 0
    for index in range( 1, len(alist)):
        while i <= index:
            if pivot > alist[index]:
                temp = pivot
                alist[index-1] = alist[index]
                alist[index] = temp
            i += 1
        i = 0
        pivot = alist[0]
    return alist

alist = [54,26,93,17,77,31,44,55,20]
insertionSort(alist)
print(alist)
