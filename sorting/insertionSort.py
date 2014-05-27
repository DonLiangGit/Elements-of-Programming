

def insertionSort(alist):
    pivot = alist[0]
    i = 1    
    for index in range( 1, len(alist) ):  # insert a number to the list
        while i <= index:                 # comparisons in a certain index
            if alist[i-1] > alist[index]:     # switch element
                temp = alist[index]
                alist[index] = alist[i-1]
                alist[i-1] = temp                                         
            i += 1                        # print (i) / print (alist) will showing the process of insertion sort
        i = 1
    return alist

alist = [54,26,93,17,77,31,44,55,20]
insertionSort(alist)
print(alist)
