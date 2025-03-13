# Sistema Bancário Simples

Este é um projeto de um sistema bancário simples desenvolvido em Python. Ele permite que os usuários realizem operações básicas, como depósitos, saques e consultas de extrato, seguindo algumas regras de negócio.

## Funcionalidades

O sistema oferece as seguintes funcionalidades:

1. **Depósito**:
   - Permite ao usuário depositar valores positivos em sua conta.
   - Todos os depósitos são armazenados no extrato.

2. **Saque**:
   - Permite ao usuário sacar valores da conta, desde que respeite o limite diário de R$ 500,00 e o número máximo de 3 saques por dia.
   - Todos os saques são armazenados no extrato.

3. **Extrato**:
   - Exibe todas as movimentações (depósitos e saques) realizadas na conta.
   - Mostra o saldo atual da conta.

4. **Sair**:
   - Encerra a execução do sistema.

## Regras de Negócio

- **Depósito**:
  - Apenas valores positivos podem ser depositados.
  - O valor do depósito é adicionado ao saldo da conta.

- **Saque**:
  - O valor do saque não pode exceder o saldo disponível.
  - O valor do saque não pode exceder o limite de R$ 500,00 por operação.
  - O número máximo de saques diários é 3.

- **Extrato**:
  - Todas as operações de depósito e saque são registradas.
  - O extrato exibe o histórico de movimentações e o saldo atual.

## Como Executar o Projeto

### Pré-requisitos

- Python 3.x instalado.

### Passos para Execução

1. Clone o repositório:
   ```bash
   git clone https://github.com/Marcuslaf/sistema_bancario.dio


# Simple Banking System

This is a simple banking system project developed in Python. It allows users to perform basic operations such as deposits, withdrawals, and checking their account statement, following some business rules.

## Features

The system offers the following features:

1. **Deposit**:
   - Allows users to deposit positive amounts into their account.
   - All deposits are recorded in the statement.

2. **Withdraw**:
   - Allows users to withdraw funds from their account, as long as they respect the daily limit of R$ 500.00 and a maximum of 3 withdrawals per day.
   - All withdrawals are recorded in the statement.

3. **Statement**:
   - Displays all transactions (deposits and withdrawals) made in the account.
   - Shows the current account balance.

4. **Exit**:
   - Terminates the system.

## Business Rules

- **Deposit**:
  - Only positive amounts can be deposited.
  - The deposited amount is added to the account balance.

- **Withdraw**:
  - The withdrawal amount cannot exceed the available balance.
  - The withdrawal amount cannot exceed the limit of R$ 500.00 per transaction.
  - The maximum number of daily withdrawals is 3.

- **Statement**:
  - All deposit and withdrawal operations are recorded.
  - The statement displays the transaction history and the current balance.

## How to Run the Project

### Prerequisites

- Python 3.x installed.

### Steps to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/Marcuslaf/sistema_bancario.dio
