liste=[int]
for k in range(6):
    liste.append(int(input("Listeye Eklenecek Nesneleri Giriniz: ")))
a=0
sayac=0
k=0
maxi=0
for i in liste:
    if a<5:
        a=a+1
        print("sayac:",sayac)
    if i==liste[a] and i==1:
        sayac=sayac+1
        print("sayac:a",sayac)
        if sayac>maxi:
            maxi=sayac
            print("maxi=",maxi)
    else:
        sayac=0
    print("a:",a)
    
print("sayac:",maxi)