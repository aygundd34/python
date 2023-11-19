# PAROLANIN KAÇ KARAKTER OLDUĞUNU VEREN KOD
parola=input("Parolanız: ")
toplam_uzunluk=len(parola)
mesaj="Parolanız toplam {} karakterden oluşuyor!"
if toplam_uzunluk > 12: 
    print(mesaj.format(toplam_uzunluk))
    print("Parolanızın toplam uzunluğu 12 karakteri geçmemeli!")
else:
    print(mesaj.format(toplam_uzunluk))
    print("Sisteme hoşgeldiniz!")