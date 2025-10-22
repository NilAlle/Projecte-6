# Autor: Nil Allende Solé       
# Data: 22-10-2025
# Versió: 1
# Descripció: Demana a l'usuari un nombre enter i imprimeix tots els nombres primers des de 2 fins a aquest nombre.​
# Especificacions d'entrada: demana a l'usuari un número

try:
    num = int(input("Posa un número enter: "))
    if num < 2:
        print("No hi ha nombres primers <=", num)
    else:
        print("Nombres primers de 2 a", num, ":")
        for i in range(2, num + 1):
            primer = True
            for d in range(2, i):
                if i % d == 0:
                    primer = False
                    break
            if primer:
                print(i)

except ValueError:
    print("Has de posar un número enter.")

