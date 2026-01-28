# Autor: Nil Allende Solé       
# Data: 21-1-2026
# Versió: 1
# Descripció:
# Especificacions d'entrada:


class ImpressoraPDF:
    def imprimir (self, contingut):
        print(f"Imprimint PDF: {contingut}")

class Factura:
    
    def __init__(self, client, import_total, impressora):
        self.client = client
        self.import_total = import_total
        self.impressora = impressora
    
    def imprimir_factura(self):
        contingut = f"Factura per a {self.client}, total: {self.import_total} €" 
        self.impressora.imprimir(contingut)


impressora = ImpressoraPDF()
factura = Factura('Nil', 100, impressora)
factura.imprimir_factura()