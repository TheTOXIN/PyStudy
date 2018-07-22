import random
import User

numbers = {}
print(type(numbers))

for i in range(1, 10):
    numbers[i] = random.random()

for n in numbers:
    print(numbers[n])

def my_random(a, b):
    return a * random.random() + b