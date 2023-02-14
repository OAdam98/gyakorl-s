import math

szam1=int(input("Szám: "))
while(szam1<0):
    print("Bem lehet negatív!")
    szam1=int(input("Új szaám: "))

szam2=int(input("Szám: "))

szamtani=(szam1+szam2)/2
mertani=round(math.sqrt((szam1*szam2)),2)

print("A beolvasott számoknak "+str(szamtani)+" a számtani közepe. ",)
print("A beolvasott számoknak "+str(mertani)+" a mértani közepe. ",)