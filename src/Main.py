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


#Validações de entradas
def validar_nome(nome):
    nome_validacao = nome.replace(" ", "") 
    if len(nome_validacao) >= 3 and nome_validacao.isalpha():
        return True
    else: 
        return False

def validar_cpf(cpf):
    cpf_limpo = cpf.replace(".", " ").replace("-", " ").replace(" ", "") 

    if cpf_limpo.isdigit() and len(cpf_limpo) == 11:
        return True
    else:
        return False
    
def validar_dias(dias):
    dias_limpo = dias.replace(" ", "")

    if dias_limpo.isdigit():
        if int(dias_limpo) > 0:
            return True
    return False


print("------------- Sistema de Reservas de Hotel ------------- ")

#nesses blocos irei pedir os dados e validar como também fazer a reserva do cliente
while True:
    nome = input("Nome do hóspede: ")
    if validar_nome(nome):
        break
    print ("Nome inválido, tente novamente")

while True:
    cpf = input("Informe seu CPF ")
    if validar_cpf(cpf):
        break
    print("CPF inválido, tente novamente")

hospede = Hospede(nome, cpf)
while True:
    dias = (input("Quantos dias ficará hospedado? "))
    if validar_dias(dias):
        dias = int(dias)
        break
    print("Informe um valor válido!")
    
while True:
    indice_input = input("Escolha o índice do quarto: ")
    if indice_input.isdigit() and int(indice_input) < len(quartos):
        indice = int(indice_input)
        quarto = quartos[indice]
        if quarto.disponivel:
            break
        else:
            print("Este quarto não está disponível.")
    else:
        print(f"Escolha um número válido entre 0 e {len(quartos)-1}.")

# 5. Pagamento e Finalização
print("\nForma de pagamento: 1 - Dinheiro | 2 - Pix")
op = input("Escolha: ")
pagamento = Dinheiro() if op == "1" else Pix()

reserva = Reserva(hospede, quarto, dias, pagamento)
gestao.adicionar(reserva)

print(f"\nReserva criada com sucesso! Total: R$ {reserva.calcular_total():.2f}")

finalizar = input("Deseja finalizar a reserva agora? (s/n): ")
if finalizar.lower() == "s":
    reserva.finalizar()
    print("Reserva finalizada e quarto liberado.")