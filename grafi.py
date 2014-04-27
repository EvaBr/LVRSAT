##########################################################################
#									 #
#           Nekaj primerov grafov za preizkušanje barvanj.		 #
#									 #
# Vse funkcije sprejmejo število vozlišč n in vrnejo seznam povezav, ki  #
# jih ima graf želene oblike na n vozliščih.				 #
#									 #
##########################################################################

from barvanje import *
from dpll2 import*
from boolean import *
from cnf import *

def polnigraf(n):
    sez=[]
    for i in range (1,n):
        for j in range (i+1, n+1):
            sez.append((i, j))
    return sez

def pot(n):
    sez=[]
    for i in range (1,n):
        sez.append((i, i+1))
    return sez

def cikel(n):
    sez=[]
    for i in range (1,n):
        sez.append((i, i+1))
    sez.append((n,1))
    return sez

#Petersenov graf; n=10

petersen=[]
for i in range (1, 5):
    petersen.append((i,i+1))
    petersen.append((i, i+5))
petersen.append((5, 1))
petersen.append((5,10))
for j in range (6, 10):
    petersen.append((j, ((j+2)%5) +1+5))
petersen.append((8,10))
    

#groetzchev graf; n=11
#biti mora 4-obarvljiv!

grotzch=[]
for i in range (1,5):
    grotzch.append((i,i+1))
grotzch.append((5,1))
for j in range(6,11):
    grotzch.append((j,11))
grotzch.append((1,7))
grotzch.append((1,10))
grotzch.append((2,6))
grotzch.append((2,8))
grotzch.append((3,7))
grotzch.append((3,9))
grotzch.append((4,8))
grotzch.append((4,10))
grotzch.append((5,6))
grotzch.append((5,9))



def HumanFriendlyVersion(dplldict):
    Ok = {}
    for spr in dplldict:
        if dplldict[spr]==T():
            [oglisce, barva] = spr.ime.split(".")
            [oglisce, barva] = [oglisce[1:], int(barva)]
            Ok["oglisce " + oglisce] = barva
    return Ok



####################################
#Komunikacija z uporabnikom datoteke:
#

print("Hello, stranger!\n")
print("Zaupamo ti, da bodo tvoji vnosi odgovorov skladni s pričakovanji programa. Or else... ;) \n\n")
print("Dovoljene izbire (če ni drugače zapisano): \n   0 ... ne, hvala \n   nat k ... da, preveri k obarvljivost\n\n")

Pet = int(input("Želiš preizkusiti obarvljivost petersenovega grafa? \n"))
Gro = int(input("Želiš preizkusiti obarvljivost grotzchevega grafa? \n"))

Poln = int(input("Želiš preizkusiti obarvljivost polnega grafa? \n"))
if Poln!=0:
    k1 = int(input("Željeno št. vozlišč grafa: (vpiši naravno št.)\n"))

Pot = int(input("Želiš preizkusiti obarvljivost poti? \n"))
if Pot!=0:
    k2 = int(input("Željeno št. vozlišč poti: (vpiši naravno št.)\n"))

Cik = int(input("Želiš preizkusiti obarvljivost cikla? \n"))
if Cik!=0:
    k3 = int(input("Željeno št. vozlišč cikla: (vpiši naravno št.)\n"))

cnfji = input("Izpišem tudi CNF izrazov, ki predstavljajo obarvljivosti? (y/n)\n")
###########################
if Pet!=0:
    print(" \n{0} barvanje Petersenovega grafa".format(Pet) + "\n=================================\n")
    izraz = kbarvanje(Pet, 10, petersen)
    CNF = izraz.cnf()
    if cnfji=="y":
        print("CNF oblika: \n", CNF)
    mozno = dpll(CNF)
    if mozno!=0: 
        print("{0}-barvanje je možno, med drugim na naslednji način: \n".format(Pet), HumanFriendlyVersion(mozno)) 
    else: 
        print("{0}-barvanje ni možno!\n".format(Pet))

if Gro!=0:
    print(" \n{0} barvanje Grotzchevega grafa".format(Gro) + "\n=================================\n")
    izraz = kbarvanje(Gro, 11, grotzch) 
    CNF = izraz.cnf()
    if cnfji=="y":
        print("CNF oblika: \n", CNF)
    mozno = dpll(CNF)
    if mozno!=0: 
        print("{0}-barvanje je možno, med drugim na naslednji način: \n".format(Gro), HumanFriendlyVersion(mozno))
    else: 
        print("{0}-barvanje ni možno!\n".format(Gro))

if Poln!=0:
    print(" \n{0} barvanje polnega grafa".format(Poln) + "\n=================================\n")
    izraz = kbarvanje(Poln, k1, polnigraf(k1)) 
    CNF = izraz.cnf()
    if cnfji=="y":
        print("CNF oblika: \n", CNF)
    mozno = dpll(CNF)
    if mozno!=0: 
        print("{0}-barvanje je možno, med drugim na naslednji način: \n".format(Poln), HumanFriendlyVersion(mozno))
    else: 
        print("{0}-barvanje ni možno!\n".format(Poln))

if Pot!=0:
    print(" \n{0} barvanje poti".format(Pot) + "\n=================================\n")
    izraz = kbarvanje(Pot, k2, pot(k2))
    CNF = izraz.cnf()
    if cnfji=="y":
        print("CNF oblika: \n", CNF)
    mozno = dpll(CNF)
    if mozno!=0:
        print("{0}-barvanje je možno, med drugim na naslednji način: \n".format(Pot), HumanFriendlyVersion(mozno))
    else:
        print("{0}-barvanje ni možno!\n".format(Pot))

if Cik!=0:
    print(" \n{0} barvanje cikla".format(Cik) + "\n=================================\n")
    izraz = kbarvanje(Cik, k3, cikel(k3))
    CNF = izraz.cnf()
    if cnfji=="y":
        print("CNF oblika: \n", CNF)
    mozno = dpll(CNF)
    if mozno!=0:
        print("{0}-barvanje je možno, med drugim na naslednji način: \n".format(Cik), HumanFriendlyVersion(mozno))
    else:
        print("{0}-barvanje ni možno!\n".format(Cik))




