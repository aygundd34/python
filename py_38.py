# PAROLA VE KULLANICI ADINDA TÜRKÇE KARAKTER KULLANILMASINI ÖNLEYEN KOD PARÇASI
harfler ="şçöğüİı"
k_adi=input("Kullanıcı adı: ")
parola = input("Parolanız: ")

for karakter in parola:
    if karakter in harfler:
        print("Parolada Türkçe karakter kullanılamaz.")
    elif k_adi in harfler:
        print("Kullanıcı adında Türkçe karakter kullanılamaz.")
