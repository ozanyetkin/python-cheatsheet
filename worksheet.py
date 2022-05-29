dct = {"a": 1, "b": 2}

def foo(d):
    b = d.copy()
    b.pop("a")
    return b

print(foo(dct))

print(type(dct.keys()))

for i, (k, v) in enumerate(dct.items()):
    print(i, k, v)