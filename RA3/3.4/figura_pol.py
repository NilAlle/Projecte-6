# Autor: Nil Allende Solé       
# Data: 28-1-2026
# Versió: 1
# Descripció:
# Especificacions d'entrada:

import math

class Figura:
    def dibuixar(self):
        return "Una figura genèrica"
    
    def calcular_area(self):
        return 0

class Cercle(Figura):
    def __init__(self, radi):
        self.radi = radi
    
    def dibuixar(self):
        return f"Un cercle de radi {self.radi}"
    
    def calcular_area(self):
        return math.pi * self.radi ** 2

class Quadrat(Figura):
    def __init__(self, costat):
        self.costat = costat
    
    def dibuixar(self):
        return f"Un quadrat de costat {self.costat}"
    
    def calcular_area(self):
        return self.costat ** 2

class Triangle(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def dibuixar(self):
        return f"Un triangle de base {self.base} i altura {self.altura}"
    
    def calcular_area(self):
        return (self.base * self.altura) / 2

class Rectange(Figura):
    def __init__(self, amplada, alçada):
        self.amplada = amplada
        self.alçada = alçada
    
    def dibuixar(self):
        return f"Un rectange de {self.amplada}x{self.alçada}"
    
    def calcular_area(self):
        return self.amplada * self.alçada