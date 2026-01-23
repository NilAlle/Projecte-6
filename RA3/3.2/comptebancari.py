# Autor: Nil Allende Solé       
# Data: 21-1-2026
# Versió: 1
# Descripció: Classe amb un atribut privat (__Saldo) i amb metodes publics per ingressar, retirar o veure els diners.
# Especificacions d'entrada:

class comptebancari:
    def __init__(self, saldo):
        self.__saldo = saldo

    def consultar_saldo(self):
        return self.__saldo

    def ingressar(self, quantitat):
        self.__saldo = self.__saldo + quantitat

    def retirar(self, quantitat):
        self.__saldo = self.__saldo - quantitat
