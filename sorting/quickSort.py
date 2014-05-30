# @author: Don Liang
def quickSort(alist):
    quickSortCoordinator(alist,0,len(alist)-1)

def quickSortCoordinator(alist,first,last):
    if first < last:
        spilt = partition(alist,first,last)

        quickSortCoordinator(alist, first, spilt-1)
        quickSortCoordinator(alist, spilt+1, last)

def partition(alist, first, last):
    pivot = alist[first]
       
    # be aware of the index
    i = first + 1
    j = last
    done = False
    
    while not done:
        while i <= j and alist[i] <= pivot:
            i += 1    
        while i <= j and alist[j] >= pivot:
            j -= 1
        if j < i:
            done = True
        else:
            temp = alist[i]
            alist[i] = alist[j]
            alist[j] = temp

    # if i use pivot instead of alist[first], i am not changing the original alist[] element
    temp = alist[first]
    alist[first]= alist[j]
    alist[j] = temp

    return j
    
# test case
alist = [54,26,93,17,77,31,44,55,20]
quickSort(alist)
print(alist)
