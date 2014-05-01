from random import *
from dpll import *
from sudoku import *


print("Prazen sudoku:")
print("="*20)
rez = dpll(sudoku([]).cnf())
if rez==0:
	print("Sudoku ni rešljiv!")
	print("\n\n")
else: 
	print("sudoku je rešljiv. Rešitev: \n")
	K = [vr for vr in rez if rez[vr]==T()]
	vrstice = {j : {int(i[2]):int(i[4]) for i in K if i[0] == str(j)} for j in range(1,10)}
	for vrstica in range(1,10):
		elti = vrstice[vrstica]
		vrsta = []
		for stolpc in range(1,10):
			vrsta.append(elti[stolpc])
		print(vrsta)
	print("\n\n")


for i in range(10): #koliko primerov bomo naredili
	P = randint(1, 81) #koliko bo danih polj
	polja = []
	p = 0
	while p<P:
		vrstica = randint(1,9) #zgeneriramo dana polja in njih vrednosti
		stolpec = randint(1,9)
		st = randint(1,9)
		polje = (vrstica, stolpec, st)
		if polje not in polja:
			polja.append(polje)
			p += 1

	print("Sudoku {0}: ".format(i+1))
	print("="*20)
	print("Podana zasedena polja na začetku: ")
	print(polja, "\n")
	
	rez = dpll(sudoku(polja).cnf())
	if rez==0:
		print("Sudoku ni rešljiv!")
	else:
		print("Sudoku je rešljiv. Rešitev: \n")
		K = [vr for vr in rez if rez[vr]==T()]
		vrstice = {j : {int(i[2]):int(i[4]) for i in K if i[0] == str(j)} for j in range(1,10)}
		for vrstica in range(1,10):
			elti = vrstice[vrstica]
			vrsta = []
			for stolpc in range(1,10):
				vrsta.append(elti[stolpc])
			print(vrsta)
	print("\n\n")

#Ker bodo najverjetneje vsi sudokuji, ki bodo takole na random zgenerirani, neresljivi, sledi se 5 primerov
#sudokujev z interneta, ki pa so zagotovo resljivi:

#easy:
s1 = [(1,2,1),(1,3,7),(1,4,5),(2,2,2),(2,4,7),(2,6,9),(2,7,8),(3,1,4),(3,4,3),(3,5,8),(3,9,5),(4,2,5),(4,4,2),(4,5,4),(4,6,6),(4,8,3),(4,9,8),(5,4,8),(5,6,3),(6,1,3),(6,2,8),(6,4,1),(6,5,5),(6,6,7),(6,8,4),(7,1,1),(7,5,7),(7,6,2),(7,9,3),(8,3,2),(8,4,9),(8,6,5),(8,8,8),(9,6,8),(9,7,2),(9,8,7)]
#medium:
s2 = [(1,3,3),(1,6,6),(1,9,8),(2,1,7),(2,3,4),(2,4,2),(2,5,5),(3,4,7),(3,6,9),(3,7,1),(4,5,9),(4,8,7),(4,9,4),(5,1,4),(5,3,1),(5,5,8),(5,7,6),(5,9,9),(6,1,8),(6,2,9),(6,5,2),(7,3,8),(7,4,3),(7,6,2),(8,5,6),(8,6,5),(8,7,2),(8,9,7),(9,1,6),(9,4,9),(9,7,3)]
#hard:
s3 = [(1,4,2),(1,7,7),(2,1,8),(2,4,7),(2,8,2),(3,2,2),(3,3,5),(3,8,1),(3,9,9),(4,2,4),(4,5,3),(4,6,1),(5,3,7),(5,7,9),(6,4,8),(6,5,4),(6,8,6),(7,1,4),(7,2,7),(7,7,5),(7,8,8),(8,2,8),(8,6,2),(8,9,3),(9,3,6),(9,6,5)]
#evil:
s4 = [(1,3,2),(1,4,7),(2,3,1),(2,6,4),(2,7,6),(2,8,2),(3,1,4),(3,6,6),(4,1,5),(4,8,4),(4,9,2),(5,2,7),(5,5,8),(5,8,3),(6,1,3),(6,2,2),(6,9,1),(7,4,3),(7,9,5),(8,2,8),(8,3,7),(8,4,5),(8,7,2),(9,6,8),(9,7,9)]
#veclicno resljiv:
s5 = [(1,2,1),(1,3,7),(1,4,5),(2,2,2),(2,4,7),(2,6,9),(2,7,8),(3,1,4),(3,4,3)]


sud = [sudoku(s1), sudoku(s2), sudoku(s3), sudoku(s4), sudoku(s5)]

for i in range(5):
	print("Sudoku {0}: ".format(i+11))
	print("="*20)
	rez = dpll(sud[i].cnf())
	if rez==0:
		print("Sudoku ni rešljiv! \n\n")
	else:
		print("sudoku je rešljiv. Rešitev: \n")
		K = [vr for vr in rez if rez[vr]==T()]
		vrstice = {j : {int(i[2]):int(i[4]) for i in K if i[0] == str(j)} for j in range(1,10)}
		for vrstica in range(1,10):
			elti = vrstice[vrstica]
			vrsta = []
			for stolpc in range(1,10):
				vrsta.append(elti[stolpc])
			print(vrsta)
		print("\n\n")

