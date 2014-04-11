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
		vr = Neg(vred).nnf() #treba tle nnf?
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


def zamenjaj(Fuormula, Abjikt, vridnastAbjikta):
	""" U Fuormuli zaminja use pojauitve Abjikta z 
		vridnastjo tiha abjikta. """
	
	tip = type(Fuormula)
	if tip==In or tip==Ali:
		neueFormel = tip(zamenjaj(f,Abjikt, vridnastAbjikta) for f in Fuormula.sez)
	elif tip==Spr and Fuormula==Abjikt:
		neueFormel = vridnastAbjikta
	elif tip==Neg and Fuormula.izr==Abjikt:
		neueFormel = Neg(vridnastAbjikta).nnf()
	else:
		neueFormel = Fuormula
	return neueFormel



def dpll(dieFormel):
	""" Pove, ali je formuli mogoce zadostiti. Ce ji je, 
	vrne slovar potrebnih vrednosti spremenljivk."""

	slovarcic = {}	
	def pomozna(formulca, slovar={}):
		formula = formulca.poenostavi().cnf()
		if formula.stavki==[]:
			slovarcic = slovar
			return T()
		else:
			for stavek in formula.stavki:
				if stavek.literali==[]:
					return F()
				elif len(stavek.literali)==1:  #Nasli smo stavek, ki je kar literal.
					spremenljivka = stavek.literali[0]
					#Nastavimo ustrezno vrednost spremenljivke:
					try:
						dodaj(spremenljivka, T(), slovar)
					except Exception:
						return F()  #( Formula zagotovo ni izpolnjiva. )

			for object in slovar: #Ko smo našli vse 'literalne' stavke, v formulo vstavimo dobljene vrednosti. #### OP: bi blo boljs to sproti, v zanki update-at?
				formulca = zamenjaj(formulca, object, slovar[object]).poenostavi() #Potrebujemo neCNF obliko nove formule...
			formula = formulca.cnf() #Potrebujemo TUDI CNF obliko.
		#Poglejmo, ali je ostala se kaksna spremenljivka brez vrednosti:
		nasliNovo = False
		for s in formula.stavki:  # Poisces eno spremenljivko, ki se ni v slovarju, tj. ji vrednost se ni dolocena.
			for l in s.literali:
				nasliNovo = True
				break

		if nasliNovo:
			return (pomozna(In(formulca, l), slovar) or pomozna(In(formulca, Neg(l)), slovar)) #ker not je treba dat v navadni obliki, sele pol znotraj f-je se nardi cnf oblika...
		else:
			if formulca: #formulca je tu ze sama T(), nismo nasli nobene spremenljivke brez vrednosti...
				slovarcic = slovar
			return formulca #<-Ko pride do sem je formulca ze T() ali F().  
					#OP: Na zacetku v f-ji rabis cnf obliko, da se loh lepo sprehajas po stavkih. problem pa se pojavi, ko 
					#vstavis notri konkretne vrednosti spremenljivk, ker CNF ne zna nc nardit s T in F...(ni stavkov zato ni mozna iteracija...)

	rezultat = pomozna(dieFormel)
	if rezultat:
		print("Formula je izpolnljiva na naslednji način: ")
		#return slovarcic
	else:
		print("Formula ni izpolnljiva.")
	return slovarcic




###########################
#Manjka se:
#--------------------------
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
                
                
