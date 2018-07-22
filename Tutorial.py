import math
import timeit


def volume(r, hueta=0):
    """VOLUME"""
    v = (4.0 / 3.0) * math.pi * r ** 3 + hueta
    return v


volume(3)
volume(3, 1)

people = {228, True}
print(type(people))
people.add("Yuri")
if "Toxin" not in people:
    len(people)

numbers = [1, 2, 3, 4, 5]
print(type(numbers))
var = numbers[0:4]

user = {"name": "Toxin", "age": 20}
print(type(user))

try:
    print(user['name'])
except KeyError:
    print("ERROR")

for key in user.keys():
    value = user[key]
    print(key, " = ", value)

a = input("Input A = ")
b = input("Input B = ")
c = input("Input C = ")

if a != c and b != c and b != c:
    print("A != B != C")
elif a == c or c == b:
    print("A == C or C == B")
else:
    pass
