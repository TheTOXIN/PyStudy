import json

file1 = open("E:\DEVELOPER\Python\json_1.txt", "r", encoding="utf-8")
json1 = json.load(file1)
print(json1)
file1.close()

user = {}
user["name"] = "Toxin"
user["age"] = 20
user["number"] = "8-800-555-35-55"

file2 = open("E:\DEVELOPER\Python\json_2.txt", "w", encoding="utf-8")
json.dump(user, file2)
file2.close()


