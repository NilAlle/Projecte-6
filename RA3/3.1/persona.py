# Autor: Nil Allende Solé       
# Data: 14-1-2026
# Versió: 1
# Descripció:Crea una classe Persona; Atributs: nom, edat; Mètode presentar_se() que imprimeixi “Hola, soc X i tinc Y anys”
# Especificacions d'entrada:

class persona:
    def __init__(self, nom, edat):
        self.nom = nom
        self.edat = edat
    
    def presentarse(self):
        print('Hola soc', self.nom, 'i tinc', self.edat)




