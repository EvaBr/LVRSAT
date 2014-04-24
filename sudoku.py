################################################################################
#                                   Sudoku                                     #
#                                                                              #
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

def sudoku(zasedena):
    def sprem(k1,k2,v):
        return Spr(str(k1)+","+str(k2)+","+str(v))
    
    #vsako polje je pobarvano
    prvidel = In(*tuple(Ali(*tuple(sprem(i, j, k) for k in range(1,10)))
                        for i in range(1,10)
                        for j in range(1,10)))
    
    #nobeno polje ni pobarvano z več kot eno barvo
    drugidel= In(*tuple(In(*tuple(Neg(In(sprem(i, j, k), sprem(i, j, l)))
                                  for l in range(1,10)
                                  for k in range(1,l)))
                        for i in range(1,10)
                        for j in range(1,10)))

    #barva se ne ponovi v stolpcu
    tretjidel = In(*tuple(Neg(In(sprem(i,j,k),sprem(l,j,k)))
                   for j in range (1,10)
                   for k in range (1,10)
                   for i in range (1,10)
                   for l in range (i,10)))
    
    #barva se ne ponovi v vrstici
    cetrtidel = In(*tuple(Neg(In(sprem(i,j,k),sprem(i,l,k)))
                   for i in range (1,10)
                   for k in range (1,10)
                   for j in range (1,10)
                   for l in range (j,10)))
    #return cetrtidel.poenostavi()

    #barva se ne ponovi v 3x3 podkvadratu
    petidel = In(*tuple(In(*tuple(Neg(In(sprem(i,j,k),sprem(m,n,k)))
                                   for i in range (I,I+3)
                                   for j in range (J,J+3)
                                   for m in range(I,I+3)
                                   for n in range (J,J+3)
                                   if not (i==m and j==n)
                                   for k in range (1,10)))
                        for I in range (1,10,3)
                        for J in range (1,10,3)))
    
    #ali je izpolnjeno zacetno stanje
    sestidel = In(*tuple(sprem(i[0],i[1],i[2]) for i in zasedena))

    return In(prvidel,drugidel,tretjidel,cetrtidel,petidel,sestidel)
