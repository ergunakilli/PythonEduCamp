# class tanımları

def selamVer():
    print("Merhaba")

def krediHesapla():
    print("Hesaplar yapıldı")

krediHesapla()

class Banka:
    def krediBasvur(self):
        print("Kredi başvurusu yapıldı")
    def krediHesapla(self):
        print("Hesaplar yapıldı")

banka = Banka()
banka.krediBasvur()
