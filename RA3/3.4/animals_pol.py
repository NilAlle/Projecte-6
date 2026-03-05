# Autor: Nil Allende Solé       
# Data: 28-1-2026
# Versió: 1
# Descripció:
# Especificacions d'entrada:

class Animal:
    def __init__(self, nom):
        self.nom = nom
    
    def fer_soroll(self):
        return "L'animal fa un so"

class Gat(Animal):
    def fer_soroll(self):
        return "Miau"

class Vaca(Animal):
    def fer_soroll(self):
        return "Muuu"

class Gos(Animal):
    def fer_soroll(self):
        return "Guau guau"

class Lloro(Animal):
    def fer_soroll(self):
        return "Cra cra"