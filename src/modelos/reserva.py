class Reserva:
    def __init__(self, hospede, quarto, dias, pagamento):
        self._hospede = hospede
        self._quarto = quarto
        self._dias = dias
        self._pagamento = pagamento
        self._estado = "CRIADA"

    @property
    def hospede(self):
        return self._hospede

    @property
    def quarto(self):
        return self._quarto

    @property
    def dias(self):
        return self._dias

    @property
    def estado(self):
        return self._estado
    

    def confirmar(self):
        self._quarto.ocupar()

    def finalizar(self):
        self._quarto.liberar()

    def calcular_total(self):
        return self._quarto.valor_total_diaria() * self._dias
