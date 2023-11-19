# #İSTENEN GEOMETRİK ŞEKİLİ ÇİZDİREN KOD PARÇASI

tekrar = int(input("Haydi bir oyun oynayalım! Kaç kere oynamak istersin? : "))
for i in range (1,tekrar+1,1):
    
    tur = input("Hangi şekli istiyorsun (dik üçgen, eşkenar üçgen, kare, dikdörtgen): ")

    if tur == "dik üçgen":
        satir = int(input("üçgen satır sayısını giriniz: "))
        for sayi in range(1,satir+1,1):
            print(sayi*"*")

    elif tur == "eşkenar üçgen":
        satir = int(input("Üçgen satır sayısını giriniz: "))
        sayac = satir
        for sayi in range(1,satir+1):
            print(sayac*" ",(2*sayi-1)*"*")
            sayac-=1

    elif tur == "kare":
        satir = int(input("Kare satır sayısını giriniz: "))
        for dis in range(1,satir+1):
            for ic in range(1,satir+1):
                print("*", end=" ")
            print()

    elif tur =="dikdörtgen":
        satir = int(input("Dikdörtgen satır sayısını giriniz: "))
        sutun = int(input("Dikdörtgen sütun sayısını giriniz: "))
        for satir in range(1,satir+1):
            for sutun in range(1,sutun+1):
                print("*", end=" ")
            print()

    else:
        print("Dik üçgen, eşkenar üçgen, kare ya da dikdörtgen seçebilirsiniz.")
        print()