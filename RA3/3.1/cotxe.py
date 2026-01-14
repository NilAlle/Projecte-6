# Autor: Nil Allende Solé       
# Data: 14-1-2026
# Versió: 1
# Descripció:1. Crea una classe Cotxe; Atributs: marca, model, any; Mètode per mostrar la informació del cotxe
# Especificacions d'entrada:

class Cotxe:
    def __init__(self, marca, model, any):
        self.marca = marca
        self.model = model
        self.any = any
    
    def descriure(self):
        print('cotxe:', self.marca, self.model, "de l'any ", self.any)
