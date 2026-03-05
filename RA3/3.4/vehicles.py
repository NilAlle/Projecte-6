# Autor: Nil Allende Solé       
# Data: 28-1-2026
# Versió: 1
# Descripció:
# Especificacions d'entrada:

class vehicles:
    def __init__ (self, marca):
        self.marca = marca
    
    def arrencar (self):
        print(self.marca, 'està arrencant...')


class cotxe(vehicles):
    def claxon (self):
        print('pip pip!')

