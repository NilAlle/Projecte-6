# Autor: Nil Allende Solé       
# Data: 21-1-2026
# Versió: 1
# Descripció:
# Especificacions d'entrada:




class CarretCompra:
  
    def __init__(self, total): 
        self.total = total

    def preu_final (self, total):
         return self.total.aplicar(total)

class descompte20:
        def aplicar(self, total):
            return total * 0.80


carretcompra = CarretCompra(descompte20())
print(carretcompra.preu_final(100))