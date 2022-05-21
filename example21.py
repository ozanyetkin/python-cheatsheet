# "anagram", "nag a ram"
# "New York Times", "monkeys write"
# "Debit Card", "Bad Credit"
# "masa" "asam"
# "1234" "2341"

test_str = "a" * 100000

def is_anagram_1(str_1, str_2):
    str_1 = str_1.replace(" ", "").lower()
    str_2 = str_2.replace(" ", "").lower()

    while str_2 != "":
        for letter_1 in str_1:
            str_new = str_2.replace(letter_1, "", 1)
            if str_new == str_2:
                return False
            str_2 = str_new
    return True

def is_anagram_2(str1, str2):
    str1 = str1.lower().replace(" ", "")
    str2 = str2.lower().replace(" ", "")

    count = 0
    for s in str1:
        if s in str2:
            count += 1
    if len(str1) == len(str2) and count == len(str2):
        return True
    else:
        return False

from time import perf_counter

t1_start = perf_counter()
print(is_anagram_2(test_str, test_str))
# print(is_anagram("anagram", "nag a ram"))
# print(is_anagram("New York Times", "monkeys write"))
t1_stop = perf_counter()

print("Elapsed time during the whole program in seconds:", t1_stop-t1_start)
