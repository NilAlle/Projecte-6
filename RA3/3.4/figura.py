# Autor: Nil Allende Solé       
# Data: 28-1-2026
# Versió: 1
# Descripció:
# Especificacions d'entrada:


import math

class figura:
    def area():
        print('Area no definida')
    
class cuadrat(figura):
    def __init__ (self, costat):
        self.costat = costat

    def area(self):
        return self.costat * self.costat
    
class cercle(figura):
    def __init__(self, radi):
        self.radi = radi
    
    def area(self):
        return  math.pi*self.radi**2

