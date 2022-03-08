#Iseseisevtöö 4
#Lauri Laanesoo
#08.03.2022

#Kuupäev

kuup = "24.02.1918"

def kuu_nimi(f):
    kuud = ["","jaanuar","veebruar","märts","aprill","mai","juuni","juuli","august","september","oktoober","detsember"]
    return kuud[f]


def kuupaev_sonena(g):
    
    a, b, c = g.split(".")
    kuupaev = f"{a}. {kuu_nimi(int(b))} {c}"
    return kuupaev
print(kuupaev_sonena(kuup))



#Banner

def banner(a):
    suur = a.upper()
    return suur
sisend = int(input("Mitu korda soovid reklaamlauset kuvada?: "))
for i in range(sisend):
    print(banner("Osta ja Sa ei kahetse!"))

#Õunamahl

oun = int(input("Sisesta õunte kogus kilogrammides: "))

def mahlapakkide_arv(b):
    arv = oun*0.4/3
    return round(arv)
print(mahlapakkide_arv(oun))

#Peo eelarve


def eelarve(c):
    inimesed =10*c+55
    return inimesed
kutsutud = int(input("Sisesta kutsutud inimeste arv: "))
tuleb = int(input("Sisesta tulevate inimeste arv: "))
print("Maksimaalne eelarve: ", eelarve(kutsutud))
print("Minimaalne eelareve: ", eelarve(tuleb))  

#Tervitused mõtisklustega

arv = int(input("Sisesta külaliste arv: "))

def tervitus(a):
    
    for i in range(a):
        print('Võõrustaja: "Tere!"')
        print(f"Täna {i+1} kord tervitada, mõtiskleb võõrustaja")
        print("ülaline: \"Tere, suur tänu kutse eest!\"")
tervitus(arv)

#Mündid
fail = "mündid.txt"
def pronksikarva_summa(e):
    nimi = input("Sisesta failinimi: ")
    if nimi == "mündid.txt":
        number = 0
        fail = open(e)
    for i in fail:
        if int(i) <= 5:
            number += int(i)
    return number    

print(pronksikarva_summa(fail))
     

