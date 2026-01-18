import json
import os
class Configuracao:
    def __init__(self):
    
        # O python não estava encontranado o arquivo settings.json com um caminho relativo, então utilizei um caminho absoluto.
        # Caminho absoluto até a pasta src
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        # Caminho absoluto até o settings.json
        caminho = os.path.join(base_dir, "config", "settings.json")

        with open(caminho, "r", encoding="utf-8") as f:
            self._dados = json.load(f)
    @property
    def multa_cancelamento(self):
        return self._dados["multa_cancelamento"]

    @property
    def taxa_no_show(self):
        return self._dados["taxa_no_show"]

    @property
    def multiplicador_fim_semana(self):
        return self._dados["multiplicador_fim_semana"]

    @property
    def estados_validos(self):
        return self._dados["estados_reserva"]
