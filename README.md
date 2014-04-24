:hibiscus: LVRSAT :hibiscus:
========

### Projekt: SAT solver in prevedba nekaterih problemov na SAT obliko.


###### Ekipa: Teja Tement :bee:, Bojan Bauman :beer: in Eva Breznik :octopus: .


![Zaenkrat kr ena random slikica...](/slikica.gif)


Projekt je razdeljen na dva dela:

:one: Prevedba nekaj znanih problemov na SAT obliko, datoteki: ?Convert2Sat? in ?C2Stesti?,

:two: SAT solver (implementacija dpll algoritma), datoteke: boolean, cnf, dpll in primeri. 

===
##### Prevedba problemov na SAT obliko
V datoteki *?Convert2Sat?* se nahajajo funkcije, ki izpišejo SAT obliko posamičnih problemov. Imena in uporaba funkcij po problemih:

* 3COL:

Funkcijo **barvanje(n, E)** pokličemo na številu vozlišč n in seznamu povezav (tj. seznamu dvojic) E. Seveda nam vozlišča predstavljajo števila od 1 do n, zato je potrebno tudi povezave E podati s tovrstnimi oznakami.
??tu dodaj kako delujejo preverbe/testi??

* Hadamard:

Funkciji **hadamard(n)** moramo podati le velikost kvadratne matrike n.

* Sudoku

* Povezanost grafa

* ...

===
##### SAT solver
V datoteki *boolean* se nahajajo definicije logičnih objektov, ki jih potrebujemo v vseh ostalih programih. Datoteka *Cnf*  pravtako vsebuje definicije ...
