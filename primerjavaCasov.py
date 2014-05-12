from random import *
from dpll import dpll
from dpll_ena_cista_pojavitev import *
from dpll_brez import dpll_osnoven
from sudoku import *
from time import clock


print("Primerjava DPLL algoritmov z, brez, ter z le eno začetno preverbo čiste pojavitve. \n")
D = input("Primerjam DPLL s čisto pojavitvijo? (y/n)  ")
D1 = input("Primerjam DPLL z le eno izvedbo čiste pojavitve (takoj na začetku)?  (y/n)  ")
DB = input("Primerjam osnoven DPLL, brez implementacije čiste pojavitve? (y/n)  ")
L = 0
if not (D=="n" and D1=="n" and DB=="n"):
	L = int(input("Koliko naključnih polnitev polj (sudokujev) zgeneriram? Vnesi naravno št."))

if not (D=="n" and D1=="n" and DB=="n"):
	print("\n Prazen sudoku:")
	print("="*25)
	CNF = sudoku([]).cnf()

if D=="y":
	kopija = Cnf([Stavek([i for i in s.literali]) for s in CNF.stavki])
	before1 = clock()
	rez1 = dpll(kopija)
	after1 = clock()
	print("Dpll z večkratno čisto pojavitvijo potrebuje {0} sec.".format(after1-before1))

if D1=="y":
	kopija = Cnf([Stavek([i for i in s.literali]) for s in CNF.stavki])
	before2 = clock()
	rez2 = dpll_brez_ciste(kopija)
	after2 = clock()
	print("Dpll z enkratno čisto pojavitvijo potrebuje {0} sec.".format(after2-before2))

if DB=="y":
	before3 = clock()
	rez3 = dpll_osnoven(CNF)
	after3 = clock()
	print("Dpll brez vsakršne čiste pojavitve potrebuje {0} sec.".format(after3-before3))



for i in range(L): #koliko primerov bomo naredili
	P = randint(1, 30) #koliko  bo danih polj
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

	print("\n \n Sudoku {0}: ".format(i+1))
	print("="*25)
	print("Podana zasedena polja na začetku: ")
	print(polja, "\n")
	CNF = sudoku(polja).cnf()

	if D=="y":
		kopija = Cnf([Stavek([i for i in s.literali]) for s in CNF.stavki])
		before1 = clock()
		rez = dpll(kopija)
		after1 = clock()
		print("Dpll z večkratno čisto pojavitvijo potrebuje {0} sec.".format(after1-before1))

	if D1=="y":
		kopija = Cnf([Stavek([i for i in s.literali]) for s in CNF.stavki])
		before2 = clock()
		rez = dpll_brez_ciste(kopija)
		after2 = clock()
		print("Dpll z enkratno čisto pojavitvijo potrebuje {0} sec.".format(after2-before2))

	if DB=="y":
		before3 = clock()
		rez = dpll_osnoven(CNF)
		after3 = clock()
		print("Dpll brez vsakršne čiste pojavitve potrebuje {0} sec.".format(after3-before3))

	if rez==0:
		print("Sudoku ni bil rešljiv. \n \n")
	else:
		print("Sudoku je bil rešljiv. \n \n")
	



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
sudi = ["Easy", "Medium", "Hard", "Evil", "večlično rešljiv"]


if not (D=="n" and D1=="n" and DB=="n"):
	print("\n \n Dodatnih 5 rešljivih sudokujev: ")
	for i in range(5):
		print("\n \n Sudoku {0}: ".format(i+L+1), sudi[i])
		print("="*30)
		CNF = sud[i].cnf()

		if D=="y":
			kopija = Cnf([Stavek([i for i in s.literali]) for s in CNF.stavki])
			bef1 = clock()
			rez1 = dpll(kopija)
			aft1 = clock()
			print("Dpll z večkratno čisto pojavitvijo potrebuje {0} sec.".format(aft1-bef1))

		if D1=="y":
			kopija = Cnf([Stavek([i for i in s.literali]) for s in CNF.stavki])
			bef2 = clock()
			rez2 = dpll_brez_ciste(kopija)
			aft2 = clock()
			print("Dpll z enkratno čisto pojavitvijo potrebuje {0} sec. ".format(aft2-bef2))

		if DB=="y":
			bef3 = clock()
			rez3 = dpll_osnoven(CNF)
			aft3 = clock()
			print("Dpll brez vsakršne čiste pojavitve potrebuje {0} sec. \n \n".format(aft3-bef3))

	
