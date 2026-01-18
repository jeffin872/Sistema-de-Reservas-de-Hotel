from modelos.hospede import Hospede
from modelos.quarto import QuartoSimples, QuartoLuxo
from modelos.pagamento import Dinheiro, Pix
from modelos.reserva import Reserva
from serviços.gestao_reservas import GestaoReservas
from modelos.configuracao import Configuracao
from modelos.configuracao import Configuracao
# Quartos disponíveis
quartos = [
    QuartoSimples(101, 2, 150),
    QuartoSimples(102, 2, 150),
    QuartoLuxo(201, 4, 300, 100)
]

gestao = GestaoReservas()
config = Configuracao()


#  VALIDAÇÕES 
def validar_nome(nome):
    nome_validacao = nome.replace(" ", "")
    return len(nome_validacao) >= 3 and nome_validacao.isalpha()


def validar_cpf(cpf):
    cpf_limpo = cpf.replace(".", "").replace("-", "").replace(" ", "")
    return cpf_limpo.isdigit() and len(cpf_limpo) == 11


def validar_dias(dias):
    return dias.strip().isdigit() and int(dias) > 0


print("------------- Sistema de Reservas de Hotel ------------- ")

controle = True

while controle:
    #  HÓSPEDE 
    while True:
        nome = input("Nome do hóspede: ")
        if validar_nome(nome):
            break
        print("Nome inválido, tente novamente.")

    while True:
        cpf = input("Informe seu CPF: ")
        if validar_cpf(cpf):
            break
        print("CPF inválido, tente novamente.")

    hospede = Hospede(nome, cpf)

    #  DIAS 
    while True:
        dias_input = input("Quantos dias ficará hospedado? ")
        if validar_dias(dias_input):
            dias = int(dias_input)
            break
        print("Informe um valor válido.")

    #  QUARTOS 
    print("\nModelos de quarto disponíveis:")
    quartos_disponiveis = [q for q in quartos if q.disponivel]

    for i, q in enumerate(quartos_disponiveis):
        print(f"{i} - {q.descricao()} (Quarto {q.numero})")

    while True:
        indice_input = input("Escolha o número do quarto: ")
        if indice_input.isdigit():
            indice = int(indice_input)
            if 0 <= indice < len(quartos_disponiveis):
                quarto = quartos_disponiveis[indice]
                break
        print("Opção inválida, tente novamente.")

    #  PAGAMENTO 
    print("\nForma de pagamento:")
    print("1 - Dinheiro")
    print("2 - Pix")

    while True:
        op = input("Escolha (1 ou 2): ")
        if op == "1":
            pagamento = Dinheiro()
            break
        elif op == "2":
            pagamento = Pix()
            break
        print("Opção inválida.")

    reserva = Reserva(hospede, quarto, dias, pagamento, config)

    #  RESUMO 
    print("\n" + "=" * 40)
    print("RESERVA CRIADA COM SUCESSO!")
    print(f"Hóspede: {hospede.nome}")
    print(f"Quarto: {quarto.numero}")
    print(f"Total a pagar: R$ {reserva.calcular_total():.2f}")
    print("=" * 40)

    #  FINALIZAÇÃO 
    pagar = input("\nDeseja pagar agora? (s/n): ")

    if pagar.lower() == "s":
        reserva.confirmar()
        reserva.finalizar()
        print("Pagamento realizado. Reserva finalizada.")
        gestao.adicionar(reserva)
        gestao.salvar()
        controle = False
    else:
        reserva.cancelar()
        print("Reserva cancelada. Quarto liberado.")