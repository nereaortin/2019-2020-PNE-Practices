def Fibon(n):
    if n < 0:
        print("Incorrect input")
        # First Fibonacci number is 0
    elif n == 1:
        return 0
    # Second Fibonacci number is 1
    elif n == 2:
        return 1
    else:
        return Fibon(n - 1) + Fibon(n - 2)
def fibosum(n):
    fibonacci = 0
    for i in range(1, n+1):
        fibonacci = fibonacci + fibon(i)
    return fibonacci
print("The sum of the first", 5, "terms of the fibonacci series:", fibosum(5))
print("The sum of the first", 10, "terms of the Fibonacci seies:", fibosum(10))