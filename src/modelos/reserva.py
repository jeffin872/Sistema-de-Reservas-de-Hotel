class Reserva:
    def __init__(self, hospede, quarto, dias, pagamento):
        if not quarto.disponivel:
            raise ValueError("Quarto indisponível")

        self._hospede = hospede
        self._quarto = quarto
        self._dias = dias
        self._pagamento = pagamento

        quarto.ocupar()

    def calcular_total(self):
        if hasattr(self._quarto, "valor_total_diaria"):
            diaria = self._quarto.valor_total_diaria()
        else:
            diaria = self._quarto.valor_diaria

        return diaria * self._dias

    def finalizar(self):
        total = self.calcular_total()
        self._pagamento.pagar(total)
        self._quarto.liberar()
