a_list = ["a", 5, 3.2, [1, 3, "b"]]
a_dict = {"name": "ozan", "surname": "yetkin", "phone": "05823124912", "mail": "ozanyetkin@test.com"}
b_list = a_list
b_dict = a_dict
print(a_dict["name"])

another_dict = {
    "key": "value",
    5: [1, 2, 4],
    "b": {
        "a": "b",
        "3": 2
    },
    "a": 3.2,
}

def list_modify(lst):
    lst.append(1)

list_modify(a_list)
print(a_list)
print(a_list)

def dict_modify(dct):
    dct.update({"key": "value"})

dict_modify(a_dict)
print(a_dict)
print(b_dict)

print(another_dict)