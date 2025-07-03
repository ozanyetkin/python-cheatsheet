cal_sur = 0
maas = 10000

if cal_sur == 0:
    print("Yeni maasiniz: " + str(maas))
elif 0 < cal_sur <= 3:
    maas = maas * 1.05
    print("Yeni maasiniz: " + str(maas))
elif 3 < cal_sur <= 5:
    maas = maas * 1.10
    print("Yeni maasiniz: " + str(maas))
elif 50 > cal_sur > 5:
    maas = maas * 1.15
    print("Yeni maasiniz: " + str(maas))
else:
    print("Girdiginiz calisma suresinde hata var")
