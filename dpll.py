#implementacija DPLL

from boolean import *
from cnf import *


def dodaj(el, vred, slov):  #Dela na CNF obliki, tj el je tipa Til/Lit, ne pa Spr/Neg. vred=T ali F, slovar={Spr("x"):T(),...}
	""" Pomozna funkcija, ki preveri, ali je dan element v 
	slovarju in ali ima ustrezno vrednost. Ce elementa v
	slovarju ni, ga doda. Ce je, a ima napacno vrednost,
	pa javi napako. Vnesen element mora biti v CNF obliki,
	tj. tipa TIL ali LIT. """

	spr = Spr(el.ime)
	if type(el)==Til:
		vr = Neg(vred).poenostavi()
		if spr in slov
			if slov[spr]==vr:
				pass
			else:
				raise Eksepsn("Not cool, dude.")
		else:
			slov[spr] = vr
	else: #if type = Lit
		if spr in slov:
			if slov[spr]==vred:
				pass
			else:
				raise Eksepsn("Not cool, dude.")
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



def dpll(dieFormel):
	""" Sprejme formulo v navadni obliki in pove, ali ji je mogoce zadostiti. 
		Ce ji je, vrne slovar potrebnih vrednosti spremenljivk."""

	slovarcic = {}	
	def pomozna(formulca, slovar={}):
		formula = formulca.poenostavi().cnf()
		if formula.stavki==[]:
			for i in slovar:
				slovarcic[i] = slovar[i]
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
					except Eksepsn, msg:
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

		if nasliNovo: #(l najprej spravimo v class Spr, ker je trenutno Til/Lit)
			return (pomozna(In(formulca, Spr(l.ime)), slovar) or pomozna(In(formulca, Neg(Spr(l.ime))), slovar)) #ker not je treba dat v navadni obliki, sele pol znotraj f-je se nardi cnf oblika...
		else:
			if formulca: #formulca je tu ze sama T(), nismo nasli nobene spremenljivke brez vrednosti...
				for i in slovar:
					slovarcic[i] = slovar[i]
			return formulca #<-Ko pride do sem je formulca ze T() ali F().  

	rezultat = pomozna(dieFormel)
	if rezultat==T():
		print("Formula je izpolnljiva na naslednji način: ")
	else:
		print("Formula ni izpolnljiva.")
	return slovarcic #Ce se ne da zadovoljit formule pac vrne praznega, pa kaj pol.




###########################
#Manjka se:
#--------------------------
# + Se cista pojavitev.     
