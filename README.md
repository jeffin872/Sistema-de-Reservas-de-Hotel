🏨 Sistema de Reservas de Hotel

▶️ Como Executar o Sistema

1️⃣ Clonar o repositório
git clone <url-do-repositorio>
cd Sistema_Reservas_Hotel

2️⃣Criar e ativar o ambiente virtual (venv)
python -m venv venv

3️⃣ Instalar as dependências
pip install -r requirements.txt

4️⃣ Executar o sistema 
python Main.py (execute dentro da pasta src)

 
 Conceitos Aplicados

Modelagem por classes bem definidas

Uso de herança (Pessoa → Hospede, Quarto → QuartoSimples / QuartoLuxo)

Encapsulamento com atributos protegidos e uso de @property

Polimorfismo para cálculo de diárias

Controle de estados da reserva (criada, confirmada, cancelada, finalizada)

Validações centralizadas nos métodos

Uso de exceções customizadas para regras de negócio

Separação por módulos (modelos, serviços, persistencia, testes)

Testes automatizados utilizando assert

💾 Persistência de Dados

Implementada persistência em JSON

As reservas são salvas automaticamente ao final do fluxo

Os dados incluem hóspede, quarto, quantidade de dias e estado da reserva

Persistência desacoplada da lógica principal, respeitando o encapsulamento

📌 Diagrama Simplificado

Pessoa
 └── Hospede
        └── lista_reservas

Quarto
 ├── QuartoSimples
 └── QuartoLuxo

Reserva
 ├── Hospede
 ├── Quarto
 └── Pagamento

Pagamento
 ├── Dinheiro
 └── Pix


📌 Principais Classes
*Pessoa*

Armazena dados básicos do usuário

Realiza validações e atualização de informações

Hospede

Representa o hóspede do hotel

Gerencia as reservas associadas

*Quarto*

Controla dados e disponibilidade

Define o valor da diária e tipo do quarto

*Reserva*

Gerencia o ciclo de vida da reserva

Controla estados, pagamentos e valores

*Pagamento*

Representa a forma de pagamento

Valida os valores pagos

Configuracao

Centraliza regras gerais do sistema

Define políticas e multiplicadores
