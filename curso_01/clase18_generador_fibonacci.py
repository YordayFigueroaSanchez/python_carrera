#Fibonacci
# 0 1 2 3 5 8 13 21 34 55
def fibonacci(limit):
    a,b=0,1
    while a < limit:
        yield a
        a,b=b,a+b
for value in fibonacci(50):
    print(value)