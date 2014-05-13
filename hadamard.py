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

def xor(A, B): #Potrebujemo ekskluzivni ali, saj 1*1 = 1 = T, in hkrati -1*-1 = 1 = T.
    return Ali(In(A, Neg(B)), In(Neg(A), B))

def equiv(A, B): #Ekvivalenca je negacija xor-a.
    return In(Ali(Neg(A), B), Ali(A, Neg(B)))



#Xij elementi matrike; Xij == T(), ce je na tem polju 1 in F(), ce je tam -1.
def hadamard(N):

    def prod(i, j, a, b):
        #Vrne T(), ce je skal prod i-tega in j-tega stolpca enak 0.
        if a<b:
            return F()
        elif a==1 and b==0:
            return xor(s(1,i), s(1,j))
        elif a==1 and b==1: 
            return equiv(s(1,i), s(1,j))
        elif b==0: #and a>1
            return In(prod(i, j, a-1, 0), xor(s(a,i), s(a,j)))
        else: #a>=b, b>0,  
            return Ali(In(prod(i, j, a-1, b-1), equiv(s(a,i), s(a,j))), In(prod(i, j, a-1, b), xor(s(a,i), s(a,j))))

    if N<=0:
        return "Haha, you are so funny."
    elif N==1:
        return s(1,1)
    elif N%2==1:
        return F()
    else:
        return In(*tuple(prod(i, j, N, N//2) for i in range(2, N+1) for j in range(1, i)))



# Bi rekla, da je tole sehr kurz und elegantisch :P, aber Piton posredno
# pravi "RuntimeError", ko dozivi katarzo ze med racunanjem za n=10. 
#
# Dejmo bit torej malo bolj dinamicni in prostorsko potratni, morda bo hitreje:
    
def hadamard2(n):

    def C(i,j,N):
        #Za vsaka dva razl. stolpca izracunamo C_{n,n/2}.
        pol = N//2
        prod = [xor(s(1,i), s(1,j)), equiv(s(1,i), s(1,j))] + [F()]*(pol-1) #Prva vrsta. pol+1 stolpcev.
        for vrsta in range(2, N): #V zadnji, n-ti vrsti bomo izacunali le zeljeno mesto.
            for stolp in range(min(vrsta,pol), 0, -1): #0-to mesto posebej, ker je druga formula.
                prod[stolp] = Ali(In(prod[stolp-1], equiv(s(vrsta,i), s(vrsta,j))), In(prod[stolp], xor(s(vrsta,i), s(vrsta,j))))
            prod[0] = In(prod[0], xor(s(vrsta,i), s(vrsta,j)))
        #Zadnja vrstica - vrsta=N: potrebujemo le stvar na N//2-tem mestu...
        C = Ali(In(prod[pol-1], equiv(s(N,i), s(N,j))), In(prod[pol], xor(s(N,i), s(N,j))))
        return C

    if n<=0:
        return "Haha, you are so funny."
    elif n==1:
        return s(1,1)
    elif n%2==1:
        return F()
    else:
        return In(*tuple(C(i,j,n) for i in range(2, n+1) for j in range(1,i)))        


# Potrata casa: hadamard(10) 4sec, in hadamard2(10) 0.18 sec! WIN :D
