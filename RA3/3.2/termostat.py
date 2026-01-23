# Autor: Nil Allende Solé       
# Data: 21-1-2026
# Versió: 1
# Descripció:Crea una classe Termostat amb un atribut privat __temperatura. Afegeix: un getter i setter amb @property i el setter només accepta valors entre 10 i 30 °C
# Especificacions d'entrada:

class termostat:
    def __init__(self, temperatura):
        self.__temperatura = temperatura

    @property
    def temperatura(self):
        return self.__temperatura

    @temperatura.setter
    def temperatura(self, valor):
    
        if 10 <= valor <= 30:
            self.__temperatura = valor




