# Autor: Nil Allende Solé       
# Data: 28-1-2026
# Versió: 1
# Descripció:
# Especificacions d'entrada:


#vehicles#########################################################

from vehicles import cotxe

cotxe1 = cotxe('BMW')
cotxe1.arrencar()
cotxe1.claxon()


#animals#########################################################

from animals import animal
from animals import gos
from animals import gat


a = animal()
g = gos()
g1 = gat()

a.parlar()
g.parlar()
g1.parlar()

#persona#########################################################

from persona import persona
from persona import treballador

persona1 = persona('Nil', 18)
persona1.saludar()

treballador1 = treballador('informatic')
treballador1.mostrar_feina()

#figura#########################################################

from figura import figura
from figura import cercle
from figura import cuadrat

figura1 = figura.area()

cuadrat1 = cuadrat(10)
print(cuadrat1.area())

cercle1 = cercle(3)
print(cercle1.area())

#figura#########################################################

from biblioteca import llibre
from biblioteca import llibrepaper
from biblioteca import llibredigital

llibre1 = llibre ('titol1', 'autor1')
llibre1.mostrar_info()

llibre2 = llibrepaper('300')
llibre2.mostrar_info()

llibre3 = llibredigital('PDF')
llibre3.mostrar_info()

##########################################################

