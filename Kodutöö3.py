#Iseseisevtöö 3
#Lauri Laanesoo
#08.03.2022

fail = open("rebased.txt", encoding="UTF-8")
vastuvõetud = []

for rida in fail:

    vastuvõetud.append(int(rida))

        fail.close()



#aasta = input("Sisesta , milline aasta")
#print(f"{aasta}")


#Porgandid

porgand = 0
ringid = int(input("Sisesta ringide arv: "))
for i in range(1,ringid):
    if i%2==0:
        porgand +=i
        
print(f"Saadavate progandite koguarv on {porgand}")
fail.close()

fail = input("Sisesta failinimi: ")
fail = open(fail, encoding="UTF-8")
num = 1
for i in fail:
    print(number+.string , i)
    number +=1
    


#Jukebox

fail = "edm.txt"

file = open(fail)
number = 0
for a in file:
    number += 1
    print(number,end=". ")
    print(a,end='')
    
sisend = int(input("\nSisesta valitud laulu number: "))

failid = open(fail)
numb = 0
for a in failid:
    numb += 1
    if numb == sisend:
        print(numb,end=". ")
        print(a,end='')
        


#Tahvli juurde
from datetime import *


fail = open("nimekiri.txt")
n = 1
for i in fail:
   if n == (datetime.now().day):
       print(i)
   n = n+1
    
   
