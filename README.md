:hibiscus: LVRSAT :hibiscus:
========

### Projekt: SAT solver in prevedba nekaterih problemov na SAT obliko.


###### Ekipa: Teja Tement :bee:, Bojan Bauman :beer: in Eva Breznik :octopus: .


![Zaenkrat kr ena random slikica...](/slikica.gif)


Projekt je razdeljen na dva dela:

:one: SAT solver (prevedba logičnega izraza na [CNF](http://en.wikipedia.org/wiki/Conjunctive_normal_form) obliko, implementacija [DPLL](http://en.wikipedia.org/wiki/DPLL_algorithm) algoritma), datoteke: *boolean*, *cnf*, *dpll* in *testniprimeri* (dodatno še *dpll_ena_cista_pojavitev*, *dpll_brez*, ter *primerjavaCasov*). 

:two: Prevedba nekaj znanih problemov na SAT, datoteke: *barvanje*, *grafi*, *hadamard*, *sudoku*, *primeri*, *resljivostSudoku* ter *sudokuji*.


===
##### SAT solver
V datoteki *boolean* se nahajajo definicije logičnih objektov, ki jih potrebujemo v vseh ostalih programih (In, Ali, Spr za spremenljivko, Neg za negacijo...). Datoteka *Cnf*  pravtako vsebuje podobne definicije objektov, ki pa jih potrebujemo predvsem pri pretvorbi logičnih formul v CNF obliko.
V *dpll* je, kot pove že ime, napisana naša luštkana implementacija dpll algoritma (t.j. algoritma, ki za dano SAT formulo pove, ali ji je možno zadostiti, in če ja, kako). Seveda vsebuje tudi kar nekaj pomožnih funkcij, katerih naloga pa je zapisana v njihovem opisu.
Glavna funkcija dpll, ki izvede algoritem, sprejme formulo v cnf obliki. Vsebuje tudi preverjanje čiste pojavitve ob vsaki spremembi podane formule. Vendar pazljivo! Formula, ki jo dpll sprejme, je po njegovi izvedbi spremenjena (saj smo se po premisleku odločili in ga sprogramirali tako, da kar nekaj sprememb naredi 'na mestu') !

Delovanje vsega trojega se lahko do neke mere preveri s pomočjo osnovnih primerov v fajlu *testniprimeri* (potreben je le zagon skripte).

Uporaba našega dpll-ja: 
 Kličemo ga (pri čemer moramo seveda najprej importati datoteko *dpll*) takole: `R = dpll(formula)`, kjer klic vrne R=0, če formula ni zadovoljiva, ter npr. R={s1: T(), s2: F(), ...} (slovar vrednosti, ki jih morajo zavzeti spremenljivke za zadovoljitev formule), če je. Formula, ki jo podamo, mora biti v cnf obliki. 

V tem vrnjenem slovarju so vrednosti tistih spremenljivk, ki se v formuli pojavijo a so nepomembne oziroma njihova vrednost na veljavo formule nima vpliva, nastavljene na vrednost T(), kar predstavlja True. (To zveni bolj prijetno in optimistično, kot pa če bi vse nastavili na False... Bi pa jih sicer BP lahko.)

Za skeptike, ki bi želeli delovanje implementacije preveriti še na zapletenejših primerih, smo v drugem delu projekta sestavili SAT oblike nekaterih znanih problemov (npr. rešljivost sudokuja in k barvanje grafa), na katerih se lahko preveri tako preoblikovanje na CNF obliko kot tudi delovanje dpll-ja.

***
**DODATNO:**
V dodatnih datotekah *dpll_brez* in *dpll_ena_cista_pojavitev* se nahajata zgolj informativni implementaciji algoritma brez oz. z eno čisto pojavitvijo;
v *dpll_brez*, kjer ima glavna funkcija ime **dpll_osnoven**, ni nikakršnega preverjanja čiste pojavitve, v *dpll_ena_cista_pojavitev* pa je to dodano le na začetku, takoj ob klicu glavne funkcije te implementacije; **dpll_brez_ciste**. 
Za primerjanje trajanja klicev vseh treh implementacij dpll-ja je dodan še programček *primerjavaCasov*, ki štopa čas izvajanja algoritmov na sudoku primerih (delovanje dpll na sudokujih je opisano malo nižje...);
 ob zagonu je možno izbrati, katere od implementacij želiš preverjati, ter na koliko random generiranih sudokujih. (V vsakem primeru se bodo izbrane 
implementacije primerjale še na praznem sudokuju ter na 5-ih rešljivih različnih težavnosti (enakih, kot se nahajajo v datot. *sudokuji*).)
Med izvajanjem bo program izpisoval pretekel čas za posamezne klice algoritmov.

Tako klic `dpll_osnoven(...)` kot tudi klic `dpll_brez_ciste(...)` sicer delujeta na enak način kot `dpll(...)`.
***

Poglejmo še klicanje pomembnejših funkcij in objektov po datotekah.

1. boolean:
  * Novo spremenljivko (tip Spr) ustvarimo s klicem `Spr("ime spremenljivke")`.
  * Konjunkcija: `Ali(x1, x2, ...)`, kjer so xi tipa Spr.
  * Konjunkcija: `In(x1, x2, ...)`, kjer so xi tipa Spr.
  * Negacija: `Neg(x)`, kjer x tipa Spr.
  * True: `T()`, False: `F()`.
  * Poenostavljanje formul: `izraz.poenostavi()`.
  * Računanje CNF oblike: `izraz.cnf()`. (Vrne formulo tipa Cnf.)
2. dpll:
  * Preverjanje rešljivosti SAT problema: `dpll(izraz)`, kjer je izraz tipa Cnf. Klic bo, kot že rečeno, vrnil 0, če problem ni rešljiv, ter ustrezen slovar, če je.



===
##### Prevedba problemov na SAT obliko
V datotekah *barvanje*, *sudoku* in *hadamard* se nahajajo funkcije, ki izpišejo SAT obliko posamezih obravnavanih problemov (Povezanost in ErdOševa diskrepanca pa morda še prideta nekoč...). Ostale datoteke tega dela so namenjene predvsem testiranju kode. 
Imena in uporaba funkcij po problemih:



* 3COL/kCOL:

Funkcijo **barvanje(n, E)** v datoteki *barvanje* pokličemo na številu vozlišč n in seznamu povezav (tj. seznamu dvojic) E. Seveda nam vozlišča predstavljajo števila od 1 do n, zato je potrebno tudi povezave E podati s tovrstnimi oznakami.
Funkcija vrne logično formulo, ki ustreza SAT obliki tega problema, pri čemer nastopajoče spremenljivke 'Ci.j' predstavljajo trditev, da je vozlišče i pobarvano z barvo j.

Primer uporabe: `formula = barvanje(5, [(1,3), (2,3), (4,5), (2,4), (2,5)])`

Povsem analogno deluje tudi funkcija **kbarvanje(K, n, E)**, ki pa ji moramo dodatno (kot prvi argument) podati še (naravno) število barv K.

Pravilnost spisanih programov se lahko preveri s pomočjo datoteke *grafi*. V njej je zapisanih nekaj definicij grafov, na katerih se kliče glavna funkcija **kbarvanje**. Za osnovno testiranje bo torej poskrbel že sam zagon datoteke **grafi**, v kolikor želiš preveriti delovanje na kakšnem povsem drugačnem grafu, pa lahko (po importanju modulov *dpll* in *barvanje*) na njem najprej pokličeš **kbarvanje** (in dobljeno pretvoriš v cnf obliko), nato pa še **dpll**. Torej takole: `rezultat = dpll(kbarvanje(K,n,E).cnf())`.


* HADAMARD:

Funkciji **hadamard(n)**, ki se (oziroma se bo nekoč) nahaja v istoimenski datoteki, moramo podati le velikost kvadratne matrike n, da dobimo SAT obliko zapisa problema. Za program se je javila :octopus:, tako da bo najbrž trajalo. Je cepljena proti hitrosti. Nekoč kasneje pa bo seveda dodano tudi preverjanje.


* SUDOKU:

Problem rešljivosti sudokuja na SAT obliko prevedemo s klicem funkcije **sudoku(polja)** istoimenske datoteke. Kot argument ji podamo seznam zasedenih polj, torej tistih, čigar vrednost je že podana. Polja predstavimo s trojicami (i, j, k), kjer je i vrstica in j stolpec polja, k pa vrednost, ki se nahaja v njem.
Funkcija ne preverja, ali so v zasedenih poljih res vrednosti med 1 in 9. (Verjamemo, da nihče ni tak buhtelj, da bi se dejansko potrudil vstaviti kaj čudnega... Hvala ker se s tem strinjaš! :smiley:)

Primer uporabe: `formula = sudoku([(1,1,9),(1,2,2),(3,4,5)])`

Pravilnost implementacije dpllja se lahko na teh dobljenih "sudoku SAT formulah" preverja (oz. se bo nekoč v bližnji prihodnosti lahko preverjala) na dva načina: s pomočjo datotek *primeri* in *resljivostSudoku*, ali pa s programom *sudokuji*. 

In sicer je za prvi način potrebno v katerega izmed sudokujev, ki so zapisani v datoteki *primeri* (.txt), vstaviti željena zasedena polja, nato pa zagnati program *resljivostSudoku* (Zaenkrat je to testiranje okorno, saj bi naj preverilo le tri oz. vse tri sudokuje, ki so napisani v njej, dodajanje novih za delovanje programa ni dovoljeno. Pravtako ima težave z izpisom rešitev v človeku prijazni obliki. Stvar torej še ne deluje, zato ne priporočamo zagona! ).

Drugi način testiranja, ki pa celo že deluje ( :grey_exclamation: ), je možno izvesti preko zagona skripte *sudokuji*. Program bo izvedel testiranje na 10 random generiranih sudokujih, ter na praznem in na petih rešljivih (povzetih z [interneta](http://www.websudoku.com/)), že podanih sudokujih.
Glavna pomanjkljivost tega programa: vnašanje sudokujev ni možno v človeku prijazni, pregledni obliki.

Seveda lahko rešljivost sudokuja (imenujmo ga MOJSUDOKU) preveriš tudi ročno: `dpll(sudoku(MOJSUDOKU).cnf())`. Kot je razloženo že v opisu *dpll*-ja, v primeru nerešljivosti ta klic vrne 0, sicer pa slovar.

Spremenljivke v slovarju, ki ga dobimo po klicu dpll-ja na nekem sudoku-ju, imajo zopet obliko trojic i,j,k, ki predstavljajo trditev, da v rešenem sudokuju na mesto v i-ti vrstici in j-tem stolpcu spada število k.

Kot že omenjeno, s pomočjo preverjanj rešljivosti sudokujev primerjamo tudi čas delovanja 'različnih' (po št. čistih pojavitev) dpll-jev. (To je opisano zgoraj, v rubriki dodatno.)

* POVEZANOST GRAFA: je :toilet:.

* ... :soon: (or not)


===

###### Neodpravljene težave in dodatne informacije o delovanju programov:

Dpll deluje, preverjanje na grafih tudi, medtem ko eden izmed programov za preverjanje njegovega delovanja preko rešljivosti sudokujev ni popolnoma končan. Mogoče je ročno klicanje dpll-ja na nekem sudokuju: `dpll(sudoku(NEK SUDOKU).cnf())`, ali preverjanje s pomočjo zagona programa *sudokuji*, program *resljivostSudoku* pa žal potrebuje še kar nekaj popravkov. Končan bo predvidoma: :soon: .

Hitrost: Na praznem sudokuju, kjer zaradi "neliteralnosti" vseh stavkov in "nevsebovanja čistih pojavitev" (na začetku) vzame največ časa, traja slabi dve minuti. Veliko časa vzame pretvorba formul na cnf obliko (vsaj 10 sekund).
Ob zagonu programa *primerjavaCasov* je mozno opaziti tudi, da v splošnem naša implementacija čiste pojavitve v funkciji **dpll** zadev sploh ne pohitri. Najhitreje deluje tista implementacija, kjer se čista pojavitev sicer preverja, a le takoj na začetku, ob klicu funkcije 
(to pa je iplementacija s funkcijo **dpll_brez_ciste** v skriptki *dpll_ena_cista_pojavitev*).
