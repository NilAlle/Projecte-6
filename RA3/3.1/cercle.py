# Autor: Nil Allende Solé       
# Data: 14-1-2026
# Versió: 1
# Descripció:Crea una classe Cercle; Atribut: radi; Mètodes: calcular àrea i perímetre
# Especificacions d'entrada:

class cercle:
    def __init__(self, radi):
        self.radi = radi

   
    def area(self):
       print("L'area és: ", 3.141592 * self.radi**2)
   
    def perimetre(self):
       print("El perímetre és: ", 2 * 3.141592 * self.radi)