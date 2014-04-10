#implementacija DPLL

#from BULL import *
from Vaje1in2 import *
from cnf import *


def dodaj(el, vred, slov):
	""" Pomozna funkcija, ki preveri, ali je dan element v 
	slovarju in ali ima ustrezno vrednost. Ce elementa v
	slovarju ni, ga doda. Ce je, a ima napacno vrednost,
	pa javi napako. """

	if type(el)==Neg:
		spr = Neg(el).nnf()
		vr = Neg(vred).nnf() #?
		if spr in slov:
			if slov[spr]==vr:
				pass
			else:
				raise Exception("Not cool, dude.")
		else:
			slov[spr] = vr
	else:
		if el in slov:
			if slov[el]==vred:
				pass
			else: #if slov[el]!=vred
				raise Exception("Not cool, dude.")
		else: #if el not in slov
			slov[el] = vred




def dpll(f):
	""" Pove, ali je formuli mogoce zadostiti. Ce ji je, 
	vrne slovar potrebnih vrednosti spremenljivk."""

	slovarcic = {}	
	def pomozna(formulca, slovar={}):
		formula = formulca.cnf()
		#newFormulca = formulca
		if formula==[]:
			slovarcic = slovar
			return T()
		else:
			for stavek in formula.stavki:
				if stavek==[]:
					return F()
				elif len(stavek.literali)==1:  #Nasli smo stavek, ki je kar literal.
					spremenljivka = stavek.literali[0]
					#Nastavimo ustrezno vrednost spremenljivke:
					print(spremenljivka)
					try:
						dodaj(spremenljivka, T(), slovar)
					except Exception:
						return F()  #( Formula zagotovo ni izpolnjiva. )

			#for object in slovar:
			#	newFormulca = zamenjaj(formulca, object, slovar[object]).poenostavi()  # ali se .cnf???
		newFormula = newFormulca.cnf()
		nasliNovo = False
		for s in newFormula.stavki:  # Poisces eno spremenljivko, ki se ni v slovarju, tj. ji vrednost se ni dolocena.
			for l in s.literali:
				if l not in slovar: #ko bo enkrat napisana f-ja zamenjaj, niti tega ne bo treba preverjat
					nasliNovo = True
					break
		#ko bo zamenjaj napisana, se bo ze tam pogledalo, ce je dobljeno slucajno kar F ali T, in se bo ustrezna stvar vrnila. Potem pa bo 
		#za tu spodaj ostal le primer, ko zagotovo najdemo se eno nedef. spremenljivko, in bo sledil kar 
		#return (pomozna(In(formula, l), slovar) or pomozna(In(formula, Neg(l)), slovar))
		if nasliNovo:
			return (pomozna(In(newFormulca, l), slovar) or pomozna(In(newFormulca, Neg(l)), slovar)) #ker not je treba dat v 
												#navadni obliki, sele pol znotraj f-je se 
													#nardi cnf oblika...
		else:
			#uIzi = (newFormulca.poenostavi()).cnf()
			if newFormulca: #uIzi:
				slovarcic = slovar
			return newFormulca #<-ko prids do sm je newFormulca ze T() ali F(). #uIzi  
					#na zacetku v f-ji rabis cnf obliko, da se loh lepo sprehajas po stavkih. problem pa se pojavi, ko 
					#vstavis notr konkretne vrednosti spremenljivk, ker CNF ne zna nc nardit s T in F...

	rezultat = pomozna(f)
	if rezultat:
		print("Formula je izpolnljiva na naslednji način: ")
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
                
                
