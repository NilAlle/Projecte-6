# Autor: Nil Allende Solé       
# Data: 28-1-2026
# Versió: 1
# Descripció:
# Especificacions d'entrada:

class Missatger:
    def __init__(self, remitent):
        self.remitent = remitent
    
    def enviar(self, destinatari, missatge):
        return f"Missatge envirat a {destinatari}: {missatge}"

class Email(Missatger):
    def enviar(self, destinatari, missatge):
        return f"[EMAIL] De: {self.remitent} → A: {destinatari}\n   Missatge: {missatge}"

class SMS(Missatger):
    def enviar(self, destinatari, missatge):
        missatge_curt = missatge[:160] if len(missatge) > 160 else missatge
        return f"[SMS] De: {self.remitent} → A: {destinatari}\n   Missatge: {missatge_curt}"

class WhatsApp(Missatger):
    def enviar(self, destinatari, missatge):
        return f"[WHATSAPP] De: {self.remitent} → A: {destinatari}\n   Missatge: {missatge}"

class Telegram(Missatger):
    def enviar(self, destinatari, missatge):
        return f"[TELEGRAM] De: {self.remitent} → A: {destinatari}\n   Missatge: {missatge}"