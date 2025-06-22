# 🏨 Sistema Simples de Reservas para Pousada

Este projeto foi desenvolvido em **Python** com a proposta de simular o controle de reservas de uma pequena pousada.  
O desafio foi sugerido pelo ChatGPT e a implementação foi realizada por mim, **Jean Paul Cézanne**, como parte do meu aprendizado em lógica de programação.

---

## 🎯 Finalidade

Criar uma aplicação de terminal que possibilite à recepção de um hotel gerenciar reservas de forma prática, oferecendo funcionalidades como:

- Registrar novas reservas
- Editar dados de hóspedes
- Cancelar hospedagens
- Listar hóspedes ativos
- Calcular o faturamento com base nas diárias
- Encerrar o sistema

---

## 🔧 Funcionalidades Principais

- 🆕 **Cadastrar Reserva:** insere um novo hóspede com nome, número do quarto (1–20) e quantidade de diárias.
- 🛠 **Editar Reserva:** permite alterar o número do quarto e as diárias de um hóspede existente.
- 🗑 **Remover Reserva:** exclui uma reserva do sistema.
- 📄 **Visualizar Reservas:** mostra todas as reservas com nome, quarto e número de diárias.
- 💵 **Calcular Total:** soma o valor das reservas com base no preço fixo da diária (R$150).
- 🚪 **Encerrar Programa:** finaliza a execução do sistema.

---

## 🧰 Tecnologias e Lógica Utilizada

- Linguagem: **Python 3**
- Estrutura principal: **dicionários**
- Fluxo de execução: **laço while com menu interativo**
- Limpeza da tela com `os.system('cls')` (no Windows)
- Utilização de métodos nativos como `sum()` e `any()`
- Condições, validações e boas práticas de codificação

---

## 📚 Conhecimento Adquirido

Esse desafio serviu como excelente prática para consolidar conceitos fundamentais de lógica de programação, como estruturas de decisão, repetição e manipulação de coleções.  
Foi uma experiência enriquecedora e motivadora no caminho para me tornar desenvolvedor.

---

## 💻 Demonstração no Terminal

```text
======Escolha uma das opções abaixo======

1 - Adicionar uma nova reserva!
2 - Atualizar um cadastro
3 - Cancelar uma reserva
4 - Exibir reservas ativas
5 - Total de reservas (R$)
6 - Sair do programa

escolha uma das opções acima: 5
O valor total que tem a receber é R$ 1950.00!
```

---

## 👤 Desenvolvedor

**Jean Paul Cézanne Silva Borja**  
Estudante de Sistemas de Informação, em transição para a área de tecnologia  
GitHub: [Cezanne369](https://github.com/Cezanne369)