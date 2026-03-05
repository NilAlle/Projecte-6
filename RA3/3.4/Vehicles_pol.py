# Autor: Nil Allende Solé       
# Data: 28-1-2026
# Versió: 1
# Descripció:
# Especificacions d'entrada:

class Vehicle:
    def __init__(self, nom, velocitat_maxima):
        self.nom = nom
        self.velocitat_maxima = velocitat_maxima
        self.posicio = 0
    
    def moure(self, distancia):
        self.posicio += distancia
        return f"{self.nom} es mou {distancia}m. Posició: {self.posicio}m"
    
    def obtenir_info(self):
        return f"{self.nom} (Velocitat máx: {self.velocitat_maxima}km/h, Posició: {self.posicio}m)"

class Cotxe(Vehicle):
    def moure(self, distancia):
        self.posicio += distancia
        return f"{self.nom} es mou {distancia}m per carretera a {self.velocitat_maxima}km/h. Posició: {self.posicio}m"

class Bicicleta(Vehicle):
    def moure(self, distancia):
        distancia_real = distancia * 0.6
        self.posicio += distancia_real
        return f"{self.nom} es mou {distancia_real:.1f}m per carril bici a {self.velocitat_maxima}km/h. Posició: {self.posicio:.1f}m"

class Barca(Vehicle):
    def moure(self, distancia):
        distancia_real = distancia * 1.2
        self.posicio += distancia_real
        return f"{self.nom} navega {distancia_real:.1f}m pel riu a {self.velocitat_maxima}km/h. Posició: {self.posicio:.1f}m"

class Autobús(Vehicle):
    def moure(self, distancia):
        distancia_real = distancia * 0.8
        self.posicio += distancia_real
        return f"{self.nom} es mou {distancia_real:.1f}m per carretera a {self.velocitat_maxima}km/h. Posició: {self.posicio:.1f}m"

class Tren(Vehicle):
    def moure(self, distancia):
        self.posicio += distancia
        return f"{self.nom} avança {distancia}m per les vies a {self.velocitat_maxima}km/h. Posició: {self.posicio}m"
