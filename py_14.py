#  1 DEN 100 E KADAR SAYILARI YAZDIRAN KOD (FOR DÖNGÜSÜ)
for n in range(1,100):
    print(n, end=" ")

# 1 DEN 100 E KADAR SAYILARI 5 ER YAZDIRAN KOD (FOR DÖNGÜSÜ)
for n in range(0,100,5):
    print(n, end= "\n" )

# 21 DEN -3 E KADAR OLAN SAYILARI YAZDIRAN KOD (FOR DÖNGÜSÜ)
for n in range(21,0,-3):
    print(n, end= "\n" )

# 1 DEN 100 E KADAR OLAN SAYILARI TOPLAYAN KOD (FOR DÖNGÜSÜ)
top=0
for i in range (1,100):
    top+=i
    print(top)
