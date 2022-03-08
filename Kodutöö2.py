#Iseseisevtöö 2
#Lauri Laanesoo
#02.03.2022


#Äratus

aratus = int(input("Mitu korda äratus heliseb?: "))
for i in range(aratus):
    print("Tõuse ja sära")
    
    
#Ringid
    
ringid = int(input("Sisesta ringide arv: "))

porgandid = 0

i = 1
while i <= ringid:
 if i%2==0:
     porgandid+=i
     print(i)
 i += 1
print(f"Porgandite koguarv on {porgandid}")

#Täringud

import random

taring = int(input("Sisesta täringute arv: "))
for i in range(taring):
    print(random.randint(1,6))

#Male

taisarv = int(input("Sisesta täisarv: "))

nisu = 1

while i < taisarv:
    
    nisu*=2
    i += 1
print(f"Nisuteri on {taisarv}. Ruudu eest: {nisu}")

#Õunad
import random
lumi = 14
vmees = int(input("Mitu tahavad õuna?: "))
for i in range(vmees):
    oun = random.randint(1,2)
    print(oun)
    lumi = lumi - oun
print('Lumivalgekesele jäi: ', lumi)
    

