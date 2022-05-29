import random

a = ["1", "asdasd", 3, 4, 5]
print(random.randint(0, 10))
print(random.choice(a))

contacts = {"atom1": {"atom2": True, "atom3": False, "atom4": True}}
["atom5", "atom12"]
contacts = {"atom1": ["atom5", "atom12"]}


d = {}
d["a"] = "b"
print(d)

aminoacids = {
    1: "A", 2: "C", 3: "D", 4: "E", 5: "F", 6: "G", 7: "H", 8: "I", 9: "K", 10: "L", 11: "M",
    12: "N", 13: "P", 14: "Q", 15: "R", 16: "S", 17: "T", 18: "V", 19: "W", 20: "Y"
}

for i in range(1, 6):
    aminoacids[i] += f"${i}"

print(aminoacids)