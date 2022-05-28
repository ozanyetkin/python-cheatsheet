from tkinter import N


a_dict = {
    "name": "ozan",
    "surname": "yetkin"
}

print(a_dict.keys())
print(a_dict.values())
print(a_dict.items())
print(a_dict["name"])

class_dict = {
    "ali": ["ali", "tekin", 54],
    "mahmut": ["mahmut", "yilmaz", 64]
}

class_dict = {
    "names": ["ali", "mahmut"],
    "surnames": ["tekin", "yilmaz"],
    "grades": [54, 64]
}

print(class_dict["grades"][0])

a_student = {
    "surname": "tekin",
    "grade": 54,
    "name": "ali",
}

class_list = []
class_list.append(a_student)

a_dict.update({"name": "ali"})
a_dict.update({"mail": "asd@qwe.com"})
print(a_dict)
print(a_student["name"])