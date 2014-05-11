################################################################################
#                                   Hadamard                                   #
#                                                                              #
#  Funkcija sprejme naravno število n in vrne logično formulo za SAT problem   #
#  (ali obstaja Hadamardova matrika n x n).                                    #
#									       #
#  Primer uporabe: hadamard(5)                                                 #
#                                                                              #
#                                                                              #
################################################################################

from boolean import *


def s(m,k):
    niz = "X({0}, {1})".format(m, k)
    return Spr(niz)

def n(m,k):
    niz = "X({0}, {1})".format(m, k)
    return Neg(Spr(niz))


#Xij elementi matrike; Xij == T(), ce je na tem polju 1.
def hadamard(N):

    def prod(i, j, a=N, b=N//2):
        #Vrne T(), ce je skal prod i-tega in j-tega stolpca enak 0.
        if a<b:
            return F()
        elif a==1 and b==0:
            return Ali(n(1,i), n(1,j))
        elif a==1 and b==1: 
            return In(s(1,i), s(1,j))
        elif b==0: #and a>1
            return In(prod(i, j, a-1, 0), Ali(n(a,i), n(a,j)))
        else: #a>=b, b>0,  
            return Ali(In(prod(i, j, a-1, b-1), s(a,i), s(a,j)), In(prod(i, j, a-1, b), Ali(n(a,i), n(a,j))))

    # Bi rekla, da je tole sehr kurz und elegantisch :P, aber Piton posredno
    # pravi "RuntimeError", ko dozivi katarzo ze med racunanjem za n=10. 
    #
    # Dejmo bit torej malo bolj dinamicni in prostorsko potratni:
    #
    #prod = [Ali(n(1,i), n(1,j)), In(s(1,i), s(1,j))]+[0]*... Se pride...

    if N%2==1:
        return F()
    else:
        return In(*tuple(prod(i, j) for i in range(2, N+1) for j in range(1, i)))
