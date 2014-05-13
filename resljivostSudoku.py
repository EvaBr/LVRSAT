from dpll import *
from sudoku import *


def resitev(rezult):
	"""Iz slovarja spremenljivk, ki jih uporablja pretvorba na SAT, 
	ta funkcija izlusci slovar vrednosti zasedenih polj. """
	
	polja = {}
	for spr in rezult:
		if rezult[spr]==T():
			trojica = tuple(int(i) for i in spr.split(","))
			polja[(trojica[0],trojica[1])] = str(trojica[2])
	return polja

	

def narisi(polja):
	"""Narise sudoku z danimi izpolnjenimi polji."""

	for vr in range(1, 10):
		if vr==1 or vr==4 or vr==7:
			print("\t _________________________")
		vrstica = [polja[(vr,st)] for st in range(1, 10)]
		vrstica = "\t | " + " ".join(vrstica[:3]) + " | " + " ".join(vrstica[3:6]) + " | " + " ".join(vrstica[6:]) + " | "
		print(vrstica)
	print("\t _________________________\n\n")



def preberi(fajlSprimeri):
	"""Prebere fajl s primeri sudokujev. Vrne seznam trojic danih polj."""

	file = open(fajlSprimeri)	
	polja = [[],[],[]]

	for vrstica,line in enumerate(file):
		if vrstica<14 or vrstica%2==1:
			continue
		elif vrstica<37 and vrstica>31:
			continue
		elif vrstica>55 and vrstica<61 :
			continue
		elif vrstica>78:
			break
		else:
			if  vrstica<31:
				vrstSud = (vrstica-12)//2
				P = 0
			elif vrstica<55:
				vrstSud = (vrstica-36)//2
				P = 1
			else:
				vrstSud = (vrstica-60)//2
				P = 2

			l = [k.strip(" ") for k in line.split("|")[1:-1]]
			L = len(l) #=9, ce gre vse po planu... :|
			p = [(vrstSud,i,int(l[i])) for i in range(L) if l[i]!=""]
			polja[P].extend(p)

	file.close()
	return polja
		




def preveri():
	i = 0
	primeri = preberi('primeri.txt')
	for polja in primeri:
		i += 1
		print("  Sudoku št. {0}".format(i))
		print("=================") 
		formula = sudoku(polja).cnf()
		resljivo = dpll(formula)
		if resljivo==0:
			print("Ta sudoku ni rešljiv. \n")
		else:
			polja2 = resitev(resljivo)
			print("Sudoku je možno rešiti. \n\tRešitev: \n")
			narisi(polja2)
		print("\n\n")

	

######

Y = input("\nProsim, vpiši znana polja v datoteko primeri.txt. Ko končaš jo shrani, zapri in pritisni enter. \n")
preveri()
