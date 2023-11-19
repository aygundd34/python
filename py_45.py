# LİSTEDEKİ SAYILARIN 2 KATINI ALIP YENİ LİSTE OLUŞTURAN KOD PARÇASI
liste=[1,2,3,4,5,6,7]

def iki_kat_al(liste):
    i=0
    while i< len(liste):
        liste[i]=liste[i]*2
        i+=1
    return liste

yeni_liste = iki_kat_al([1, 2, 3, 4, 5, 6, 7])
print(f"Yeni Liste: {yeni_liste}")
