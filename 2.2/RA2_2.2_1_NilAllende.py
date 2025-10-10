# Autor: Nil Allende Solé       
# Data: 1-10-2025
# Versió: 1
# Descripció: Aquest programa fa un compte atras de 10 segons per despres dir "feliç any nou!"
# Especificacions d'entrada: 

from time import sleep
num = 10
while num >=0:
    print(num)
    num = num-1
    sleep(0.5)
sleep(1)
print("Feliç any nou!")