# Autor: Nil Allende Solé
# Data: 7/10/2025
# Versió: 1
# Descripció: Fes un programa que mostri la data i hora actual i la formati de manera llegible (dd/mm/yyyy hh:mm).
# Especificacions de entrada: 


from datetime import datetime
hora_actual = datetime.now()
data_formatejada = hora_actual.strftime("%d/%m/%Y %H:%M")
print("La data i hora actual és:", data_formatejada)

data_nadal = datetime(hora_actual.year, 12, 25)  
dies_fins_nadal = (data_nadal - hora_actual).days
print("Queden", dies_fins_nadal, "dies per Nadal")