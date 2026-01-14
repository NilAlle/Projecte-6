# Autor: Nil Allende Solé       
# Data: 14-1-2026
# Versió: 1
# Descripció:Crea una classe Producte; Atributs: nom, preu; Mètode: aplicar un descompte (donat com a percentatge)

# Especificacions d'entrada:

class producte:
    def __init__(self, nom, preu):
        self.nom = nom
        self.preu = preu
    
    def descompte(self):
        print('El producte', self.nom, 'costa', self.preu * 0.9, '€ amb descompte del 10%')
