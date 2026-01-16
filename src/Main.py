from modelos.hospede import Hospede
from modelos.quarto import QuartoSimples, QuartoLuxo
from modelos.pagamento import Dinheiro, Pix
from modelos.reserva import Reserva
from serviços.gestao_reservas import GestaoReservas

# Quartos disponíveis
quartos = [
    QuartoSimples(101, 2, 150),
    QuartoSimples(102, 2, 150),
    QuartoLuxo(201, 4, 300, 100)
]

def validacao_nome(nome):
    if not nome.strip():
        return "Você informou espaços vázios, tente novamente."
    elif nome.isdigit():
        return "VocÊ informou apenas números, tente novamente."
    elif nome.isalnum():
        return "Você informou letras e números, tente novmente. "
    return None

gestao = GestaoReservas()
controle = True


#Validações de entradas
def validar_nome(nome):
    nome_validacao = nome.replace(" ", "") #remover espaços em brancos para validações

    if not nome_validacao:
        return "Nome não pode ser vazio, tente novamente!"
    elif not len(nome_validacao) < 3:
        return "Nome precisa ter ao menos 3 letras"



print("=== Sistema de Reservas de Hotel ===")
while controle:
    nome = input("Nome do hóspede: ")
    cpf = input("CPF: ")
    hospede = Hospede(nome, cpf)

    dias = int(input("Quantos dias ficará hospedado? "))

    print("\nModelos de quarto disponíveis:")
    for i, q in enumerate(quartos):
        if q.disponivel:
            print(f"{i} - {q.descricao()} (Quarto {q.numero})")

    indice = int(input("Escolha o quarto: "))
    quarto = quartos[indice]

    print("\nForma de pagamento:")
    print("1 - Dinheiro")
    print("2 - Pix")
    op = input("Escolha: ")

    pagamento = Dinheiro() if op == "1" else Pix()

    reserva = Reserva(hospede, quarto, dias, pagamento)
    gestao.adicionar(reserva)

    print("\nReserva criada com sucesso!")
    print(f"Total a pagar: R$ {reserva.calcular_total():.2f}")

    finalizar = input("Deseja finalizar a reserva agora? (s/n): ")
    if finalizar.lower() == "s":
        reserva.finalizar()
        print("Reserva finalizada e quarto liberado.")
