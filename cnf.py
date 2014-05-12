# Cnf oblika za formule

class Cnf():
    def __init__(self, lst):
        self.stavki = lst

    def __repr__(self):
        return "CNF" + str(self.stavki)

class Stavek():
    def __init__(self, lst):
        self.literali = lst

    def __repr__(self):
        return "Stavek" + str(self.literali)

class Lit():
    """Atom."""

    def __init__(self, x):
        self.ime = x

    def __repr__(self):
        return self.ime

    def __eq__(self,other):
        if type(other)==Lit:
            return self.ime==other.ime
        else:
            return False
    def __hash__(self):
        return hash(repr(self))

class Til():
    """Negiran atom."""

    def __init__(self, x):
        self.ime = x

    def __repr__(self):
        return "~" + self.ime

    def __eq__(self,other):
        if type(other)==Til:
            return self.ime==other.ime
        else:
            return False

    def __hash__(self):
        return hash(repr(self))
