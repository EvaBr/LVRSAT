:hibiscus: LVRSAT :hibiscus:
========

### Projekt: SAT solver in prevedba nekaterih problemov na SAT obliko.


###### Ekipa: Teja Tement :bee:, Bojan Bauman :beer: in Eva Breznik :octopus: .


![Zaenkrat kr ena random slikica...](/slikica.gif)


Projekt je razdeljen na dva dela:

:one: Prevedba nekaj znanih problemov na SAT obliko, datoteke: *barvanje*, *grafi*, *hadamard*, *sudoku*, *primeri*, ter *resljivostSudoku*.

:two: SAT solver (implementacija dpll algoritma), datoteke: *boolean*, *cnf*, *dpll* in *testniprimeri*. 

===
##### Prevedba problemov na SAT obliko
V datotekah *barvanje*, *sudoku* in *hadamard* se nahajajo funkcije, ki izpišejo SAT obliko posamezih obravnavanih problemov (Povezanost in ErdOševa diskrepanca še prideta nekoč...). Ostale datoteke tega dela so namenjene predvsem testiranju kode. 
Imena in uporaba funkcij po problemih:

* 3COL:

Funkcijo **barvanje(n, E)** v datoteki *barvanje* pokličemo na številu vozlišč n in seznamu povezav (tj. seznamu dvojic) E. Seveda nam vozlišča predstavljajo števila od 1 do n, zato je potrebno tudi povezave E podati s tovrstnimi oznakami.
Funkcija vrne logično formulo, ki ustreza SAT obliki tega problema, pri čemer nastopajoče spremenljivke 'Ci.j' predstavljajo trditev, da je vozlišče i pobarvano z barvo j.

Primer uporabe: 'formula = barvanje(5, [(1,3), (2,3), (4,5), (2,4), (2,5)])'

Pravilnost spisanih programov se lahko preveri s pomočjo datoteke *grafi*. V njej je zapisanih nekaj definicij grafov, na katerih se kliče glavna funkcija **barvanje**.

DODAJ: NACIN KLICA TEH PRIMEROV


* Hadamard:

Funkciji **hadamard(n)**, ki se nahaja v istoimenski datoteki, moramo podati le velikost kvadratne matrike n, da dobimo SAT obliko zapisa problema. Za program se je javila :octopus:, tako da bo najbrž trajalo. Je cepljena proti hitrosti. Nekoč kasneje pa bo seveda dodano tudi preverjanje.


* Sudoku:

Problem rešljivosti sudokuja na SAT obliko prevedemo s klicem funkcije **sudoku(polja)** istoimenske datoteke. Kot argument ji podamo seznam zasedenih polj, torej tistih, čigar vrednost je že podana. Polja predstavimo s trojicami (i, j, k), kjer je i vrstica in j stolpec polja, k pa vrednost, ki se nahaja v njem.
Funkcija ne preverja, ali so v zasedenih poljih res vrednosti med 1 in 9. (Verjamemo, da nihče ni tak buhtelj, da bi se dejansko potrudil vstaviti kaj čudnega... Hvala ker se s tem strinjaš! :smiley:)

Primer uporabe: 'formula = sudoku([(1,1,9),(1,2,2),(3,4,5)])' 

Pravilnost kode se lahko preverja s pomočjo datotek *primeri* in *resljivostSudoku*. In sicer je potrebno v katerega izmed sudokujev, ki so zapisani v datoteki *primeri* (.txt), vstaviti željena zasedena polja. Zaenkrat je testiranje še okorno, saj vedno preveri le tri oz. vse tri sudokuje, ki so napisani v njej.


* Povezanost grafa


* ...


===
##### SAT solver
V datoteki *boolean* se nahajajo definicije logičnih objektov, ki jih potrebujemo v vseh ostalih programih (In, Ali, Spr za spremenljivko, Neg za negacijo...). Datoteka *Cnf*  pravtako vsebuje podobne definicije objektov, ki pa jih potrebujemo predvsem pri pretvorbi logičnih formul v CNF obliko.
V *dpll* je, kot pove že ime, napisana naša luštkana implementacija dpll algoritma (t.j. algoritma, ki za dano SAT formulo pove, ali ji je možno zadostiti, in če ja, kako). Seveda vsebuje tudi kar nekaj pomožnih funkcij, katerih naloga pa je zapisana v njihovem opisu. 

Delovanje vsega trojega se lahko do neke mere preveri s pomočjo primerov v fajlu *testniprimeri* (potreben je le zagon skripte).


Naš dpll sicer dela, vendar smo si zaznačili kar nekaj izboljšav (predvsem lepotnih), ki se jih še nameravamo lotiti. Dodano je tudi preverjanje čiste pojavitve.

Kličemo ga takole: 'R = dpll(formula)', pri čemer klic vrne R=0, če formula ni zadovoljiva, ter npr. R={s1: T(), s2: F(), ...} (slovar vrednosti spremenljivk), če je. 

V tem vrnjenem slovarju so vrednosti tistih spremenljivk, ki so nepomembne oziroma njihova vrednost na veljavo formule nima vpliva, nastavljene na vrednost T(), kar predstavlja True. (To nekako zveni bolj prijetno optimistično, kot pa če bi vse nastavili na False... Bi pa jih sicer BŠS lahko.)
