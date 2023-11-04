#pi= 3,14159
def faktoryel(sayi):
    if(sayi==0):
        return 1
    else:
        deger=1
        for i in range(1,sayi+1):
            deger=deger*i

        return deger
def kesmeHatasi(gercek,yaklasik):
    sonuc=0
    sonuc=gercek-yaklasik
    return sonuc

def degerBul(terimSayisi,x):

    deger=1
    for i in range(1,terimSayisi+1):
        deger=((((-1)**i)*(x**(2*i)))/faktoryel(2*i))+deger


    return deger



print("!!!LÜTFEN İSTEDİĞİNİZ Pİ DEĞERİNİN YAKLAŞIK DEĞERİNİ GİRİNİZ!!!!!")

#EĞER X E SAYI GİRMEK YERİNE Pİ DEĞERİ GİRİLECEKSE YAKLAŞIK DEĞERİ GİRİLMELİDİR

x=float(input("cos(x) fonksyonu için x değerini girin : "))
terim=int(input("cos(x) fonksiyonunda kaç terimde değer hesaplayacağınızı yazınız : "))

print("İstediğiniz fonksiyonun yaklasik değeri :",degerBul(terim,x))

gercek=float(input("cas(x) fonksyonundaki gerçek değeri giriniz : "))

print("Kesme Hatası değeri :",kesmeHatasi(gercek,degerBul(terim,x)))





