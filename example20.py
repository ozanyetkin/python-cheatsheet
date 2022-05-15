# 321581262662993888198883612863553555553192875390101
girdi = "12233322"
"""
def longest_consecutive(input_str):
    last_visited = ""
    longest_repetition = ""
    longest_count = 0
    for i, digit in enumerate(input_str):
        last_visited = input_str[i - 1]
        if last_visited == digit:
            longest_repetition += digit
            longest_count += 1
    print(longest_repetition)
"""

def sayac(bas):
    tekrar_uzunlugu = 1
    if bas >= len(girdi) - 1:
        return girdi[-1], tekrar_uzunlugu
    while girdi[bas] == girdi[bas + 1]:
        tekrar_uzunlugu += 1
        bas += 1
        if bas == len(girdi) - 1:
            break
    return girdi[bas], tekrar_uzunlugu

sonuc = sayac(0)
i = sonuc[1]
while i <= len(girdi) - 1:
    uzunluk = sayac(i)[1]
    if uzunluk >= sonuc[1]:
        sonuc = sayac(i)
    i += uzunluk

print(sonuc)
# longest_consecutive("321581262662993888198883612863553555553192875390101")

def consecutive_repeat(user_str):
    last_letter = ""
    longest_word = ""
    current_count = 1
    max_count = 1
    for s in user_str:
        if s == last_letter:
            current_count += 1
            longest_word += s
            if current_count > max_count:
                max_count = current_count
        else:
            current_count = 1
            last_letter = s
    return longest_word[len(longest_word) - max_count::]

print(consecutive_repeat(girdi))