#implementacija DPLL

from boolean import *
from cnf import *

flag = False
def dodaj(el, vred, slov):  #Dela na CNF obliki, tj el je tipa Til/Lit, ne pa Spr/Neg. vred=T ali F, slovar={Spr("x"):T(),...}
	""" Pomozna funkcija, ki preveri, ali je dan element v 
	slovarju in ali ima ustrezno vrednost. Ce elementa v
	slovarju ni, ga doda. Ce je, a ima napacno vrednost,
	pa javi napako. Vnesen element mora biti v CNF obliki,
	tj. tipa TIL ali LIT. """

	spr = Spr(el.ime)
	if type(el)==Til:
		vr = Neg(vred).poenostavi()
		if spr in slov:
			if slov[spr]==vr:
				pass
			else:
				flag = True
		else:
			slov[spr] = vr
	else: #if type = Lit
		if spr in slov:
			if slov[spr]==vred:
				pass
			else:
				flag = True
		else:
			slov[spr] = vred


def zamenjaj(Fuormula, Abjikt, vridnastAbjikta):
	""" U Fuormuli (ka nij u CNF abliki) zaminja use pojauitve 
		Abjikta z vridnastjo tiha abjikta. """
	
	tip = type(Fuormula)
	if tip==In or tip==Ali:
		neueFormel = tip(*tuple(zamenjaj(f,Abjikt, vridnastAbjikta) for f in Fuormula.sez))
	elif tip==Spr and Fuormula==Abjikt:
		neueFormel = vridnastAbjikta
	elif tip==Neg and Fuormula.izr==Abjikt:
		neueFormel = Neg(vridnastAbjikta).poenostavi()
	else:
		neueFormel = Fuormula
	return neueFormel


def NovaFormula(CNFformula, spr):
	""" Vrne formulo In(CNFformula, spr) v navadni obliki. """
	
	inoti = T()
	for st in CNFformula.stavki:
		aliji = F()
		for sprem in st.literali:
			if type(sprem)==Lit:
				spr = Spr(sprem.ime)
			else: 
				spr = Neg(Spr(sprem.ime))

			aliji = Ali(spr, aliji).poenostavi()
		inoti = In(inoti, aliji).poenostavi()
	return In(inoti, spr)


def dpll(dieFormel):
	""" Sprejme formulo v navadni obliki in pove, ali ji je mogoce zadostiti. 
		Ce ji je, vrne slovar potrebnih vrednosti spremenljivk."""

	slovar = {}
	### Cista pojavitev:
	pojavitve = {}
	Formul = dieFormel.cnf()
	for stavk in Formul.stavki:
		for lit in stavk.literali:
			S = Spr(lit.ime)
			if S in pojavitve:
				pojavitve[S].add(type(lit))
			else:
				pojavitve[S] = {type(lit)}

	for i in pojavitve:
		if len(pojavitve[i])==1:
			tip = pojavitve[i].pop()
			dodaj(tip(i.ime), T(), slovar)

	for neki in slovar:
		dieFormel = zamenjaj(dieFormel, neki, slovar[neki]).poenostavi()
	
	###
	def pomozna(formulca, slovar):
		formula = formulca.poenostavi().cnf()
		sprememba = True
		while sprememba:			
			if formula.stavki==[]:
				return (T(), slovar)
			else:
				for stavek in formula.stavki:
					sprememba = False
					if stavek.literali==[]:
						return (F(), slovar)
					elif len(stavek.literali)==1:  #Nasli smo stavek, ki je kar literal.
						spremenljivka = stavek.literali[0]
						#Nastavimo ustrezno vrednost spremenljivke:
						if not flag:
							dodaj(spremenljivka, T(), slovar)
							spremenljivka = Spr(spremenljivka.ime)
							formulca = zamenjaj(formulca, spremenljivka, slovar[spremenljivka]).poenostavi()
							formula = formulca.cnf()
							sprememba = True
							break
						else: #if flag; to se ne bi smelo zgoditi spljoh.
							print("this should not happen")
							return (F(), slovar)
						
			
		#Poglejmo, ali je ostala se kaksna spremenljivka brez vrednosti:
		nasliNovo = False
		for s in formula.stavki:  #Poisces eno spremenljivko, ki se ni v slovarju, tj. ji vrednost se ni dolocena.
			for l in s.literali:
				nasliNovo = True
				break
	
		if nasliNovo: #l najprej spravimo v class Spr, ker je trenutno tipa Til/Lit.
			L = Spr(l.ime)
			blabla = pomozna(NovaFormula(formula,L),slovar)
			if blabla[0]==T():
				return blabla
			else:
				return pomozna(NovaFormula(formula,Neg(L)),slovar)
		else:
			return (formulca, slovar) #<-Ko pride do sem je formulca ze T() ali F().  

	rezultat = pomozna(dieFormel, slovar)
	
	#Nastimamo se vse nepotrebne zadeve v slovarju:
	for teja in pojavitve:
		if teja not in rezultat[1]:
			rezultat[1][teja] = T() #Smo optimisti, pa bomo vse nastimali na tru.

	if rezultat[0]==T():
		print("Formula je izpolnljiva.")
		return rezultat[1] #Returnamo slovarcek.
	else:
		print("Formula ni izpolnljiva.")
		return 0
