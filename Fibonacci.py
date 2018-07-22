
cache = {}

def fibonacci(n):
    if type(n) != int:
        raise TypeError("n must be a INT")

    if n in cache:
        return cache[n]

    if n == 1:
        value = 1
    elif n == 2:
        value = 2
    elif n > 2:
        value = fibonacci(n - 1) + fibonacci(n - 2)

    cache[n] = value
    return value


for i in range(1, 11):
    print(i, ":", fibonacci(i))
