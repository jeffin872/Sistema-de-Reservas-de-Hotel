class Reserva:
    def __init__(self, cliente, quarto, data_entrada, data_saida):
        self.__cliente = cliente
        self.__quarto = quarto
        self.__data_entrada = data_entrada
        self.__data_saida = data_saida

    @property
    def cliente(self):
        return self.__cliente
    
    @property
    def quarto (self):
        return self.__quarto
    
    @quarto.setter
    def quarto(self, novo_quarto):
        if novo_quarto.disponivel:
            self.__quarto.liberar_quarto()
            self.__quarto = novo_quarto
            self.__quarto.ocupar_quarto()
        else:
            print("Quarto não está disponível para reserva.")