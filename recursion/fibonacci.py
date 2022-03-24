# 0 1 1 2 3 5
def fibonacci(n):
    if n == 0 or n == 1:
        return n

    return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(5))

# Normal way to do fibonacci 

class A:
    def fibo(n):
        f1 = 0
        f2 = 1
        test = ""
        for i in range(1,n):
            test = f1 + f2
            f1 = f2
            f2 = test
        return test


a = A
print(a.fibo(5))
            