#   testni primeri
from Vaje1in2 import *
from dpll import *

x=Spr('x')
y=Spr('y')
z=Spr('z')
u=Spr('u')
primer1=Ali(In(x, y), In(z, u))

primer2=In(x)
primer3=In()
primer4=Ali(In(x, y, z), In(x))
primer5=In(Ali(x, y), Ali(u)) #tolko da dela dpll na dolžino 1
primer6=Ali(x,y,z)
primer7=Ali(x,y)
