istema de Reservas de Hotel
Integrantes da equipe:
-----------------------------------------
Jefferson da Rocha Teodoro - Responsabilidade: Criação da API (Flask) e Integração do Sistema

Gival Pordeus da Silva Neto - Responsabilidade: Modelagem de Classes e POO

Genildo da Silva Ferreira - Responsabilidade: Regras de Negócio e Estados da Reserva

Thalyson de Sousa Batista Maia - Responsabilidade: Cálculo de Tarifas e Relatórios

Thalis Leandro Bezerra de Lima - Responsabilidade: Persistência, Configurações e Testes

Principais Classes Projeto:
Classe: Pessoa (será a interface para outros usuários)

Atributos: Nome, CPF, E-mail, Telefone
Métodos: getters e setters (para validação dos dados), atualização_dos_dados (mudar email ou telefone)
Classe: Hospede

Atributos: [Nome, CPF, E-mail, Telefone] e lista_de_reservas_do_hóspede (vai herdar os atributos de pessoa e adicionar mais um)
Métodos: Adicionar_reserva(), listar_reservas()
Classe: Quarto

Atributos: Número (Chave primária), capacidade, tarifa_por_diária, status
Métodos: Verificar_disponibilidade(), alterar_status(), bloquear() e desbloquear()
Classe: Reserva

Atributos: Hóspede, quarto, data_entrada, data_saida, n_de_hóspedes, origem, status, pagamentos, adicionais
Métodos: confirmar(), cancelar(). checkin(), checkout(), marcar_no_show(), calcular_valor_diarias(), calcular_valor_total, total_pago(), validar_capacidade()
Classe: Pagamento

Atributos: data, forma_pagamento (dinheiro, crédito, débito, PIX), valor
Métodos: validar_valor()
Classe: Configuracao

Atributos: horario_checkin, horario_checkout, tolerancia_no_show, politica_cancelamento, multiplicador_fim_semana, temporadas
Métodos: carregar_configuracoes(), obter_multiplicador()
