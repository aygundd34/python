# SAYI TAHMİN ETME OYUNU
import random

print("**********Sayı Tahmin Oyununa Hoşgeldiniz...***********")
oynamak_istiyor_musun="Evet"

while oynamak_istiyor_musun=="Evet":
    cevap=random.randint(1,100)
    tahmin=int(input("1 ile 100 arasında bir sayıyı tahmin et: "))
    hak=1

    while tahmin!=cevap:
        if tahmin>cevap:
            print("Yanlış! Bir dahakine daha küçük sayı tahmin et!")
        
        if tahmin<cevap:
            print("Yanlış! Bir dahakine daha büyük sayı tahmin et!")
        tahmin=int(input("1 ile 100 arasında bir sayıyı tahmin et: "))
        hak +=1

    else:
        print("Tebrikler, kazandın! Kazanan tahmin: ", cevap)
        



