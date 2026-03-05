# Autor: Nil Allende Solé       
# Data: 28-1-2026
# Versió: 1
# Descripció:
# Especificacions d'entrada:


class Empleat:
    def __init__(self, nom):
        self.nom = nom
    
    def calcular_sou(self):
        return 0

class Fixe(Empleat):
    def __init__(self, nom, sou_mensual):
        super().__init__(nom)
        self.sou_mensual = sou_mensual
    
    def calcular_sou(self):
        return self.sou_mensual

class Autonom(Empleat):
    def __init__(self, nom, tarifa_hora, hores_treballades):
        super().__init__(nom)
        self.tarifa_hora = tarifa_hora
        self.hores_treballades = hores_treballades
    
    def calcular_sou(self):
        hores_normals = min(self.hores_treballades, 160)
        hores_extra = max(0, self.hores_treballades - 160)
        
        return (hores_normals * self.tarifa_hora) + (hores_extra * self.tarifa_hora * 1.5)

class Comissió(Empleat):
    def __init__(self, nom, sou_base, vendes, percentatge_comissio):
        super().__init__(nom)
        self.sou_base = sou_base
        self.vendes = vendes
        self.percentatge_comissio = percentatge_comissio
    
    def calcular_sou(self):
        comissio = (self.vendes * self.percentatge_comissio) / 100
        return self.sou_base + comissio