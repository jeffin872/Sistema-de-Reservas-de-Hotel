class Quarto:
    def __init__(self, numero, capacidade, valor_diaria):
        self._numero = numero
        self._capacidade = capacidade
        self._valor_diaria = valor_diaria
        self._disponivel = True

    def valor_total_diaria(self):
        return self._valor_diaria

    @property
    def numero(self):
        return self._numero

    @property
    def capacidade(self):
        return self._capacidade

    @property
    def disponivel(self):
        return self._disponivel

    def ocupar(self):
        self._disponivel = False

    def liberar(self):
        self._disponivel = True

    def descricao(self) -> str:
        raise NotImplementedError("Este método deve ser implementado nas subclasses")

class QuartoSimples(Quarto):
    def descricao(self) -> str:
        return "Quarto Simples"



class QuartoLuxo(Quarto):
    def __init__(self, numero, capacidade, valor_diaria, taxa_luxo):
        super().__init__(numero, capacidade, valor_diaria)
        self._taxa_luxo = taxa_luxo

    def valor_total_diaria(self):
        return self._valor_diaria + self._taxa_luxo

    def descricao(self) -> str:
        return "Quarto Luxuoso"

