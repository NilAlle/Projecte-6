# Autor: Nil Allende Solé       
# Data: 28-1-2026
# Versió: 1
# Descripció:
# Especificacions d'entrada:

class persona:
    def __init__ (self, nom, edat):
        self.nom = nom
        self.edat = edat
    
    def saludar (self):
        print('Hola, sóc ', self.nom)


class treballador(persona):
    def __init__ (self, feina):
        self.feina = feina
    
    def mostrar_feina(self):
        print('Treballo de ', self.feina)


