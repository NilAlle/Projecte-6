# Autor: Nil Allende Solé       
# Data: 14-1-2026
# Versió: 1
# Descripció:1. Crea una classe Llibre; Atributs: títol, autor, any; Mètode mostrar_info() per imprimir les dades
# Especificacions d'entrada:

class llibre:
    def __init__(self, titol, autor, any):
        self.titol = titol
        self.autor = autor
        self.any = any
    
    def mostrar_info(self):
        print('El llibre:', self.titol, 'és de', self.autor, 'i és del', self.any)
