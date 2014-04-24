#
#TESTNI PRIMERI
#
#Testni primeri za preizkusanje delovanja pretvorbe v CNF
#obliko in resevanja z DPLL. Vključeni so primeri preprostih
#formul v različnih osnovnih možnih kombinacijah stavkov 'In',
#'Ali', negacij ter možnih praznih stavkov/formul.
#
##########################################################

from boolean import *
from cnf import *
from dpll import *
from sudoku import *
from barvanje import *

x=Spr('x')
y=Spr('y')
z=Spr('z')
w=Spr('w')

primer1=Ali(x,y,z)
print('===== Primer 1 =====')
print (primer1)
print (primer1.cnf())
print(dpll(primer1))

primer2=Ali(x, y, In(z,w))
print('===== Primer 2 =====')
print (primer2)
print (primer2.cnf())
print (dpll(primer2))

primer3=In(x,y,z)
print('===== Primer 3 =====')
print (primer3)
print (primer3.cnf())
print (dpll(primer3))

primer4=In(x, Ali(x,y))
print('===== Primer 4 =====')
print (primer4)
print (primer4.cnf())
print (dpll(primer4))

primer5= Ali(In(x,y), In(z,w))
print('===== Primer 5 =====')
print (primer5)
print (primer5.cnf())
print (dpll(primer5))

primer6=In(Ali(x,y), Ali(z,w))
print('===== Primer 6 =====')
print (primer6)
print (primer6.cnf())
print (dpll(primer6))

primer7=In(In(x,y), Ali(z,w))
print('===== Primer 7 =====')
print (primer7)
print (primer7.cnf())
print (dpll(primer7))

primer8=In(x, Neg(x))
print('===== Primer 8 =====')
print (primer8)
print (primer8.cnf())
print (dpll(primer8))

primer9=Ali(x, Neg(x))
print('===== Primer 9 =====')
print (primer9)
print (primer9.cnf())
print (dpll(primer9))

primer10=Neg(In(x,y))
print('===== Primer 10 =====')
print (primer10)
print (primer10.cnf())
print (dpll(primer10))

primer11=In(x, Ali(Neg(x), y))
print('===== Primer 11 =====')
print (primer11)
print (primer11.cnf())
print (dpll(primer11))

primer12=x
print('===== Primer 12 =====')
print (primer12)
print (primer12.cnf())
print (dpll(primer12))

#preverjanje dpll: primer brez čiste pojavitve
primer13=Ali(In(x,y), Neg(x), Neg(y))
print('===== Primer 13 =====')
print (primer13)
print (primer13.cnf())
print (dpll(primer13))

#preverjanje dpll: primer brez čiste pojavitve in brez stavkov dolžine 1
primer14=Ali(In(x,y), In(Neg(x), Neg(y)))
print('===== Primer 14 =====')
print (primer14)
print (primer14.cnf())
print (dpll(primer14))

#dolga čudna izpolnjiva formula :D
primer15=Ali(In(Ali(Neg(x),y,z),In(x,w),z),Ali(w,Neg(z),Neg(w)),z,x)
print('===== Primer 15 =====')
print (primer15)
print (primer15.cnf())
print (dpll(primer15))

primer16=In(x)
print('===== Primer 16 =====')
print (primer16)
print (primer16.cnf())
print (dpll(primer16))

primer17=In()
print('===== Primer 17 =====')
print (primer17)
print (primer17.cnf())
print (dpll(primer17))

primer18=Ali()
print('===== Primer 18 =====')
print (primer18)
print (primer18.cnf())
print (dpll(primer18))

primer19=In(Ali(x, Neg(y), Neg(z)), Ali(Neg(x), y), Ali(x,z))
print('===== Primer 19 =====')
print (primer19)
print (primer19.cnf())
print (dpll(primer19))

#dolga čudna neizpolnjiva formula :D
primer20=In(Neg(x), y, Neg(Ali(z, Neg(w))), Neg(In(w,z)), Neg(Ali(w, y)))
print('===== Primer 20 =====')
print (primer20)
print (primer20.cnf())
print (dpll(primer20))

primer21=Neg(Ali(x,y))
print('===== Primer 21 =====')
print (primer21)
print (primer21.cnf())
print (dpll(primer21))
