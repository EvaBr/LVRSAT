#
#TESTNI PRIMERI
#
#Testni primeri za preizkusanje delovanja pretvorbe v CNF
#obliko in resevanja z DPLL.
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

xx=Lit('x')
yy=Lit('y')
zz=Lit('z')
ww=Lit('w')

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

##primer3=In(x,y,z)
##print('===== Primer 3 =====')
##print (primer3)
##print (primer3.cnf())
##print (dpll(primer3))

primer4=In(x, Ali(x,y))
print('===== Primer 4 =====')
print (primer4)
print (primer4.cnf())
print (dpll(primer4))

##primer5= Ali(In(x,y), In(z,w))
##print('===== Primer 5 =====')
##print (primer5)
##print (primer5.cnf())
##print (dpll(primer5))

##primer6=In(Ali(x,y), Ali(z,w))
##print('===== Primer 6 =====')
##print (primer6)
##print (primer6.cnf())
##print (dpll(primer6))

##primer7=In(In(x,y), Ali(z,w))
##print('===== Primer 7 =====')
##print (primer7)
##print (primer7.cnf())
##print (dpll(primer7))

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

##primer10=Neg(In(x,y))
##print('===== Primer 10 =====')
##print (primer10)
##print (primer10.cnf())
##print (dpll(primer10))

##primer11=In(x, Ali(Neg(x), y))
##print('===== Primer 11 =====')
##print (primer11)
##print (primer11.cnf())
##print (dpll(primer11))

primer12=x
print('===== Primer 12 =====')
print (primer12)
print (primer12.cnf())
print (dpll(primer12))

