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

x=Spr('x')
y=Spr('y')
z=Spr('z')
w=Spr('w')

primer1 = Ali(x, y, z)
print('===== Primer 1 =====')
print (primer1)
print (primer1.cnf())
print(dpll(primer1.cnf()))

primer2 = Ali(x, y, In(z,w))
print('===== Primer 2 =====')
print (primer2)
print (primer2.cnf())
print (dpll(primer2.cnf()))

primer3 = In(x, y, z)
print('===== Primer 3 =====')
print (primer3)
print (primer3.cnf())
print (dpll(primer3.cnf()))

primer4 = In(x, Ali(x, y))
print('===== Primer 4 =====')
print (primer4)
print (primer4.cnf())
print (dpll(primer4.cnf()))

primer5 = Ali(In(x, y), In(z, w))
print('===== Primer 5 =====')
print (primer5)
print (primer5.cnf())
print (dpll(primer5.cnf()))

primer6 = In(Ali(x, y), Ali(z, w))
print('===== Primer 6 =====')
print (primer6)
print (primer6.cnf())
print (dpll(primer6.cnf()))

primer7 = In(In(x, y), Ali(z, w))
print('===== Primer 7 =====')
print (primer7)
print (primer7.cnf())
print (dpll(primer7.cnf()))

primer8 = In(x, Neg(x))
print('===== Primer 8 =====')
print (primer8)
print (primer8.cnf())
print (dpll(primer8.cnf()))

primer9 = Ali(x, Neg(x))
print('===== Primer 9 =====')
print (primer9)
print (primer9.cnf())
print (dpll(primer9.cnf()))

primer10 = Neg(In(x, y))
print('===== Primer 10 =====')
print (primer10)
print (primer10.cnf())
print (dpll(primer10.cnf()))

primer11 = In(x, Ali(Neg(x), y))
print('===== Primer 11 =====')
print (primer11)
print (primer11.cnf())
print (dpll(primer11.cnf()))

primer12 = x
print('===== Primer 12 =====')
print (primer12)
print (primer12.cnf())
print (dpll(primer12.cnf()))

#preverjanje dpll: primer brez čiste pojavitve
primer13 = Ali(In(x, y), Neg(x), Neg(y))
print('===== Primer 13 =====')
print (primer13)
print (primer13.cnf())
print (dpll(primer13.cnf()))

#preverjanje dpll: primer brez čiste pojavitve in brez stavkov dolžine 1
primer14 = Ali(In(x, y), In(Neg(x), Neg(y)))
print('===== Primer 14 =====')
print (primer14)
print (primer14.cnf())
print (dpll(primer14.cnf()))

#dolga čudna izpolnjiva formula :D
primer15 = Ali(In(Ali(Neg(x), y, z), In(x, w), z), Ali(w, Neg(z), Neg(w)), z, x)
print('===== Primer 15 =====')
print (primer15)
print (primer15.cnf())
print (dpll(primer15.cnf()))

primer16 = In(x)
print('===== Primer 16 =====')
print (primer16)
print (primer16.cnf())
print (dpll(primer16.cnf()))

primer17 = In()
print('===== Primer 17 =====')
print (primer17)
print (primer17.cnf())
print (dpll(primer17.cnf()))

primer18 = Ali()
print('===== Primer 18 =====')
print (primer18)
print (primer18.cnf())
print (dpll(primer18.cnf()))

primer19 = In(Ali(x, Neg(y), Neg(z)), Ali(Neg(x), y), Ali(x, z))
print('===== Primer 19 =====')
print (primer19)
print (primer19.cnf())
print (dpll(primer19.cnf()))

#dolga čudna neizpolnjiva formula :D
primer20 = In(Neg(x), y, Neg(Ali(z, Neg(w))), Neg(In(w, z)), Neg(Ali(w, y)))
print('===== Primer 20 =====')
print (primer20)
print (primer20.cnf())
print (dpll(primer20.cnf()))

primer21 = Neg(Ali(x, y))
print('===== Primer 21 =====')
print (primer21)
print (primer21.cnf())
print (dpll(primer21.cnf()))


primer22 = In(Neg(x), y, Ali(x, Neg(z), In(z, x, Neg(y))))
print('===== Primer 22 =====')
print (primer22)
print (primer22.cnf())
print (dpll(primer22.cnf()))

primer23 = In(Neg(x), y, Ali(x, y, Neg(z), In(z, x, Neg(y))))
print('===== Primer 23 =====')
print (primer23)
print (primer23.cnf())
print (dpll(primer23.cnf()))
