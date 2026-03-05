# Autor: Nil Allende Solé       
# Data: 28-1-2026
# Versió: 1
# Descripció:
# Especificacions d'entrada:


class llibre:
    def __init__(self, titol, autor):
        self.titol = titol
        self.autor = autor

    def mostrar_info(self):
        print('el titol és', self.titol, "i l'autor", self.autor)


class llibrepaper(llibre):
    def __init__ (self, n_pagines):
        self.n_pagines = n_pagines

    def mostrar_info(self):
        print('el número de pàgines és', self.n_pagines)

class llibredigital(llibre):
    def __init__(self, format):
        self.format = format

    def mostrar_info(self):
        print('amb el format', self.format)
