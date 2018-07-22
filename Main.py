import sys
import math
import datetime

message = "TEXT"
print(type(message))

int = 228
print(type(int))

float = 3.14
print(type(float))

complex = 1 * 5j
print(type(complex))

bool = True
print(type(bool))

print(hex(15))

print(dir(math))

print(math.pow(2, 10))
print(math.radians(180))

birthday = datetime.date(1998, 6, 4)
print(birthday.strftime("%d - %B - %Y (%A)"))

kitchen = datetime.time(16, 30, 0)
print(kitchen)

now = datetime.datetime.today()
print(now)