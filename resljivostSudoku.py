from dpll import *
from sudoku import *


def narisi(polja):
	"""Narise sudoku z danimi izpolnjenimi polji."""

	for i in range(1, 10):
		print("_____________________________________\n")
		for j in range(1, 10):
			zasedli = False
			for k in range(1, 10):
				if (i, j, k) in polja:
					print("| {0} ".format(k))
					zasedli = True
					break
			if not zasedli:
				print("|   ")
		print("|\n")
	print("_____________________________________\n\n")



def preberi(fajlSprimeri):
	"""Prebere fajl s primeri sudokujev. Vrne seznam trojic danih polj."""

	file = open(fajlSprimeri, 'r')
	
	koncna = []
	polja = []
	vpisano = {}
	vrstica = -1
	for line in file:
		vrstica+=1
		if vrstica<13 or vrstica%2==0:
			continue
		#else:
		try:
			for k in range(9):
				if line[2+4*k]!=" ":
					vpisano[k+1] = int(line[2+4*k])
			for element in vpisano:
				polja.append((vrstica, element, vpisano[element]))
		except IndexError:
			continue
		if vrstica%24==9:
			print("polja: ",polja)
			koncna.append(polja)
			polja = []
	file.close()
	return koncna		
		


def resitev(rezult):
	"""Spremenljivke, ki jih uporablja pretvorba na SAT, ta funkcija 
	spremeni nazaj v trojice zasedenih polj. """
	
	polja = []
	for spr in rezult:
		if rezult[spr]==T():
			trojica = tuple(int(i) for i in spr.split(","))
			polja.append(trojica)	
	return polja



def preveri():
	i = 0
	primeri = preberi('primeri.txt')
	for polja in primeri:
		i += 1
		print("  Sudoku št. {0}".format(i))
		print("=================") 
		formula = sudoku(polja)
		resljivo = dpll(formula)
		narisi(polja)
		if resljivo==0:
			print("Ta sudoku ni rešljiv. \n")
		else:
			polja2 = resitev(resljivo)
			print("Sudoku je možno rešiti. \n Rešitev je naslednja: \n")
			narisi(polja2)
		print("\n\n")

	

######
preveri()
