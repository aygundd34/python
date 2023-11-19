# PAROLADA TÜRKÇE KARAKTER KULLANILMASINA İZİN VERMEYEN KOD.

tr_harfler = "ŞşÇçĞğÖöÜüİi"

parola = input("Parolanız: ")

for karakter in parola:
    if karakter in tr_harfler:
        print("Parolada Türkçe karakter kullanılamaz.")