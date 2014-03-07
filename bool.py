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
        elif len(self.sez)==1: return self.sez[0]
        slo = {}
        for i in self.sez:
            if type(i)==F: return F()
            elif type(i)==T: pass
            elif type(i) in slo:
                slo[type(i)].add(i.poenostavi())
            else:
                slo[type(i)]={i.poenostavi()}

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
        elif len(self.sez)==1: return self.sez[0]
        slo = {}
        for i in self.sez:
            if type(i)==T: return T()
            elif type(i)==F: pass
            elif type(i) in slo:
                slo[type(i)].add(i.poenostavi())
            else:
                slo[type(i)]={i.poenostavi()}

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
                
                

        mn=set()
        for i in slo.values():
            mn|=i
        return Ali(*tuple(mn))

primer1 = Ali(Spr("p"),In(Spr("q"),Spr("p")))

primer2 = In(Spr("p"),Ali(Spr("q"),Neg(Spr("p"))))

primer3 = In(Ali(Spr("p"),Spr("q")),Ali(Spr("p"),Spr("r")))
















    
