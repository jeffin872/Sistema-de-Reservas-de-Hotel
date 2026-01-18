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
    dias = input("Quantos dias ficará hospedado? ")

    if validar_dias(dias):
        dias = int(dias.replace(" ", ""))
        break
    else:
        print("Informe um valor válido!")

print("\nModelos de quarto disponíveis:")
for i, q in enumerate(quartos):
    status = "Disponível" if q.disponivel else "Ocupado"
    if q.disponivel:
        print(f"{i} - {q.descricao()} (Quarto {q.numero}) - {status}")

while True:
    indice_input = input("Escolha o número do quarto: ")
    if indice_input.isdigit():
        indice = int(indice_input)
        if 0 <= indice < len(quartos):
            quarto = quartos[indice]
            if quarto.disponivel:
                break
            else:
                print("Este quarto já está ocupado. Escolha outro.")
        else:
            print(f"Opção inválida. Escolha um número entre 0 e {len(quartos)-1}.")
    else:
        print("Erro: Digite apenas o número da opção.")

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
    print("Opção de pagamento inválida.")

reserva = Reserva(hospede, quarto, dias, pagamento)
gestao.adicionar(reserva)

print("\n" + "="*40)
print("RESERVA CRIADA COM SUCESSO!")
print(f"Hóspede: {hospede.nome}")
print(f"Quarto: {quarto.numero}")
print(f"Total a pagar: R$ {reserva.calcular_total():.2f}")
print("="*40)

finalizar = input("\nDeseja finalizar (pagar e libertar) a reserva agora? (s/n): ")
if finalizar.lower() == "s":
    reserva.finalizar()
    print("Reserva finalizada. O quarto está agora disponível.")