# lifeforlifeforlifeforlife, life 4
# lifeforlifeforlifeforlife, lifeforlife 3
# print("lifeforlifeforlifeforlife"[0:7])

def count_string(str_1, str_2):
    count = 0
    for i in range(len(str_1) - len(str_2) + 1):
        if str_1[i:i + len(str_2)] == str_2:
            count += 1
    return count

print(count_string("lifeforlifeforlifeforlife", "life"))
print(count_string("lifeforlifeforlifeforlife", "lifeforlife"))