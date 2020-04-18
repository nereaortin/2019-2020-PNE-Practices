#-- Session 2. Exercise 3

def fibosum(n):
    index1= 0
    index2= 1
    sumn = 1
    count = 0

    for number in range(0, n+1):
        if number == 0:
            count = 0
        elif number == 1:
            count = count + 1
        else:
            count = index1 + index2
            index1 = index2
            index2 = count
            sumn = sumn + count
    return sumn
print("The sum of the first", 5, "terms of the fibonacci series:", fibosum(5))
print("The sum of the first", 10, "terms of the Fibonacci seies:", fibosum(10))