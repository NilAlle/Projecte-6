# Autor: Nil Allende Solé       
# Data: 21-1-2026
# Versió: 1
# Descripció: Alumne amb edat controlada Classe Alumne amb atribut privat __edat. El setter no accepta valors negatius El getter retorna l’edat
# Especificacions d'entrada:

class joc:
    def __init__(self):
        self.__puntuacio = 0

    def puntuacio(self):
        return self.__puntuacio

    def sumar_punts(self, punts):
        if punts < 0:
            raise ValueError("No es poden sumar punts negatius")
        self.__puntuacio += punts

    def reiniciar_puntuacio(self):
        self.__puntuacio = 0