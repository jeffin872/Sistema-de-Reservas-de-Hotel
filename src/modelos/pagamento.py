class Pagamento:
    def pagar(self, valor):
        pass
class Dinheiro(Pagamento):
    def pagar(self, valor):
        print(f"Pagamento de R$ {valor:.2f} em dinheiro realizado.")

class Pix(Pagamento):
    def pagar(self, valor):
        print(f"Pagamento de R$ {valor:.2f} via Pix realizado.")
