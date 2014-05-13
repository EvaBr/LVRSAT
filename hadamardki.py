from hadamard import *
from dpll import *

print("\n"+"*"*20)
print("* Prikaz delovanja DPLL-ja na odločitvenem problemu obstoja Hadamardove matrike velikosti nxn")
print("*"*20+"\n")

print("""[OPOZORILO: priporočeni so n<10. Dinamična verzija funkcije, ki vrne logično formulo tega problema sicer deluje kar hitro (za n=24 
potrebuje zgolj 12s, za n=14 manj kot pol sekunde), vendar pa lahko pretvorba v cnf obliko že pri n=6 potrebuje ogromnih 30+ min...]""")

sajz = int(input("\nVnesi n:  "))
prikaz1 = input("Želiš prikaz formule? (y/n)  ")
prikaz2 = input("Želiš prikaz njene CNF oblike? (y/n)  ")

H = hadamard2(sajz)
if prikaz1=="y":
    print("\nLogična formula:\n hadamard2({0}) = ".format(sajz), H)

C = H.cnf()
if prikaz2=="y":
    print("\nCNF oblika formule:\n formula.cnf() = ", C)

D = dpll(C)

print("\nPreverjanje rešljivosti formule:\n dpll(formula.cnf()) = ", D)

interp = input("Želiš človeku prijazno interpretacijo rezultata? (y/n)  ")
if interp=="y":
    if D==0:
        print("\nHadamardova matrika velikosti {0}x{0} ne obstaja. ".format(sajz))
    else:
        def polje(spr):
            lst = map(int,spr[2:-1].split(","))
            return tuple(lst)
        D = {polje(i) : " 1" if D[i]==T() else "-1" for i in D}
        print("\nPrimer Hadamardove matrike velikosti {0}x{0}: ".format(sajz))
        for vr in range(1, sajz+1):
            vrstica = "\t | " + " ".join([D[(vr, st)] for st in range(1, sajz+1)]) + " |"
            print(vrstica)
                
