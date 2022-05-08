series = range(2, 1000)

asal_sayilar = []
for num in series:
    asal = True
    for n in range(2, num):
        if num % n == 0:
            asal = False
            break
    
    if asal == True:
        print(f"{num} bir asal sayidir")
        asal_sayilar.append(num)
    else:
        print(f"{num} bir asal sayi degildir")

print(asal_sayilar)
