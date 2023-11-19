# Fonksiyonlar- GİRİLEN SAYININ KAREKÖKÜNÜ VEREN KOD 
import math
dir(math)
sayi= float(input("Sayi giriniz: "))
kok=math.sqrt(sayi)
print(sayi, " sayısının karekökü=" , kok)

# İç içe karekök fonsiyonu (İKİ KEZ KAREKÖK ALAN KOD)
import math
sayi= float(input("İki defa karekökü alınacak sayıyı giriniz: "))
y= math.sqrt(math.sqrt(sayi))
print(y)