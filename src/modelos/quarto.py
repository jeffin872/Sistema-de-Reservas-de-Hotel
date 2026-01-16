class Quarto:
    def __init__(self, numero, capacidade, modelo, valor_diaria):
        self.__numero = numero
        self.__capacidade = capacidade
        self.__modelo = modelo
        self.__disponivel = True
        self.__valor_diaria = valor_diaria

    @property
    def numero(self):
        return self.__numero

    @property
    def capacidade(self):
        return self.__capacidade

    @property
    def modelo(self):
        return self.__modelo

    @property
    def disponivel(self):
        return self.__disponivel

    @property
    def valor_diaria(self):
        return self.__valor_diaria

    def liberar_quarto(self):
        self.__disponivel = True

    def ocupar_quarto(self):
        self.__disponivel = False
