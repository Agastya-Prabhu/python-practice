# def factorial(n):
#     if n == 1:
#             return n
#     x = n * factorial(n - 1)
#     return x

# x = factorial(6)
# print(x)

l = []

def fibonacci(n):
    if len(l) == n:
        return n
    return fibonacci(n-1)

x = fibonacci(5)
print(x)

