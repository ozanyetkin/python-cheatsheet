"""
*
**
***
****
*****
****
***
**
*
"""
symbol = input("bir sembol giriniz ")
repetition = input("bir sayi giriniz ")

while not repetition.isnumeric():
    repetition = input("bir sayi giriniz ")

repetition = int(repetition)
"""
for i in range(1, repetition):
    print(symbol * i)
for i in range(repetition, 0, -1):
    print(symbol * i)
"""
"""
i = 1
while i < repetition:
    print(symbol * i)
    i += 1
while i != 0:
    print(symbol * i)
    i -= 1
"""
"""
i = 1
j = 1
while i < 2 * repetition:
    print(symbol * j)
    i += 1
    if i <= repetition:
        j += 1
    else:
        j -= 1
"""
j = 1
for i in range(1, repetition * 2):
    print(symbol * j)
    if i < repetition:
        j += 1
    else:
        j -= 1
