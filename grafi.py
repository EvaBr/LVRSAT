##################################################################
#
#           Nekaj primerov grafov, za preizkušanje barvanj.
#
# Vse funkcije sprejmejo število vozlišč n in vrnejo seznam povezav, ki
# jih ima graf želene oblike na n vozliščih.
#
##################################################################

from barvanje import *
from dpll import*
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
