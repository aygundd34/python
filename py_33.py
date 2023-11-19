# SAATİN 7' DE ÇALMASINI SAĞLAYAN KOD PARÇASI

saat=int(input("Saati giriniz: "))
if saat<7 or saat>7:
    print("Uyumaya devam...")
elif saat==7:
    print("Alarma çalıyor, kalk...")
else:
    print("Lütfen bir saat giriniz")