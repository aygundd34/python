print("1)Köroğlu, 2)Tarkan, 3)Kara Murat ")
print()
sayi = int(input("Yenilmezlerden birini seç "))
if sayi>=1 and sayi<=10:
    sayac=0
    for say in range(sayi+1):

        if sayi==1:
            sayac+=2
            print(sayac*"*", end="")

        elif sayi==2:
            sayac+=1
            print(sayac*"*", end="")

        elif sayi==3:
            print("*", end="")

    print(" yıldız gücünde bir karakter seçtin.")

else:
    print("lütfen yenilmezler listesinden bir tanesinin numarasını giriniz.")