:hibiscus: LVRSAT :hibiscus:
========

### Projekt: SAT solver in prevedba nekaterih problemov na SAT obliko.


###### Ekipa: Teja Tement :bee:, Bojan Bauman :beer: in Eva Breznik :octopus: .


![Zaenkrat kr ena random slikica...](/slikica.gif)


Projekt je razdeljen na dva dela:

:one: SAT solver (implementacija dpll algoritma), datoteke: *boolean*, *cnf*, *dpll* in *testniprimeri*. 

:two: Prevedba nekaj znanih problemov na SAT obliko, datoteke: *barvanje*, *grafi*, *hadamard*, *sudoku*, *primeri*, ter *resljivostSudoku*.


===
##### SAT solver
V datoteki *boolean* se nahajajo definicije logičnih objektov, ki jih potrebujemo v vseh ostalih programih (In, Ali, Spr za spremenljivko, Neg za negacijo...). Datoteka *Cnf*  pravtako vsebuje podobne definicije objektov, ki pa jih potrebujemo predvsem pri pretvorbi logičnih formul v CNF obliko.
V *dpll* je, kot pove že ime, napisana naša luštkana implementacija dpll algoritma (t.j. algoritma, ki za dano SAT formulo pove, ali ji je možno zadostiti, in če ja, kako). Seveda vsebuje tudi kar nekaj pomožnih funkcij, katerih naloga pa je zapisana v njihovem opisu. 

Delovanje vsega trojega se lahko do neke mere preveri s pomočjo osnovnih primerov v fajlu *testniprimeri* (potreben je le zagon skripte).


Naš dpll sicer dela, vendar smo si zaznačili kar nekaj izboljšav (predvsem lepotnih), ki se jih še nameravamo lotiti. Dodano je tudi preverjanje čiste pojavitve.

Kličemo ga takole: `R = dpll(formula)`, pri čemer klic vrne R=0, če formula ni zadovoljiva, ter npr. R={s1: T(), s2: F(), ...} (slovar vrednosti, ki jih morajo zavzeti spremenljivke za zadovoljitev formule), če je. 

V tem vrnjenem slovarju so vrednosti tistih spremenljivk, ki so nepomembne oziroma njihova vrednost na veljavo formule nima vpliva, nastavljene na vrednost T(), kar predstavlja True. (To nekako zveni bolj prijetno in optimistično, kot pa če bi vse nastavili na False... Bi pa jih sicer BP lahko.)


Za skeptike, ki bi želeli delovanje implementacije preveriti še na zapletenejših primerih, smo v drugem delu projekta sestavili SAT oblike nekaterih znanih problemov (npr. rešljivost sudokuja, k barvanje grafa ...), na katerih se lahko preveri tako preoblikovanje na CNF obliko kot tudi delovanje dpll-ja.

Poglejmo še klicanje pomembnejših funkcij in objektov po datotekah.

1. boolean:
  * Novo spremenljivko (tip Spr) ustvarimo s klicem `Spr("ime spremenljivke")`.
  * Konjunkcija: Ali(x1, x2, ...), kjer so xi tipa Spr.
  * Konjunkcija: In(x1, x2, ...), kjer so xi tipa Spr.
  * Negacija: Neg(x), kjer x tipa Spr.
  * True: T(), False: F().
  * Poenostavljanje formul: izraz.poenostavi()
  * Računanje CNF oblike: izraz.cnf()
2. dpll:
  * Preverjanje rešljivosti SAT problema: dpll(izraz), kjer je izraz tipa Ali, In, Spr, Neg, T ali F. Klic bo, kot že rečeno, vrnil 0, če problem ni rešljiv, ter ustrezen slovar, če je.



===
##### Prevedba problemov na SAT obliko
V datotekah *barvanje*, *sudoku* in *hadamard* se nahajajo funkcije, ki izpišejo SAT obliko posamezih obravnavanih problemov (Povezanost in ErdOševa diskrepanca še prideta nekoč...). Ostale datoteke tega dela so namenjene predvsem testiranju kode. 
Imena in uporaba funkcij po problemih:



* 3COL/kCOL:

Funkcijo **barvanje(n, E)** v datoteki *barvanje* pokličemo na številu vozlišč n in seznamu povezav (tj. seznamu dvojic) E. Seveda nam vozlišča predstavljajo števila od 1 do n, zato je potrebno tudi povezave E podati s tovrstnimi oznakami.
Funkcija vrne logično formulo, ki ustreza SAT obliki tega problema, pri čemer nastopajoče spremenljivke 'Ci.j' predstavljajo trditev, da je vozlišče i pobarvano z barvo j.

Primer uporabe: `formula = barvanje(5, [(1,3), (2,3), (4,5), (2,4), (2,5)])`

Povsem analogno deluje tudi funkcija **kbarvanje(K, n, E)**, ki pa ji moramo dodatno (kot prvi argument) podati še število barv K.

Pravilnost spisanih programov se lahko preveri s pomočjo datoteke *grafi*. V njej je zapisanih nekaj definicij grafov, na katerih se kliče glavna funkcija **kbarvanje**. Za osnovno testiranje bo torej poskrbel že sam zagon datoteke **grafi**, v kolikor želiš preveriti delovanje na kakšnem povsem drugačnem grafu, pa lahko (po importanju modulov *dpll* in *barvanje*) na njem najprej pokličeš **kbarvanje**, nato pa še **dpll** : `rezultat = dpll(kbarvanje(K,n,E))`.


* HADAMARD:

Funkciji **hadamard(n)**, ki se nahaja v istoimenski datoteki, moramo podati le velikost kvadratne matrike n, da dobimo SAT obliko zapisa problema. Za program se je javila :octopus:, tako da bo najbrž trajalo. Je cepljena proti hitrosti. Nekoč kasneje pa bo seveda dodano tudi preverjanje.


* SUDOKU:

Problem rešljivosti sudokuja na SAT obliko prevedemo s klicem funkcije **sudoku(polja)** istoimenske datoteke. Kot argument ji podamo seznam zasedenih polj, torej tistih, čigar vrednost je že podana. Polja predstavimo s trojicami (i, j, k), kjer je i vrstica in j stolpec polja, k pa vrednost, ki se nahaja v njem.
Funkcija ne preverja, ali so v zasedenih poljih res vrednosti med 1 in 9. (Verjamemo, da nihče ni tak buhtelj, da bi se dejansko potrudil vstaviti kaj čudnega... Hvala ker se s tem strinjaš! :smiley:)

Primer uporabe: `formula = sudoku([(1,1,9),(1,2,2),(3,4,5)])`

Pravilnost kode se lahko preverja s pomočjo datotek *primeri* in *resljivostSudoku*. In sicer je potrebno v katerega izmed sudokujev, ki so zapisani v datoteki *primeri* (.txt), vstaviti željena zasedena polja, nato pa zagnati program *resljivostSudoku*.
Zaenkrat je testiranje še okorno, saj vedno preveri le tri oz. vse tri sudokuje, ki so napisani v njej. (Pa še to jih noče izpisovat. Ampak to so že malenkosti. :wink: )

Spremenljivke v slovarju, ki ga dobimo po klicu dpll-ja na nekem sudoku-ju, imajo zopet obliko trojic i,j,k, ki predstavljajo trditev, da v rešenem sudokuju na mesto v i-ti vrstici in j-tem stolpcu spada število k.


* POVEZANOST GRAFA: je :toilet:.

* ... :soon: (or not)


===
