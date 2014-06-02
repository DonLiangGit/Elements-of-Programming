'''
Created on Jun 1, 2014

@author: new
'''
def power(number):
    if number == 0:
        return 0
    if number < 0:
        number = -number
     
    i = 0
    difference = 1
    total = 0
    while i < number:
        total = total + difference
        difference += 2
        i += 1
        
    return total

print(power(7))