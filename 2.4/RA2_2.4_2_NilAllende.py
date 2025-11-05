# Autor: Nil Allende Solé       
# Data: 31-10-2025
# Versió: 1
# Descripció: Demana una frase i compta quantes vocals conté.
# Especificacions d'entrada: demana a l'usuari una cadena de caracters

text = str(input("Introdueix una línnia de caràcters "))
contador = 0
vocals = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
num_vocals = 0

while contador < (len(text)):
    if text[contador] in vocals:
        num_vocals += 1
    contador += 1
print("la teva cadena té", num_vocals, "vocals")
