import json
from datetime import date, timedelta

ARQUIVO = "dados.json"


# =========================
# Classe Quarto
# =========================
class Quarto:
    def __init__(self, numero, capacidade, tarifa):
        self.numero = numero
        self.capacidade = capacidade
        self.tarifa = tarifa
        self._disponivel = True

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, valor):
        if valor <= 0:
            raise ValueError("Número do quarto inválido.")
        self._numero = valor

    @property
    def capacidade(self):
        return self._capacidade

    @capacidade.setter
    def capacidade(self, valor):
        if valor < 1:
            raise ValueError("Capacidade deve ser maior que zero.")
        self._capacidade = valor

    @property
    def tarifa(self):
        return self._tarifa

    @tarifa.setter
    def tarifa(self, valor):
        if valor <= 0:
            raise ValueError("Tarifa deve ser maior que zero.")
        self._tarifa = valor

    @property
    def disponivel(self):
        return self._disponivel

    def ocupar(self):
        self._disponivel = False

    def liberar(self):
        self._disponivel = True

    def __str__(self):
        status = "Disponível" if self.disponivel else "Ocupado"
        return f"Quarto {self.numero} | Capacidade: {self.capacidade} | R$ {self.tarifa} | {status}"


# =========================
# Classe Hospede
# =========================
class Hospede:
    def __init__(self, nome, documento):
        self.nome = nome
        self.documento = documento

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        if len(valor.strip()) < 2:
            raise ValueError("Nome inválido.")
        self._nome = valor

    @property
    def documento(self):
        return self._documento

    @documento.setter
    def documento(self, valor):
        if len(valor.strip()) < 3:
            raise ValueError("Documento inválido.")
        self._documento = valor

    def __str__(self):
        return f"{self.nome} ({self.documento})"


# =========================
# Classe Reserva
# =========================
class Reserva:
    def __init__(self, hospede, quarto, noites):
        self.hospede = hospede
        self.quarto = quarto
        self.noites = noites
        self.data_entrada = date.today()
        self.data_saida = self.data_entrada + timedelta(days=self.noites)
        self.valor_total = self.noites * self.quarto.tarifa

    @property
    def noites(self):
        return self._noites

    @noites.setter
    def noites(self, valor):
        if valor < 1:
            raise ValueError("O número de noites deve ser no mínimo 1.")
        self._noites = valor

    def __len__(self):
        return self.noites

    def __str__(self):
        return (
            f"Hóspede: {self.hospede}\n"
            f"Quarto: {self.quarto.numero}\n"
            f"Noites: {self.noites}\n"
            f"Entrada: {self.data_entrada}\n"
            f"Saída: {self.data_saida}\n"
            f"Valor total: R$ {self.valor_total}"
        )


# =========================
# Persistência simples
# =========================
def salvar_dados(quartos):
    data = {
        "quartos": [
            {
                "numero": q.numero,
                "capacidade": q.capacidade,
                "tarifa": q.tarifa,
                "disponivel": q.disponivel,
            }
            for q in quartos
        ]
    }
    with open(ARQUIVO, "w") as f:
        json.dump(data, f, indent=2)


def carregar_quartos():
    try:
        with open(ARQUIVO, "r") as f:
            data = json.load(f)
            quartos = []
            for q in data["quartos"]:
                quarto = Quarto(q["numero"], q["capacidade"], q["tarifa"])
                if not q["disponivel"]:
                    quarto.ocupar()
                quartos.append(quarto)
            return quartos
    except FileNotFoundError:
        return []


# =========================
# Função de validação do quarto
# =========================
def buscar_quarto(numero, quartos):
    for quarto in quartos:
        if quarto.numero == numero:
            return quarto
    raise ValueError("Quarto não existe.")


# =========================
# Método main (CLI)
# =========================
def main():
    quartos = carregar_quartos()

    if not quartos:
        quartos = [
            Quarto(101, 1, 120),
            Quarto(102, 2, 180),
            Quarto(201, 3, 250),
        ]

    print("\n=== QUARTOS ===")
    for q in quartos:
        print(q)

    try:
        print("\n=== CHECK-IN ===")
        nome = input("Nome do hóspede: ")
        doc = input("Documento: ")

        # 🔢 valida número do quarto
        try:
            numero_quarto = int(input("Número do quarto: "))
        except ValueError:
            raise ValueError("Número do quarto deve ser numérico.")

        # 🔎 valida se o quarto existe IMEDIATAMENTE
        quarto = buscar_quarto(numero_quarto, quartos)

        if not quarto.disponivel:
            raise ValueError("Quarto não está disponível.")

        # 🌙 valida noites
        try:
            noites = int(input("Quantas noites vai ficar? "))
        except ValueError:
            raise ValueError("Número de noites deve ser numérico.")

        hospede = Hospede(nome, doc)
        reserva = Reserva(hospede, quarto, noites)

        quarto.ocupar()
        salvar_dados(quartos)

        print("\n✅ CHECK-IN REALIZADO COM SUCESSO\n")
        print(reserva)

    except ValueError as erro:
        print(f"\n❌ Erro: {erro}")


if __name__ == "__main__":
    main()
