from src.modelos import reserva
from src.modelos.quarto import QuartoSimples, QuartoLuxo
from src.modelos.hospede import Hospede
from src.modelos.pagamento import Dinheiro, Pix
from src.modelos.reserva import Reserva
from src.modelos.configuracao import Configuracao

#testes simples para verificar o funcionamento das classes e métodos principais



def teste_quarto_simples():
    quarto = QuartoSimples(101, 2, 150)

    assert quarto.valor_total_diaria() == 150
    assert quarto.disponivel is True
    assert quarto.descricao() == "Quarto Simples"


def teste_quarto_luxo():
    quarto = QuartoLuxo(201, 4, 300, 100)

    assert quarto.valor_total_diaria() == 400
    assert quarto.descricao() == "Quarto Luxuoso"


def teste_reserva_calculo_total():
    hospede = Hospede("Jefferson", "12345678901")
    quarto = QuartoSimples(101, 2, 150)
    pagamento = Pix()
    config = Configuracao()

    reserva = Reserva(hospede, quarto, 3, pagamento, config)

    assert reserva.calcular_total() == 450


#Esse aqui é um teste para garantir que o quarto só é ocupado após a finalização/Pagamento da reserva
def teste_quarto_so_ocupa_apos_finalizar():
    hospede = Hospede("Jefferson", "12345678901")
    quarto = QuartoSimples(102, 2, 150)
    pagamento = Dinheiro()
    config = Configuracao()
    reserva = Reserva(hospede, quarto, 2, pagamento, config)

    # Antes de finalizar
    assert quarto.disponivel is True

    reserva.confirmar()
    reserva.finalizar()

    # Depois de finalizar
    assert quarto.disponivel is False


print("✅ Todos os testes passaram com sucesso!")
