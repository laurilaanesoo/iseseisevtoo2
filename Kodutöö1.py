#Kodutöö 1
#02.03.2022
#Lauri Laanesoo

#Tervitus
def maailm():
    print("Tere, maailm!")
    
maailm()

#Aasta liblikas

aasta = 2020
liblikas = "teelehe-mosaiikliblikas"
lause_keskosa = "Aasta liblikas on "
lause = lause_keskosa + liblikas
 
print(lause)

#Pilved

input("Sisesta pilviede kõrgus kilomeetrites: ")
def a():
    if a > 6:
        print("Need on ülemised pilved")
    else:
        print("Need ei ole ülemised pilved")
print(a)

        
#Bussid
inimesed=int(input("Sisesta inimeste arv: "))
bussid=int(input("Sisesta busside arv:"))
kohad =int(input("Sisesta kohtade arv:"))

viimased=inimesed%kohad

if viimased==0:
    bussid=inimesed//kohad
    viimased=kohad
else:
    bussid=inimesed//kohad+1
    
print(f"Busse on vaja:{bussid}\nViimases bussis inimesi on: {viimased}")