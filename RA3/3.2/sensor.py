# Autor: Nil Allende Solé       
# Data: 21-1-2026
# Versió: 1
# Descripció:Classe Sensor amb atribut privat __valor. El setter: només permet valors entre 0 i 100 i el getter retorna el valor actual
# Especificacions d'entrada:

class sensor:
    def __init__(self, valor):
        self.__valor = valor

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, nou_valor):
        if 0 <= nou_valor <= 100:
            self.__valor = nou_valor

