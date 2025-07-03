from math import sqrt
e = float(input("Dodecahedron icin kenar uzunlugu giriniz:"))

# Formulu gormek icin linke tiklayabilirsiniz: https://www.google.com/search?q=dodecahedron+volume&bih=1071&biw=958&hl=en&sxsrf=ALiCzsYWMI_GSK45DxwQWT0hNfBbrhNNUA%3A1651926791763&source=hp&ei=B2d2Yr6TKtKJxc8PqLKSoAI&iflsig=AJiK0e8AAAAAYnZ1FzILeTtsEcr8pjJPnL6pzbDWqxZY&oq=&gs_lcp=Cgdnd3Mtd2l6EAEYADIHCCMQ6gIQJzIHCCMQ6gIQJzIHCCMQ6gIQJzIHCCMQ6gIQJzIHCCMQ6gIQJzIHCCMQ6gIQJzIHCCMQ6gIQJzIHCCMQ6gIQJzIHCCMQ6gIQJzIHCCMQ6gIQJ1AAWABg-QloAnAAeACAAQCIAQCSAQCYAQCwAQo&sclient=gws-wiz
v = (15 + 7 * sqrt(5)) * e ** 3 / 4
a = 3 * sqrt(25 + 10 * sqrt(5)) * e ** 2
print(f"Girdiginiz kenar uzunluguna gore yuzey alani = {a} hacim = {v}")

if  0 < v <= 1000:
    print("Hesaplanan hacim basim icin uygundur")
else:
    print("Hesaplanan hacim basim icin uygun degildir")
