class Person:
    # Initializer
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Getter
    def selam(self):
        return f"Merhaba, benim adim {self.name}, yasim {self.age}"

    # Modifier
    def yaslan(self):
        self.age += 1

    # Setter
    def isim_degistir(self, name):
        self.name = name

class Child(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
    
    def oyna(self):
        return "oyun oynamak cok eglenceli"

    def selam(self):
        return f"Ben {self.name}, {self.age} yasindayim"

p1 = Person("ali", 25)
print(p1.name)
p2 = Person("ayse", 26)
print(p2.age)

print(p1.selam())
p1.yaslan()
print(p1.selam())

print(p2.selam())
p3 = Person(715623, "sana ne")
print(p3.selam())
p3.isim_degistir("ahmet")
print(p3.selam())

c1 = Child("can", 9)
print(c1.selam())
print(c1.oyna())