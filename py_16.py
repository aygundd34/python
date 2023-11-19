# İLK_METİN‘DE OLAN AMA İKİNCİ_METİN‘DE OLMAYAN ÖĞELERİ YAZDIRAN KOD.

ilk_metin= input("İlk kelimeyi giriniz: ")
ikinci_metin=input("İlk kelimeyi giriniz: ")
for s in ilk_metin:
    if not s in ikinci_metin:
        print(s, end = " ")