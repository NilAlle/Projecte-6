# Autor: Nil Allende Solé       
# Data: 14-1-2026
# Versió: 1
# Descripció:1. Crea una classe Rectangle; Atributs: amplada, alçada; Mètodes: area() i perimetre()
# Especificacions d'entrada:

class rectangle:
    def __init__(self, amplada, alçada):
        self.amplada = amplada
        self.alçada = alçada
    
    def area(self):
        print("L'area del rectangle és: ", self.amplada * self.alçada)
    def perimetre(self):
        print('El perímetre del rectangle és: ', 2 * (self.amplada + self.alçada))

