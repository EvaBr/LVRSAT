class T():
    def __init__(self):
        pass

    def __repr__(self):
        return "⊤"

    def __eq__(self,other):
        return type(other)==T

    def __hash__(self):
        return hash(repr(self))

    def vrednost(self,slo):
        return True

    def poenostavi(self):
        return self

    def cnfconvert(self):
            return self
###################################################
class F():
    def __init__(self):
        pass

    def __repr__(self):
        return "⊥"
    
    def __eq__(self,other):
        return type(other)==F

    def __hash__(self):
        return hash(repr(self))

    def vrednost(self,slo):
        return False

    def poenostavi(self):
        return self

    def cnfconver(self):
        return self

###################################################
class Spr():
    def __init__(self,ime):
        self.ime=ime

    def __repr__(self):
        return self.ime

    def __eq__(self,other):
        if type(other)==Spr:
            return self.ime==other.ime
        else:
            return False

    def __hash__(self):
        return hash(repr(self))

    def vrednost(self,slo):
        return slo[self.ime]

    def poenostavi(self):
        return self

    def cnfconvert(self):
        return self

    
######################################################
class Neg():
    def __init__(self,izr):
        self.izr = izr

    def __repr__(self):
        return "¬"+repr(self.izr)

    def __eq__(self,other):
        if type(other) == Neg:
            return self.izr==other.izr
        else:
            return False
    
    def __hash__(self):
        return hash(repr(self))

    def vrednost(self,slo):
        return not self.izr.vrednost(slo)

    def poenostavi(self):
        a = self.izr.poenostavi()
        tip = type(a)
        if tip == T:
            return F()
        elif tip == F:
            return T()
        elif tip == Spr:
            return Neg(a)
        elif tip == Neg:
            return a.izr
        elif tip == In:
            return Ali(*tuple(Neg(i) for i in a.sez)).poenostavi()
        elif tip == Ali:
            return In(*tuple(Neg(i) for i in a.sez)).poenostavi()

    def cnfconvert(self):
        a = self.izr.cnfconvert()
        tip = type(a)
        if tip == T:
            return F()
        elif tip == F:
            return T()
        elif tip == Spr:
            return Neg(a)
        elif tip == Neg:
            return a.izr
        elif tip == In:
            return Ali(*tuple(Neg(i) for i in a.sez)).cnfconvert()
        elif tip == Ali:
            return In(*tuple(Neg(i) for i in a.sez)).cnfconvert()


#####################################################
class In():
    def __init__(self,*args):
        self.sez=set(args)

    def __repr__(self):
        niz=""
        for i in self.sez:
            niz+=" ∧ "+repr(i)

        return "("+niz[3:]+")"

    def __eq__(self,other):
        if type(other)==In:
            return self.sez==other.sez
        else:
            return False
    
    def __hash__(self):
        return hash(repr(self))

    def vrednost(self,slo):
        a=True
        for i in self.sez:
            a= a and i.vrednost(slo)
            if a==False:
                return a
        return a

    def poenostavi(self):
        if len(self.sez)==0: return T()
        elif len(self.sez)==1: return self.sez.pop().poenostavi()
        slo = {}
        for i in self.sez:
            i=i.poenostavi()
            if type(i)==F: return F()
            elif type(i)==T: pass
            elif type(i) in slo:
                slo[type(i)].add(i)
            else:
                slo[type(i)]={i}

        #complementary law
        if Neg in slo:
            for i in slo[Neg]:
                for j in slo.values():
                    if i.izr in j:
                        return F()

        #absorpcija in common identities
        if Ali in slo:
            menjave={}
            for i in slo[Ali]:
                for j in slo.values():
                    for k in j:
                        if k in i.sez:
                            menjave[i]=0
                        elif Neg(k) in i.sez:
                            menjave[i]=i.sez-{Neg(k)}
            slo[Ali]={(Ali(*tuple(menjave[i])) if menjave[i]!=0 else None )if i in menjave else i for i in slo[Ali]} - {None}
        
        #distributivnost

        if In in slo:
            for j in slo[In]:
                for i in j.sez:
                    if type(i) in slo: slo[type(i)].add(i)
                    else: slo[type(i)]={i}
      
            del slo[In]
        
        mn=set()
        for i in slo.values():
            mn|=i
        return In(*tuple(mn))
    
    def cnfconvert(self):
        if len(self.sez)==0: return T()
        elif len(self.sez)==1: return self.sez.pop().cnfconvert()
        slo = {}
        for i in self.sez:
            i=i.cnfconvert()
            if type(i)==F: return F()
            elif type(i)==T: pass
            elif type(i) in slo:
                slo[type(i)].add(i)
            else:
                slo[type(i)]={i}

        #complementary law
        if Neg in slo:
            for i in slo[Neg]:
                for j in slo.values():
                    if i.izr in j:
                        return F()

        #absorpcija in common identities
        if Ali in slo:
            menjave={}
            for i in slo[Ali]:
                for j in slo.values():
                    for k in j:
                        if k in i.sez:
                            menjave[i]=0
                        elif Neg(k) in i.sez:
                            menjave[i]=i.sez-{Neg(k)}
            slo[Ali]={(Ali(*tuple(menjave[i])) if menjave[i]!=0 else None )if i in menjave else i for i in slo[Ali]} - {None}
        
        #distributivnost

        if In in slo:
            for j in slo[In]:
                for i in j.sez:
                    if type(i) in slo: slo[type(i)].add(i)
                    else: slo[type(i)]={i}
      
            del slo[In]
        
        mn=set()
        for i in slo.values():
            mn|=i
        return In(*tuple(mn))
    
########################################################
class Ali():
    def __init__(self,*args):
        self.sez=set(args)

    def __repr__(self):
        niz=""
        for i in self.sez:
            niz+=" ∨ "+repr(i)

        return "("+niz[3:]+")"

    def __eq__(self,other):
        if type(other)==Ali:
            return self.sez==other.sez
        else:
            return None

    def __hash__(self):
        return hash(repr(self))

    def vrednost(self,slo):
        a=False
        for i in self.sez:
            a= a or i.vrednost(slo)
            if a==True:
                return a
        return a

    def poenostavi(self):
        if len(self.sez)==0: return F()
        elif len(self.sez)==1: return self.sez.pop().poenostavi()
        slo = {}
        for i in self.sez:
            i=i.poenostavi()
            if type(i)==T: return T()
            elif type(i)==F: pass
            elif type(i) in slo:
                slo[type(i)].add(i)
            else:
                slo[type(i)]={i}
        
        #complementary law
        if Neg in slo:
            for i in slo[Neg]:
                for j in slo.values():
                    if i.izr in j:
                        return T()

        #absorpcija in common identities in distributivnost
        if In in slo:
            menjave={}
            for i in slo[In]:
                for j in slo.values():
                    for k in j:
                        if k in i.sez: #absorpcija
                            menjave[i]=0
                        elif Neg(k) in i.sez: #common id
                            menjave[i]=i.sez-{Neg(k)}
            slo[In]={(In(*tuple(menjave[i])) if menjave[i]!=0 else None )if i in menjave else i for i in slo[In]} - {None}
        
            #distributivnost

       
        if Ali in slo:
            for j in slo[Ali]:
                for i in j.sez:
                    if type(i) in slo: slo[type(i)].add(i)
                    else: slo[type(i)]={i}
      
            del slo[Ali]

        mn=set()
        for i in slo.values():
            mn|=i
        return Ali(*tuple(mn))

    def cnfconvert(self):
        if len(self.sez)==0: return F()
        elif len(self.sez)==1: return self.sez.pop().cnfconvert()
        slo = {}
        for i in self.sez:
            i=i.cnfconvert()
            if type(i)==T: return T()
            elif type(i)==F: pass
            elif type(i) in slo:
                slo[type(i)].add(i)
            else:
                slo[type(i)]={i}
        
        #complementary law
        if Neg in slo:
            for i in slo[Neg]:
                for j in slo.values():
                    if i.izr in j:
                        return T()

        #absorpcija in common identities in distributivnost
        if In in slo:
            menjave={}
            for i in slo[In]:
                for j in slo.values():
                    for k in j:
                        if k in i.sez: #absorpcija
                            menjave[i]=0
                        elif Neg(k) in i.sez: #common id
                            menjave[i]=i.sez-{Neg(k)}
            slo[In]={(In(*tuple(menjave[i])) if menjave[i]!=0 else None )if i in menjave else i for i in slo[In]} - {None}
        
            #distributivnost

       
##        if Ali in slo:
##            for j in slo[Ali]:
##                for i in j.sez:
##                    if type(i) in slo: slo[type(i)].add(i)
##                    else: slo[type(i)]={i}
##      
##            del slo[Ali]

        mn=set()
        for i in slo.values():
            mn|=i
        return Ali(*tuple(mn))

primer1 = Ali(Spr("p"),In(Spr("q"),Spr("p")))

primer2 = In(Spr("p"),Ali(Spr("q"),Neg(Spr("p"))))

primer3 = In(Ali(Spr("p"),Spr("q")),Ali(Spr("p"),Spr("r")))




###################### VAJE ŠTEVILKA 2 ########################################################################
##
##
##def barvanje(g,k):
##    """Ali lahko graf podan s slovarjem g pobarvamo s k barvami? """
##    def sprem(v,b):
##        return Spr(str(v)+","+str(b))
##    
##    #vsako vozlišče vsaj ene barve
##    f1 = In(*tuple(Ali(*tuple(sprem(v,b) for b in range(k))) for v in g))
##
##    #vsako vozlišče z ne več kot eno barvo
##    f2 = In(
##        *tuple(
##            In(
##                *tuple(
##                    Neg(In(sprem(v,b1),sprem(v,b2)))
##                    for b1 in range(k-1)
##                    for b2 in range(b1+1,k))
##                )
##            for v in g))
##    
##    #povezani vozlišči različnih barv
##    f3 = In(
##        *tuple(
##            In(
##                *tuple(
##                    Neg(In(sprem(v1,b),sprem(v2,b)))
##                    for b in range(k)
##                    )
##                )
##            for v1 in g for v2 in g[v1]))
##
##    formula = In(f1,f2,f3)
##
##    return formula.poenostavi()
##
##g = {"a":{"d"},"b":{"d"},"c":{"d"},"d":{"a","b","c"}}
##
##########################################################################

#3COL

def barvanje(n, E):
    prva = T()
    druga = T()
    tretja = T()
    for i in range(1,n):
        prva = In(Ali(Spr("c{0}1".format(i)), Spr("c{0}2".format(i)), Spr("c{0}3".format(i))), prva)
    prva=prva.poenostavi()
    
    for i in range(1,n):
        druga = In(druga, In(Neg(In(Spr("c{0}1".format(i)),Spr("c{0}2".format(i)))),
                   Neg(In(Spr("c{0}1".format(i)),Spr("c{0}3".format(i)))),Neg(In(Spr("c{0}3".format(i)),Spr("c{0}2".format(i))))))
    druga=druga.poenostavi()
    
    for pov in E:
        tretja = In(tretja, In(Neg(In(Spr("c{0}1".format(pov[1])),Spr("c{0}1".format(pov[0])))),
                  Neg(In(Spr("c{0}2".format(pov[1])),Spr("c{0}2".format(pov[0])))),
        Neg(In(Spr("c{0}3".format(pov[1])),Spr("c{0}3".format(pov[0]))))))
    tretja=tretja.poenostavi()
    
    form = In(prva,druga,tretja)
    return form.poenostavi()

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
    
            

#SUDOKU
#sprejme seznam trojic zasedenih polj
#
#

def sudoku(zasedena):
    def sprem(k1,k2,v):
        return Spr(str(k1)+","+str(k2)+","+str(v))
    
    #vsako polje je pobarvano
    prvidel = In(*tuple(Ali(*tuple(sprem(i, j, k) for k in range(1,10)))
                        for i in range(1,10)
                        for j in range(1,10)))
    #return prvidel.poenostavi()


    #nobeno polje ni pobarvano z več kot eno barvo
    drugidel= In(*tuple(In(*tuple(Neg(In(sprem(i, j, k), sprem(i, j, l)))
                                  for l in range(1,10)
                                  for k in range(1,l)))
                        for i in range(1,10)
                        for j in range(1,10)))



    #return drugidel.poenostavi()

    #barva se ne ponovi v stolpcu
    tretjidel = In(*tuple(Neg(In(sprem(i,j,k),sprem(l,j,k)))
                   for j in range (1,10)
                   for k in range (1,10)
                   for i in range (1,10)
                   for l in range (i,10)))
    #return tretjidel.poenostavi()
    

    #barva se ne ponovi v vrstici
    cetrtidel = In(*tuple(Neg(In(sprem(i,j,k),sprem(i,l,k)))
                   for i in range (1,10)
                   for k in range (1,10)
                   for j in range (1,10)
                   for l in range (j,10)))
    #return cetrtidel.poenostavi()

    #barva se ne ponovi v 3x3 podkvadratu
    #for i in range (1,10,3)
    petidel = In(*tuple(In(*tuple(Neg(In(sprem(i,j,k),sprem(m,n,k)))
                                   for i in range (I,I+3)
                                   for j in range (J,J+3)
                                   for m in range (i,I+3)
                                   for n in range (j,J+3)
                                   for k in range (1,10)))
                        for I in range (1,10,3)
                        for J in range (1,10,3)))
    #return petidel.poenostavi()


    #preverjanje ali je izpolnjeno zacetno stanje
    sestidel = In(*tuple(sprem(i[0],i[1],i[2]) for i in zasedena))
    return sestidel.poenostavi()
                   






#######################################################################
# vaje 4 - pretvorba v CNF

def cnfconvert(p):
    p1=p.poenostavi()
    #najprej potisnemo negacije do atomov; to naredi poenostavi
    #iz fomle izluscimo posamezne stavke
    stavki=[]
    
    

#implementacija DPLL
#def dpll(formula):
##    # formula je seznam stavkov
##    if formula == []:
##        return T()
##    else:
##        for clause in formula:
##            if clause == []:
##                return ()
##            elif length(clause)==1:
##                vrednost = clause(1)
##                #nastavi vrednost spremenljivke
##    


