
u are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. Write a method that takes the array as an argument and returns this "outlier" N.

def find_outlier(integers):
    
    oddIntegerCounter = 0
    evenIntegerCounter = 0
    
    #Count all of the odd and even integers
    
    for i in integers:
        if (i%2 == 0):
            evenIntegerCounter += 1
        if(i%2 == 1):
            oddIntegerCounter += 1
    
    #Test which counter is higher, and return the outlier integer
    if(evenIntegerCounter > oddIntegerCounter):
        for i in integers:
            if(i%2 == 1):
                return i
    
    if(evenIntegerCounter < oddIntegerCounter):
        for i in integers:
            if(i%2 == 0):
                return i
