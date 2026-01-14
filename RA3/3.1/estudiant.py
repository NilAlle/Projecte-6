# Autor: Nil Allende Solé       
# Data: 14-1-2026
# Versió: 1
# Descripció:Crea una classe Estudiant; Atributs: nom, nota; Mètode: dir si ha aprovat o no (nota ≥ 5)

# Especificacions d'entrada:

class estudiant:
    def __init__(self, nom, nota):
        self.nom = nom
        self.nota = nota
    
    def aprovat(self):
        if self.nota >= 5:
            print("L'alumne ", self.nom, "ha aprovat.")
        else:
            print("L'alumne ", self.nom, "ha suspés.")
