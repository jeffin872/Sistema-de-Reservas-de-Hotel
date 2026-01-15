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

    @numero.setter
    def numero(self, numero):
        self.__numero = numero

    @property
    def capacidade(self):
        return self.__capacidade
    
    @capacidade.setter
    def capacidade(self, capacidade):
        self.__capacidade = capacidade

    #modelo não tem setter porque não pode ser alterado depois de criado
    @property
    def modelo(self):
        return self.__modelo
    
    @property
    def disponivel(self):
        return self.__disponivel
    
    @disponivel.setter
    def disponivel(self, disponivel):
        self.__disponivel = disponivel
    
    #valor não tem setter porque não é recomendavel ser adicionado dentro do setter, só por meio de métodos específicos
    @property
    def valor_diaria(self):
        return self.__valor_diaria
    
    def liberar_quarto(self):
        self.__disponivel = True

    def ocupar_quarto(self):
        self.__disponivel = False
        