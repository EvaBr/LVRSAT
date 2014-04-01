#implementacija DPLL

from Vaje1in2 import *
from cnf import *

def dpll(formula, slovar={}):
    formula=formula.cnf()
    if formula == []:
        return T()
    else:
        for stavek in formula.stavki:
            if stavek == []:
                return F()
            elif len(stavek.literali)==1:
                spremenljivka = stavek.literali[0]
                #nastavi vrednost spremenljivke
                if type(spremenljivka)==Neg:
                    spr2=Neg(spremenljivka).nnf()
                    if (spr2 in slovar and slovar[spr2]==F()): pass
                    elif (spr2 in slovar and slovar[spr2]==T()):
                        return ('Formula ni izpolnjiva')
                    else: slovar[spr2]=F()
                else:
                    if (spremenljivka in slovar and slovar[spremenljivka]==T()):
                        pass
                    elif (spremenljivka in slovar and slovar[spr2]==F()):
                        return ('Formula ni izpolnjiva')
                    else: slovar[spremenljivka]=T()
            else: #če stavk dalši
                sw=0
##                for stavek in formula.stavki:
##                    for spremenljivka in stavek.literali
##                        if (spremenljivka not in slovar):
##                            slovar[spremenljivka]=T()
##                            sw=1
##                            break
##                    if sw==1:
##                        break

                #če smo napolnili in je formula zadovoljena
                if sw==0:
                    pass
                
                return dpll(formula, slovar)
                

    print('Formula je izpolnjiva na sledeč način:')
    return slovar
                
                
