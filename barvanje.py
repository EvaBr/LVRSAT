################################################################################
#                                   Barvanje                                   #
#                                                                              #
#  Funkcija barvanje sprejme število vozlišč ter seznam parov, ki              #
#    predstavljajo povezave grafa in vrne formulo za barvanje grafa s tremi    #
#    barvami.                                                                  #
#                                                                              #
#  Primer uporabe: barvanje(5,[(1,2),(2,3)])                                   #
#                                                                              #
#                                                                              #
#  Funkcija kbarvanje sprejme število barv, število vozlišč ter seznam parov,  #
#    ki predstavljajo povezave grafa in vrne formulo za barvanje grafa s k     #
#    barvami.                                                                  #
#                                                                              #
#  Primer uporabe: kbarvanje(4, 3, [(1,2),(2,3)])                              #
#                                                                              #
################################################################################

from boolean import *

def barvanje(n, E):
    prva = T()
    druga = T()
    tretja = T()

    #vsako vozlišče je pobarvano vsaj z eno barvo
    for i in range(1,n+1):
        prva = In(Ali(Spr("c{0}1".format(i)), Spr("c{0}2".format(i)), Spr("c{0}3".format(i))), prva)
    prva=prva.poenostavi()

    #eno vozlišče ni pobarvano z več kot eno barvo
    for i in range(1,n+1):
        druga = In(druga, In(Neg(In(Spr("c{0}1".format(i)),Spr("c{0}2".format(i)))),
                   Neg(In(Spr("c{0}1".format(i)),Spr("c{0}3".format(i)))),Neg(In(Spr("c{0}3".format(i)),Spr("c{0}2".format(i))))))
    druga=druga.poenostavi()

    #sosednji vozlišči sta različnih barv
    for pov in E:
        tretja = In(tretja, In(Neg(In(Spr("c{0}1".format(pov[1])),Spr("c{0}1".format(pov[0])))),
                  Neg(In(Spr("c{0}2".format(pov[1])),Spr("c{0}2".format(pov[0])))),
        Neg(In(Spr("c{0}3".format(pov[1])),Spr("c{0}3".format(pov[0]))))))
    tretja=tretja.poenostavi()
    
    form = In(prva,druga,tretja)
    return form.poenostavi()



###############################

def kbarvanje(K, n, E):
    prva = T()
    druga = T()
    tretja = T()

    #vsako vozlišče je pobarvano vsaj z eno barvo
    for i in range(1,n+1):
        prva = In(prva, *tuple(Ali(Spr(("c{0}"+str(j)).format(i)), Spr(("c{0}"+str(j)).format(i)), Spr(("c{0}"+str(j)).format(i))) for j in range (1,K+1)))
    prva=prva.poenostavi()

    #eno vozlišče ni pobarvano z več kot eno barvo
    for i in range(1,n+1):
        druga = In(druga, In(*tuple (Ali(Neg(Spr(("c{0}"+str(j)).format(i))),Neg(Spr(("c{0}"+str(k)).format(i)))) for j in range (1,K+1) for k in range (j+1,K+1))))
    druga=druga.poenostavi()
    
    #sosednji vozlišči sta različnih barv
    for pov in E:
        tretja = In(tretja, In(*tuple(Ali(Neg(Spr(("c{0}"+str(j)).format(pov[1]))),Neg(Spr(("c{0}"+str(j)).format(pov[0])))) for j in range (1,K+1))))
    tretja=tretja.poenostavi()
    
    form = In(prva,druga,tretja)
    return form.poenostavi()














