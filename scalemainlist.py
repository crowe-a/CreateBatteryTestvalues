mainlist_80step=[0,30,26,30,0,37,40,37,30,37,17,30,0,0,55,60,40,55,30,35,28,30,17,17,30,22,0,40,17,20,0,35,30,35,0,45,0,45,50,0,0,60,65,28,40,28,45,30,38,60,28,60,45,55,50,75,60,70,60,80,80,35,55,50,80,80,25,60,65,60,55,65,60,55,70,70,0,0,80,80,0]

mainlist_120step=[0,30,26,30,15,  0,30,40,37,37,22,35,17,25,30,0,0, 40,43,60,50,42,55,40,20,0, 30,37,30,20,30,33,30,33,0   ,30,40,30,20,22,0,  20,37,35,37,0,50,0,45,50,20,0,0,   55,63,50,25,20,40,30,20,30,35,45,40,30,45,45,55,60,25,55,60,50,40,50,55,50,70,60,65,63,70,75,80,90,90,90,60,30,50,55,50,60,65,80,75,55,30,55,60,50,60,50,60,67,70,50,25,0,0,  40,60,80,80,80,75,40,25,0]

yenilist = []  # Burada düz liste olması için boş başlat

def scale_list(liste, yeni_min, yeni_max):
    eski_min = min(liste)
    eski_max = max(liste)

    scaled = [
        ((x - eski_min) / (eski_max - eski_min)) * (yeni_max - yeni_min) + yeni_min
        for x in liste
    ]
    # DÜZELTME: extend kullanarak düz liste olarak ekle
     # Her değeri 2 basamaklı yuvarlayarak ekle
    yuvarlanmis = [round(x, 2) for x in scaled]

    yenilist.extend(yuvarlanmis)  # Düz liste olarak ekle
    return yuvarlanmis

# Ölçeklendirme işlemi
scale_list(mainlist_120step, 0, 5.76)
print(yenilist)
print(len(yenilist))

rangelist=[]
for i in range(0,1200,10):
    rangelist.append(i)
    
