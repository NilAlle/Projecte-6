# Autor: Nil Allende Solé       
# Data: 21-1-2026
# Versió: 1
# Descripció: 6. Producte amb preu controlat Classe Producte amb atributs: nom (públic) __preu (privat) Mètodes per obtenir i modificar el preu (només si > 0)

# Especificacions d'entrada:

class producte:
    def __init__(self, nom, preu):
        self.nom = nom
        self.__preu = preu

    def consultar_preu(self):
        return self.__preu
    
    def canviar_preu(self, nou_preu):
        self.__preu = nou_preu
