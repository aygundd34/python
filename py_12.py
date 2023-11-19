# BOY UZUNLUĞUNA GÖRE YORUM VEREN KOD (ELİF YAPISI ÖRNEK)
boy=int(input("Boyunuz kaç cm: "))
if boy < 160 :
    print("Boyunuz kısa.")
elif boy < 180:
    print("Boyunuz normal.")
elif boy < 200:
    print("Boyunuz uzun.")
else:
    print("Boyunuz çok uzun.")