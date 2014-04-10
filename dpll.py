#implementacija DPLL

#from BULL import *
from vaja1in2 import *
from cnf import *


def dodaj(el, vred, slov):
	""" Pomozna funkcija, ki preveri, ali je dan element v 
	slovarju in ali ima ustrezno vrednost. Ce elementa v
	slovarju ni, ga doda. Ce je, a ima napacno vrednost,
	pa javi napako. """

	if el in slov:
		if slov[el]==vred:
			pass
		else: #if slov[el]!=vred
			raise Exception("Not cool, dude.")
	else: #if el not in slov
		slov[el] = vred
			


def dpll(formula):
	""" Pove, ali je formuli mogoce zadostiti. Ce ji je, 
	vrne slovar potrebnih vrednosti spremenljivk."""
	
	def pomozna(formula, slovar={}):
		formula = formula.cnf()
		if formula==[]:
			return T()
		else:
			for stavek in formula.stavki:
				if stavek==[]:
					return F()
				elif len(stavek.literali)==1:  #Nasli smo stavek, ki je kar literal.
					spremenljivka = stavek.literali[0]
					#Nastavimo ustrezno vrednost spremenljivke:
					if type(spremenljivka)==Neg:
						spr2 = Neg(spremenljivka).nnf()
						try:
							dodaj(spr2, F(), slovar)
						except Exception:
							return F()  #( Formula zagotovo ni izpolnjiva. )
					else:	
						try:
							dodaj(spr2, T(), slovar)
						except Exception:
							return F()  #( Formula zagotovo ni izpolnjiva. )
					formula = (zamenjaj(formula, spr2, slovar[spr2]).poenostavi()).cnf()  # ali samo .cnf???

		for s in formula.stavki:  # Poisces eno spremenljivko, ki se ni v slovarju, tj. ji vrednost se ni dolocena.
			for l in s.literali:
				if l not in slovar:
					break
		return (pomozna(In(formula, l), slovar) or pomozna(In(formula, Neg(l)), slovar))

	slovarcic = {}
	rezultat = pomozna(formula, slovarcic)
	if rezultat:
		print("Formula je izpolnljiva na naslednji način: /n")
		return slovarcic
	else:
		print("Formula ni izpolnljiva.")
		# Je treba kaj returnat?



###########################
#Manjka se:
#--------------------------
# + Funkcija zamenjaj (form, s, v), ki zamenja vse pojave s-a v formuli form z vrednostjo v.
# + Se cista pojavitev.     




























#            else: #ce stavek daljsi
#                sw = 0
#                for stavek in formula.stavki:
#                    for spremenljivka in stavek.literali:
#                        if (spremenljivka not in slovar):
#                            slovar[spremenljivka]=T()
#                            sw=1
#                            break
#                    if sw==1:
#                        break
#
#                #če smo napolnili in je formula zadovoljena
#                if sw==0:
#	                return dpll(formula, slovar)
#
#    print('Formula je izpolnjiva na sledeč način:')
#    return slovar
                
                
