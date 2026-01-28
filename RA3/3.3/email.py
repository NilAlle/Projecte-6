# Autor: Nil Allende Solé       
# Data: 21-1-2026
# Versió: 1
# Descripció:
# Especificacions d'entrada:



class EmailNotificador:
    def enviar (self, missatge):
        print(f"Enviant email: {missatge}")

class Comanda:
   
    def __init__(self, client, notificador):
        self.client = client
        self.notificador = notificador
   
    def confirmar(self):
        print(f"Comanda confirmada per {self.client}")
        self.notificador.enviar (f"Hola {self.client}, la teva comanda ha estat confirmada.")


servei = EmailNotificador()
comanda = Comanda('Nil', servei)
comanda.confirmar()