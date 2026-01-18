class Reserva:
    def __init__(self, hospede, quarto, dias, pagamento, configuracao):
        self._hospede = hospede
        self._quarto = quarto
        self._dias = dias
        self._pagamento = pagamento
        self._config = configuracao

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

    #  Regras de Estado 
    def confirmar(self):
        if self._estado != "CRIADA":
            raise Exception("Reserva não pode ser confirmada neste estado.")
        self._estado = "CONFIRMADA"
        self._quarto.ocupar()

    def cancelar(self):
        if self._estado not in ["CRIADA", "CONFIRMADA"]:
            raise Exception("Reserva não pode ser cancelada.")
        self._estado = "CANCELADA"
        self._quarto.liberar()

    def finalizar(self):
        if self._estado != "CONFIRMADA":
            raise Exception("Reserva não pode ser finalizada.")
        self._quarto.ocupar()     
        self._estado = "FINALIZADA"

    def marcar_no_show(self):
        if self._estado != "CONFIRMADA":
            raise Exception("No-show inválido.")
        self._estado = "NO_SHOW"

    #  Cálculo 
    def calcular_total(self):
        diaria = self._quarto.valor_total_diaria()
        return diaria * self._dias
