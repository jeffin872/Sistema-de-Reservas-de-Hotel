class GestaoReservas:
    def __init__(self):
        self._reservas = []

    def adicionar(self, reserva):
        self._reservas.append(reserva)

    def listar(self):
        return self._reservas

    def salvar(self):
        from persistencia.persistencia__json import salvar_reservas
        salvar_reservas(self._reservas)
