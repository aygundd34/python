#EHLİYET ALINIP ALINAMAYACAĞINA KARAR VEREN PROGRAM

ad=input("Ad ve Soyadınız: ")
yas=int(input("Yaşınız:"))

if (yas<18):
    print("18 yaşından küçük olduğunuz için ehliyet alamazsınız.")

else:
    egitim=input('Eğitim durumunuzu giriniz: "İlköğretim" , "Ortaöğretim" , "Lise", "Lisans", "Yüksek""Lisans" ')
    
    if (egitim=="İlköğretim" or egitim=="Ortaöğretim"):
        print("Sayın ", ad, " eğitim durumunuz yetersiz olduğundan ehliyet alamazsınız.")
    else:
        print("Sayın ", ad, " ehliyet alabilirsiniz.")