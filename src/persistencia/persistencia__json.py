import json
import os

#Criando pasta dados caso não exista e definindo o caminho do arquivo reservas.json

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
CAMINHO_DADOS = os.path.join(BASE_DIR, "dados")

os.makedirs(CAMINHO_DADOS, exist_ok=True)

ARQUIVO_RESERVAS = os.path.join(CAMINHO_DADOS, "reservas.json")


def salvar_reservas(reservas):
    dados = []

    for r in reservas:
        dados.append({
            "hospede": r.hospede.nome,
            "cpf": r.hospede.cpf,
            "quarto": r.quarto.numero,
            "dias": r.dias,
            "estado": r.estado
        })

    with open(ARQUIVO_RESERVAS, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)
