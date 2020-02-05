#Session 2. Exercise 1


a, b = 0, 1

for i in range(11):
    print(a, end=' ')
    a, b = b, a + b

#Session 2. Exercise 2

def fibon(n):
    index1 = 0
    index2 = 0
    sumn = 0
    count = 0
    for number in range(0, n+1):
        if number == 0:
            sumn = 0
        # First Fibonacci number is 0
        elif number == 1:
            sumn = sumn + 1
    # Second Fibonacci number is 1
        else:
            count = index1 + index2
            index1 = index2
            sumn = sumn + count
    return sumn

print("sumn of the first 5 terms of trhe fibonacci series is :", fibo(5))
print("sumn of the first 5 terms of trhe fibonacci series is :", fibo(5))
#Exercise3
