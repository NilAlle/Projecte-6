# Autor: Nil Allende Solé       
# Data: 21-1-2026
# Versió: 1
# Descripció: Alumne amb edat controlada Classe Alumne amb atribut privat __edat. El setter no accepta valors negatius El getter retorna l’edat
# Especificacions d'entrada:

class alumne:
    def __init__(self, edat):
        self.__edat = edat
    
    def edat (self, valor):
        if 0 <= self.__edat:
            self.__edat = valor

    def mostrar_edat(self):
        print(self.__edat)


