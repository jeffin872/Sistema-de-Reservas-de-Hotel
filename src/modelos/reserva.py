from datetime import date

class Reserva:
    def __init__(self, hospede, quarto, data_entrada, data_saida):
        if not quarto.disponivel:
            raise ValueError("Quarto indisponível")

        self.__hospede = hospede
        self.__quarto = quarto
        self.__data_entrada = data_entrada
        self.__data_saida = data_saida

        self.__quarto.ocupar_quarto()

    @property
    def hospede(self):
        return self.__hospede

    @property
    def quarto(self):
        return self.__quarto

    @property
    def data_entrada(self):
        return self.__data_entrada

    @property
    def data_saida(self):
        return self.__data_saida

    def calcular_duracao(self):
        return (self.__data_saida - self.__data_entrada).days

    def calcular_valor_total(self):
        return self.calcular_duracao() * self.__quarto.valor_diaria

    def encerrar(self):
        self.__quarto.liberar_quarto()
