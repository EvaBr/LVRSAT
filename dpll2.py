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
		Ce ji je, vrne slovar potrebnih vrednosti spremenljivk."""

	slovar = {}
	### Cista pojavitev:
	pojavitve = {}
	for stavk in dieFormel.stavki:
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
		zamenjaj(dieFormel, neki.ime, slovar[neki])
	
	###
	def pomozna(formula, slovar):
		#formula = cnf oblike
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
							zamenjaj(formula, spremenljivka.ime, slovar[Spr(spremenljivka.ime)])
							sprememba = True
							break
						else: #if flag; to se ne bi smelo zgoditi spljoh.
							print("So not cool, dude. This should not happen!")
							return (F(), slovar)
						
			
		#Poglejmo, ali je ostala se kaksna spremenljivka brez vrednosti:
		nasliNovo = False
		#preostanek = formula.stavki.sort(key = lambda s: len(s))
		for s in formula.stavki:  #Poisces eno spremenljivko, ki se ni v slovarju, tj. ji vrednost se ni dolocena.
			for l in s.literali:
				nasliNovo = True #Ce ne bo poenostavljanja, je treba pazit se da l!=T in F?
				break
	
		if nasliNovo: 
			formula.stavki.extend([Stavek([Lit(l.ime)])])
			blabla = pomozna(formula, slovar)
			if blabla[0]==T():
				return blabla
			else:
				#iz formule je treba stran vzet kar smo prej extendali, oz. menjat z lih negiranim stavkom
				for sentence in formula.stavki:
					sezn = sentence.literali
					if len(sezn)==1 and sezn[0].ime==l.ime and type(sezn[0])==Lit:
						sentence.literali[0] = Til(l.ime)		
				return pomozna(formula, slovar)
		else:
			return (formula, slovar) #<-Ko pride do sem je formula ze T().cnf() ali F().cnf().  

	rezultat = pomozna(dieFormel, slovar)
	
	#Nastimamo se vse nepotrebne zadeve v slovarju:
	for teja in pojavitve:
		if teja not in rezultat[1]:
			rezultat[1][teja] = T() #Smo optimisti, pa bomo vse nastimali na tru.

	if rezultat[0]==T():
		#print("Formula je izpolnljiva.")
		return rezultat[1] #Returnamo slovarcek.
	else:
		#print("Formula ni izpolnljiva.")
		return 0
