# Autor: Nil Allende Solé       
# Data: 14-1-2026
# Versió: 1
# Descripció:Crea una classe Punt; Atributs: x, y; Mètode: calcular la distància a un altre punt
# Especificacions d'entrada:

class punt:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distancia(self):
        print('La distància és:', (self.x**2 + self.y**2)**0.5)
    