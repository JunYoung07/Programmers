# Fibonacci

def Fibo(n):
    if n < 2:
        return n
    return Fibo(n-1) + Fibo(n-2)
print(Fibo(5))

'''
def sigma(n):
    if n < 1:
        return 0
    return n + sigma(n-1)

print(sigma(4))

def factorial(n):
    if n <= 1:
        return 1
    return n*factorial(n-1)
print(factorial(3))
'''

