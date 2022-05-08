from math import gcd, sqrt

a_number = input("bir sayi giriniz: ")

if a_number.isnumeric():
    a_number = int(a_number)
else:
    print("hatali giris yaptiniz")
    exit()

if a_number > 1:
    if gcd(2, a_number) > 1:
        print("bu sayi cifttir")
    else:
        prime_list = [3]
        asal = True
        for i in prime_list:
            if i > sqrt(a_number):
                break
            if gcd(a_number, i) > 1:
                asal = False
                break
            cift_list = [2]
            advoc = i + 2
            for c in cift_list:
                if c % 2 == 0:
                    asal_advoc = True
                    for j in prime_list:
                        if j > sqrt(advoc):
                            break
                        if gcd(j, advoc) > 1:
                            asal_advoc = False
                            break
                    if asal_advoc:
                        prime_list.append(advoc)
                        break
                    else:
                        advoc = advoc + 2
                    cift_list.append(c)
    if asal:
        print("bu sayi asaldir")
    else:
        print("bu sayi asal degildir")
else:
    print("bu sayi asal olamaz")

print(prime_list)