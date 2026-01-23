# Autor: Nil Allende Solé       
# Data: 21-1-2026
# Versió: 1
# Descripció: Classe Rellotge amb atribut __hores. El setter només accepta valors entre 0 i 23. Afegeix mètode per mostrar les hores en format “HH:00”
# Especificacions d'entrada:

class rellotge:
    def __init__(self, hores):
        self.__hores = hores
    
    def canviar_hora(self, nova_hora):
        if 0 <= nova_hora <= 23:
            self.__hores = nova_hora

    def mostrar_hora(self):
        return f"{self.__hores:02d}:00"


