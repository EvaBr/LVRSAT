################################################################################
#                                   Hadamard                                   #
#                                   spremeni                                   #
#  Funkcija sprejme seznam trojic in vrne formulo za sudoku.                   #
#                                                                              #
#  Primer uporabe: sudoku([(1,1,9),(1,2,2),(3,4,5)])                           #
#                                                                              #
#  V vsaki trojici prvi števili predstavlja indeksa vrstice in stolpca,        #
#    tretje pa število v tem polju. Vsako število mora biti iz množice         #
#    {1,2,3,4,5,6,7,8,9}                                                       #
#                                                                              #
#  Funkcija ne preverja ali so v seznamu, ki ga prejme kot parameter, števila  #
#    med 1 in 9.                                                               #
#                                                                              #
################################################################################

from boolean import *

#HADAMARD
#Xij elementi matrike
##def hadamard(n):
##    if n%2==1:
##        return F()
##    for j in range (2,n): #stolpec1
##        for i in range (1,j): #stolpec2
##            vektor = {}
##            for st in range(1,n):
##                vektor["prod{0}".format(st)] = In(Spr("X{0}{1}".format(i,st)), Spr("X{0}{1}".format(j,st))) #V vektorju maš pol skalarni prod. stolpcev i in j
##            Spr("C1,0")= Neg(vektor["prod1"])
##            Spr("C{0},{1}".format(n, n/2)) = Ali(In(Spr("C{0}{1}".format(n-1, n/2)), Neg(vektor["prod{0}".format(n)])),In(vektor["prod{0}".format(n)],Spr("C{0}{1}".format(n-1, n/2-1))))
##            if Spr("C{0}{1}".format(n,n/2))==F():
##                return F()
