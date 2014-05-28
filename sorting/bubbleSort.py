# your code goes here
# Test Case: List [ 2,4,5,7,1,2,3,6 ]
# Error 1: 'list' object cannot be interpreted as an integer
# Because range() only accepts integer, I parse a list obeject.
# Error 2: IndexError: list index out of range
# Because if i+1 <= max this condition i should be up to 7 not 8. cancel "="
def bubbleSort(aList):
	
	j = 1
	max = len(aList)
	while j < max:                      # comparisons for each round
		for i in range(len(aList)):
			if i+1 < max:
				if aList[i] < aList[i+1]:
					temp = aList[i]
					aList[i] = aList[i+1]
					aList[i+1] = temp
		max -= 1

aList = [2,4,5,7,1,2,3,6]
bubbleSort(aList)
print(aList)
