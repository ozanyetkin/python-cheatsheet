import pandas as pd
from collections import Counter

df = pd.read_table("11_advent_of_code/day_8.txt", header=None, delimiter="|")
input_digits = df[0][0].split(" ")
output_digits = df[1][0].split(" ")

def decoder(list_of_str):
    decoded_digits = {}
    encoded_digits = {}
    for s in list_of_str:
        encoded_digits.update({len(s):[]})
    for s in list_of_str:
        encoded_digits[len(s)].append(set(s))

    cf = encoded_digits[2][0]
    adg = encoded_digits[5][0].intersection(encoded_digits[5][1]).intersection(encoded_digits[5][2])

    decoded_digits.update({"a": encoded_digits[3][0].difference(cf)})

    for digit in encoded_digits[6]:
        advo = digit.difference(adg).difference(cf)
        if len(advo) == 1:
            decoded_digits.update({"b": advo})

    decoded_digits.update({"d": encoded_digits[4][0].difference(cf).difference(decoded_digits["b"])})
    decoded_digits.update({"e": encoded_digits[7][0].difference(adg).difference(cf).difference(decoded_digits["b"])})
    decoded_digits.update({"g": adg.difference(decoded_digits["a"]).difference(decoded_digits["d"])})

    for digit in encoded_digits[5]:
        test = digit.intersection(decoded_digits["e"])
        if len(test) == 1:
            decoded_digits.update({"c": digit.difference(adg).difference(decoded_digits["e"])})
    
    decoded_digits.update({"f": cf.difference(decoded_digits["c"])})

    decoded = {}
    for key, value in decoded_digits.items():
        decoded[list(value)[0]] = key

    return decoded

print(decoder(input_digits))

output_list = []
for i in range(len(df[0])):
    output_str = df[1][i].split(" ")
    key = decoder(df[0][i].split(" "))

    for str in output_str:
        number = ""
        for char in str:
            number += key[char]
        number_set = set(number)
        if number_set == set("abcefg"):
            output_list.append(0)
        if number_set == set("cf"):
            output_list.append(1)
        if number_set == set("acdeg"):
            output_list.append(2)
        if number_set == set("acdfg"):
            output_list.append(3)
        if number_set == set("bcdf"):
            output_list.append(4)
        if number_set == set("abdfg"):
            output_list.append(5)
        if number_set == set("abdefg"):
            output_list.append(6)
        if number_set == set("acf"):
            output_list.append(7)
        if number_set == set("abcdefg"):
            output_list.append(8)
        if number_set == set("abcdfg"):
            output_list.append(9)

print(Counter(output_list))
