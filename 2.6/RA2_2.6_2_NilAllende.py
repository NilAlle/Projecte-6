# Autor: Nil Allende Solé
# Data: 14/10/2025
# Versió: 1
# Descripció: Crea un fitxer de text anomenat "sortida.txt" i escriu diverses línies de text en ell utilitzant el mètode writelines().
# Instruccions de entrada: 

linies = [
    "Primera linia\n",
    "Segona linia\n",
    "Tercera linia\n"
]

with open("sortida.txt", "w") as f:
    f.writelines(linies)