# MANAVDAN ALINANLARA GÖRE FİYAT HESAPLAYAN KOD PARÇASI
meyve=input("Hangi meyveyi istiyorsunuz: ")

if meyve==("muz"):
    kilo=int(input("Kaç kilo muz istiyorsunuz: "))
    print(kilo*5," TL ücret ödeyeceksiniz.")

elif meyve==("elma"):
    renk= input("Hangi renk elma istiyorsunuz: ")
    if renk==("kırmızı"):
        kilo=int(input("Kaç kilo kırmızı elma istiyorsunuz: "))
    elif renk==("sarı"):
        kilo=int(input("Kaç kilo sarı elma istiyorsunuz: "))
    elif renk==("yeşil"):
        kilo=int(input("Kaç kilo yeşil elma istiyorsunuz: "))
    else:
        print("Sadec, sarı, yeşil ve kırmızı renk elma bulunmaktadır.")

    print(kilo*2," TL ücret ödeyeceksiniz.")

elif meyve==("üzüm"):
    renk=(input("Hangi renk üzüm istiyorsunuz:"))
    if renk == ("mor"):
        kilo = int(input("Kaç kilo mor üzüm istiyorsun?"))
        print(kilo*3,"tl ücret ödeyeceksiniz.")
    elif renk ==("yeşil"):
        kilo = int(input("Kaç kilo yeşil üzüm istiyorsun?"))
        print(kilo*3.5,"tl ücret ödeyeceksiniz.")
    else:
        print("Sadece mor ya da yeşil renk üzüm var.")

else:
    print("Manavda sadece muz, elma ve üzüm bulunmaktadır.")