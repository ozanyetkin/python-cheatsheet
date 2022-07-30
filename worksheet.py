from collections import defaultdict


def def_value():
    return 0


a = defaultdict(def_value)
print(a)

a["ali"] = "veli"
print(a)
a.clear()

print(a)