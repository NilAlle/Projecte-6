# Autor: Nil Allende Solé       
# Data: 14-1-2026
# Versió: 1
# Descripció:
# Especificacions d'entrada:


# Cotxe #####################################################################

from cotxe import Cotxe

cotxe1 = Cotxe('Audi', 'A4', 2007)
cotxe2 = Cotxe('Lamborgini', 'Venom', 2013)

cotxe1.descriure()
cotxe2.descriure()

# Rectangle #####################################################################

from rectangle import rectangle

rectangle1 = rectangle(4,9)
rectangle2 = rectangle(2,6)
rectangle3 = rectangle(3,4)

rectangle1.area()
rectangle1.perimetre()
rectangle2.area()
rectangle2.perimetre()
rectangle3.area()
rectangle3.perimetre()

# Persona #####################################################################

from estudiant import estudiant

estudiant1 = estudiant('Nil', 2)
estudiant2 = estudiant('Gerard', 1)
estudiant3 = estudiant('Marc', 7)

estudiant1.aprovat()
estudiant2.aprovat()
estudiant3.aprovat()

# Compte Bancari #####################################################################

from comptebancari import comptebancari
compte1 = comptebancari(1500)

compte1.ingressar()
compte1.retirar()
compte1.retirar()

# Productes #####################################################################

from producte import producte
producte1 = producte('Pa', 15)
producte2 = producte('Llet', 9)
producte3 = producte('Formatge', 6)

producte1.descompte()
producte2.descompte()
producte3.descompte()

# Punts #####################################################################

from punt import punt
punt1 = punt(3,4)

punt1.distancia()

# Animal #####################################################################

from animal import animal

class gos(animal):
    def soroll(self):
        print('bup bup!')

gos1= gos('Toby', 'gos')
gos1.soroll()

# Llibreria #####################################################################

from llibre import llibre
class biblioteca(llibre):
    def __init__(self):
        self.llistallibres = []
    
    def afegir_llibre(self, llibre):
        self.llistallibres.append(llibre)
    
    def mostrar_llibres(self):
        for llibre in self.llistallibres:
            print("Títol:", llibre.titol, ", Autor:", llibre.autor)

biblioteca1 = biblioteca()
llibre1 = llibre("El Quijote", "Cervantes", 1605)
llibre2 = llibre("1984", "George Orwell", 1949)

biblioteca1.afegir_llibre(llibre1)
biblioteca1.afegir_llibre(llibre2)
biblioteca1.mostrar_llibres()

# Cercle #####################################################################

from cercle import cercle
cercle1 = cercle(4)
cercle2 = cercle(5)
cercle3 = cercle(6)
cercle4 = cercle(7)
cercle5 = cercle(8)

llistat_cercles = [cercle1, cercle2, cercle3, cercle4, cercle5]
for i in llistat_cercles:
    area = 3.141592 * i.radi**2
    if area > 50:
        print("El cercle de radi", i.radi, "té àrea superior a 50:", area)

# Persones #####################################################################

from persona import persona
persona1 = persona("Nil", 21)
persona2 = persona("Gerard", 88)
persona3 = persona("Marc", 39)

llistat_persones = [persona1, persona2, persona3]
for i in llistat_persones:
    if i.edat > 30:
        i.presentarse()
