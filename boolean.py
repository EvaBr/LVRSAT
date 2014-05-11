from cnf import *

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
        return T()

    def nnf(self, negiramo=False):
        if negiramo:
            return F()
        else:
            return T()

    def cnf(self):
            return Cnf([])
        
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
        return F()

    def nnf(self, negiramo=False):
        if negiramo:
            return T()
        else:
            return F()

    def cnf(self):
            return Cnf([Stavek([])])

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
        return Spr(self.ime)
    
    def nnf(self, negiramo=False):
        """Vrne nnf obliko objekta self."""
        if negiramo:
            return Neg(Spr(self.ime))
        else:
            return Spr(self.ime)

    def cnf(self):
        """Vrne CNF obliko objekta self."""
        return Cnf([Stavek([Lit(self.ime)])])
    
    
######################################################
class Neg():
    def __init__(self,izr):
        self.izr = izr

    def __repr__(self):
        return "¬" + repr(self.izr)

    def __eq__(self,other):
        if type(other)==Neg:
            return self.izr==other.izr
        else:
            return False
    
    def __hash__(self):
        return hash(repr(self))

    def vrednost(self,slo):
        return not self.izr.vrednost(slo)

    def poenostavi(self):
        notr = self.izr.poenostavi()
        tip = type(notr)
        if tip==T:
            return F()
        elif tip==F:
            return T()
        elif tip==Spr:
            return Neg(notr)
        elif tip==Neg:
            return notr.izr
        elif tip==In:
            return Ali(*tuple(Neg(i) for i in notr.sez)).poenostavi()
        elif tip==Ali:
            return In(*tuple(Neg(i) for i in notr.sez)).poenostavi()
        
    def nnf(self, negiramo=False):
        notr = self.izr.poenostavi()
        tip = type(notr)
        if tip==T:
            return F()
        elif tip==F:
            return T()
        elif tip==Spr:
            return Neg(notr)
        elif tip==Neg:
            return notr.izr
        elif tip==In:
            return Ali(*tuple(Neg(i) for i in notr.sez))
        elif tip==Ali:
            return In(*tuple(Neg(i) for i in notr.sez))

    def cnf(self):
        if isinstance(self.izr, Spr):
            return Cnf([Stavek([Til(self.izr.ime)])])
        else:
            return self.nnf().cnf()
        
##########################################################################
class In():
    def __init__(self,*args):
        self.sez = list(args)

    def __repr__(self):
        niz = ""
        for i in self.sez:
            niz += " ∧ " + repr(i)
        if len(self.sez)==1:
            return niz[3:]
        return "(" + niz[3:] + ")"

    def __eq__(self,other):
        if type(other)==In:
            return self.sez==other.sez
        else:
            return False
    
    def __hash__(self):
        return hash(repr(self))

    def vrednost(self,slo):
        vr = True
        for i in self.sez:
            vr = vr and i.vrednost(slo)
            if vr==False:
                return False
        return vr

    def poenostavi(self):
        if len(self.sez)==0: 
            return T()
        elif len(self.sez)==1: 
            return self.sez.pop().poenostavi()
        slo = {}
        for i in self.sez:
            i = i.poenostavi()
            if type(i)==F: 
                return F()
            elif type(i)==T: 
                pass   
            elif type(i) in slo:
                slo[type(i)].add(i)
            else:
                slo[type(i)]={i}

        #Znebimo se In-a v In-u:
        if In in slo:
            for j in slo[In]:
                for i in j.sez:
                    if type(i) in slo: 
                        slo[type(i)].add(i)
                    else: 
                        slo[type(i)] = {i}
            del slo[In]

        #Complementary law:
        if Neg in slo:
            for i in slo[Neg]:
                for j in slo.values():
                    if i.izr in j:
                        return F()

        #Absorp., common ident.:
        if Ali in slo:
            menjave = {}
            for i in slo[Ali]:
                for j in slo.values():
                    for k in j:
                        if k in i.sez:
                            menjave[i] = 0
                        elif Neg(k) in i.sez:
                            menjave[i] = set(i.sez)-{Neg(k)}
            slo[Ali]={(Ali(*tuple(menjave[i])) if menjave[i]!=0 else None )if i in menjave else i for i in slo[Ali]} - {None}
                    
        mn = set()
        for i in slo.values():
            mn |= i
        konc = In(*tuple(mn))

        if len(konc.sez)==0:
            return T()
        elif len(konc.sez)==1:
            return konc.sez[0]
        else:
            return konc


    def nnf(self, negiramo=False):
        lst = [p.nnf(negiramo) for p in self.sez]
        if negiramo:
            return Ali(lst)
        else:
            return In(lst)

    def cnf(self):
        stavki = []
        for p in self.sez:
            dodamo = [i for i in p.cnf().stavki if i not in stavki]
            stavki.extend(dodamo)
        return Cnf(stavki)
    
##########################################################################
class Ali():
    def __init__(self, *args):
        self.sez = list(args)

    def __repr__(self):
        niz = ""
        for i in self.sez:
            niz += " ∨ " + repr(i)
        if len(self.sez)==1:
            return niz[3:]
        else:
            return "(" + niz[3:] + ")"

    def __eq__(self,other):
        if type(other)==Ali:
            return self.sez==other.sez
        else:
            return None

    def __hash__(self):
        return hash(repr(self))

    def vrednost(self,slo):
        vr = False
        for i in self.sez:
            vr = vr or i.vrednost(slo)
            if vr==True:
                return True
        return vr

    def poenostavi(self):
        if len(self.sez)==0: 
            return F()
        elif len(self.sez)==1: 
            return self.sez.pop().poenostavi()
        slo = {}
        for i in self.sez:
            i = i.poenostavi()
            if type(i)==T: 
                return T()
            elif type(i)==F: 
                pass
            elif type(i) in slo:
                slo[type(i)].add(i)
            else:
                slo[type(i)] = {i}

        #Znebimo se Ali-ja v Ali-ju:
        if Ali in slo:
            for j in slo[Ali]:
                for i in j.sez:
                    if type(i) in slo: 
                        slo[type(i)].add(i)
                    else: 
                        slo[type(i)] = {i}
            del slo[Ali]
        
        #Complementary law:
        if Neg in slo:
            for i in slo[Neg]:
                for j in slo.values():
                    if i.izr in j:
                        return T()

        #Absorpcija, common ids in distributivnost:
        if In in slo:
            menjave = {}
            for i in slo[In]:
                for j in slo.values():
                    for k in j:
                        if k in i.sez:
                            menjave[i] = 0
                        elif Neg(k) in i.sez:
                            menjave[i] = set(i.sez)-{Neg(k)}
            slo[In] = {(In(*tuple(menjave[i])) if menjave[i]!=0 else None) if i in menjave else i for i in slo[In]} - {None}
        
        #DODAJ DISTRIBUTIVNOST!
       
        mn = set()
        for i in slo.values():
            mn |= i
        return Ali(*tuple(mn))

    def nnf(self, negiramo=False):
        lst = [p.nnf(negiramo) for p in self.sez]
        if negiramo:
            return In(lst)
        else:
            return Ali(lst)
        
    def cnf(self):
        if len(self.sez)==0:
            return Cnf([Stavek([])])
        elif len(self.sez)==1:
            return self.sez[0].cnf()
        else:
            # Razbijemo disjunkcijo na dve podformuli in izracunamo CNF
            stavki = []
            for s1 in self.sez[0].cnf().stavki:
                for i in self.sez[1:]:
                    if i==self.sez[1]:
                        pom = i
                    else:
                        pom = Ali(pom,i)
                for s2 in pom.cnf().stavki:
                    stavki.append(Stavek(s1.literali + s2.literali))
                    
            return Cnf(stavki)
