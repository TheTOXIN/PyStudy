class User:
    def __init__(self, name, age, number):
        self.name = name
        self.age = age
        self.number = number

    def toString(self):
        string = "{\n" \
                 "name: ", self.name, "\n" \
                 "age: ", self.age, "\n" \
                 "number: ", self.number, "\n" \
                 "}"
        return string

    def getFuncCheckAge(self):
        return lambda age: self.age < age

user = User("Yuri", 19, "2468")
print(user.toString())
check = user.getFuncCheckAge()
print(check(18))
