
class Matematik:
    def __init__(self, sayi1, sayi2):
        self.sayi1 = sayi1
        self.sayi2 = sayi2
        print("calisti")
    def topla(self):
        return self.sayi1 + self.sayi2
    def cikar(self):
        return self.sayi1 - self.sayi2
    def bol(self):
        return self.sayi1 / self.sayi2
    def carp(self):
        return self.sayi1 * self.sayi2

class Istatistik(Matematik):
    def __init__(self, sayi1, sayi2):
        super().__init__(sayi1,sayi2)
    def varyansHesapla(self):
        return self.sayi1 * self.sayi2

# inheritance - kalıtım

istatistik = Istatistik(5,8)
print(istatistik)