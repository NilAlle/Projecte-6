# Autor: Nil Allende Solé       
# Data: 14-1-2026
# Versió: 1
# Descripció:Crea una classe Animal; Atributs: nom, espècie; Mètode fer_soroll() que mostri un text genèric (“fa un soroll”)
# Especificacions d'entrada:

class animal:
    def __init__(self, nom, especie):
        self.nom = nom
        self.especie = especie

   
    def soroll(self):
       print("fa un soroll")
