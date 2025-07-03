a_number = input("bir sayi giriniz: ")

if a_number.isnumeric():
    a_number = int(a_number)
else:
    print("hatali giris yaptiniz")
    exit()

if a_number > 1:
    asal = True
    for n in range(2, a_number):
        if a_number % n == 0:
            asal = False
            break

    if asal == True:
        print("bu bir asal sayidir")
    else:
        print("bu bir asal sayi degildir")
else:
    print("bu bir asal sayi degildir")
