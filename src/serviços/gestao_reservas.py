class GestaoReservas:
    def __init__(self):
        self._reservas = []

    def adicionar(self, reserva):
        self._reservas.append(reserva)

    def listar(self):
        return self._reservas
