#implementacija DPLL

from boolean import *
from cnf import *


def dodaj(el, vred, slov):  #Dela na CNF obliki, tj el je tipa Til/Lit, ne pa Spr/Neg. vred=T ali F, slovar={Spr("x"):T(),...}
	""" Pomozna funkcija, ki v slovarju vrednosti spremenljivk pripise
		podanemu elementu (ki mora biti tipa TIL ali LIT) ustrezno 
		vrednost (glede na njegov tip). """

	spr = el.ime
	if type(el)==Til:
		vred = Neg(vred).poenostavi()
	slov[spr] = vred


def zamenjaj(Fuormula, Abjikt, vridnastAbjikta):
	""" U Fuormuli (ka je u CNF abliki) zaminja use pojauitve 
		Abjikta z vridnastjo tiha abjikta. (Na mistu!) 
		Abjikt je padan kat string (sam z iminam). """
	
	stavk = 0
	stavkov = len(Fuormula.stavki)
	while stavk < stavkov:
		poved = Fuormula.stavki[stavk]
		koliko = len(poved.literali)
		crka = 0
		while crka < koliko:
			naVrsti = poved.literali[crka]
			if naVrsti.ime == Abjikt:
				Tip = type(naVrsti)
				if (Tip==Til and vridnastAbjikta==T()) or (Tip==Lit and vridnastAbjikta==F()): #vstavljamo F v Ali -> lahko ga kar spustimo.
					del (Fuormula.stavki[stavk]).literali[crka]
					koliko -= 1
					crka -= 1
				else: #if (Tip==Til and vridnastAbjikta==F()) or (Tip==Lit and vridnatAbjikta==T()) #vstavljamo T v Ali -> lahko spustimo cel stavek.
					del Fuormula.stavki[stavk]
					stavkov -= 1
					stavk -= 1
					break
			crka += 1
		stavk += 1
	#returnat nam ni treba nic, ker gre za spremembo formule na mestu.



def dpll(dieFormel):
	""" Sprejme formulo v CNF obliki in pove, ali ji je mogoce zadostiti. 
		Ce ji je, vrne slovar potrebnih vrednosti spremenljivk. """

	slovarc = {}
	### Cista pojavitev:
	pojavitve = {}
	for stavk in dieFormel.stavki:
		for lit in stavk.literali:
			S = lit.ime
			if S in pojavitve:
				pojavitve[S].add(type(lit))
			else:
				pojavitve[S] = {type(lit)}
	for i in pojavitve:
		if len(pojavitve[i])==1:
			tip = pojavitve[i].pop()
			dodaj(tip(i.ime), T(), slovarc)
	for neki in slovarc:
		zamenjaj(dieFormel, neki, slovarc[neki])
	###

	def pomozna(formula, slovar):
		#formula je cnf oblike
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
						dodaj(spremenljivka, T(), slovar)
						zamenjaj(formula, spremenljivka.ime, slovar[spremenljivka.ime])
						sprememba = True
						break
			
		#Poglejmo, ali je ostala se kaksna spremenljivka brez vrednosti:
		nasliNovo = False
		for s in formula.stavki:  #Poisces eno spremenljivko, ki se ni v slovarju, tj. ji vrednost se ni dolocena.
			for l in s.literali:
				nasliNovo = True
				break
			if nasliNovo: break
	
		if nasliNovo: #to bi se tako moralo zmeraj zgoditi, če pridemo do sem 

			formula2 = Cnf([Stavek([litral for litral in st.literali]) for st in formula.stavki]) #naredimo kopijo, saj zadevo kasneje spreminjamo 'na mestu'
			slovar2 = {i:slovar[i] for i in slovar} #naredimo kopijo, saj zadevo kasneje spreminjamo 'na mestu'
			slovar2[l.ime] = T()
			zamenjaj(formula2, l.ime, T())
			blabla = pomozna(formula2, slovar2)
			if blabla[0]==T():
				return blabla
			else:
				slovar[l.ime] = F()
				zamenjaj(formula, l.ime, F())
				return pomozna(formula, slovar)

	rezultat = pomozna(dieFormel, slovarc)
	
	#Nastimamo se vse nepotrebne zadeve v slovarju:
	for teja in pojavitve:
		if teja not in rezultat[1]:
			rezultat[1][teja] = T()

	if rezultat[0]==T():
		#print("Formula je izpolnljiva.")
		return rezultat[1] #Returnamo slovarcek.
	else:
		#print("Formula ni izpolnljiva.")
		return 0
