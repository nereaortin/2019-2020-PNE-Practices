#Session 2. Exercise 2

def fibonacci(n):
    index1 = 0
    index2 = 1

    count = 0
    for number in range(0, n+1):
        if number == 0:
            count = 0
        # First Fibonacci number is 0
        elif number == 1:
            count = count + 1
    # Second Fibonacci number is 1
        else:
            count = index1 + index2
            index1 = index2
            index2 = count
    return count

print("5th Fibonacci term: ", fibonacci(5))
print("10th Fibonacci term:", fibonacci(10))
print("15th Fibonacci term:", fibonacci(15))