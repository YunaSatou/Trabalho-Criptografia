# 🔐 Cifra de César

Programa de criptografia desenvolvido em Python para permitir a criptografia e a descriptografia de textos por meio da Cifra de César, um método clássico de substituição de caracteres.

O projeto foi desenvolvido com o objetivo de explorar conceitos fundamentais da criptografia, aplicando lógica de programação, estruturas de repetição, funções e manipulação de strings para transformar textos de maneira simples e interativa.

## 📌 Objetivo

O objetivo do projeto é demonstrar o funcionamento da Cifra de César por meio de um programa que permite ao usuário criptografar e descriptografar mensagens utilizando uma chave de deslocamento fixa.

O sistema possibilita:

* Criptografar textos inseridos pelo usuário.
* Descriptografar textos previamente criptografados.
* Visualizar o resultado do processamento diretamente no terminal.
* Navegar por menus interativos para escolher as operações desejadas.

## 🛠️ Tecnologias Utilizadas

* **Python** — linguagem utilizada no desenvolvimento do programa.
* **Módulos `os`, `platform` e `subprocess`** — utilizados para auxiliar na interação com o sistema operacional e na limpeza do terminal.
* **Manipulação de strings** — utilizada para percorrer e transformar os caracteres dos textos.
* **Estruturas condicionais e de repetição** — utilizadas para controlar os menus e as operações de criptografia.
* **Funções** — utilizadas para organizar o código e separar as responsabilidades do programa.
* **Importação de módulos** — utilizada para dividir a implementação entre os arquivos `main.py` e `Cifra.py`.

## ✨ Funcionalidades

### ✅ Tela Inicial

* Mensagem de boas-vindas ao usuário.
* Apresentação do objetivo do programa.
* Menu principal com opções para iniciar a criptografia ou encerrar a execução.
* Limpeza do terminal para melhorar a organização visual.

### ✅ Sistema de Criptografia

* Recebimento de textos digitados pelo usuário.
* Conversão do texto para letras minúsculas.
* Deslocamento dos caracteres utilizando uma chave fixa de três posições.
* Preservação de caracteres que não são encontrados na sequência definida pelo programa.

### ✅ Sistema de Descriptografia

* Recebimento de textos criptografados.
* Deslocamento dos caracteres no sentido inverso, utilizando a mesma chave.
* Recuperação do texto original, considerando as regras de transformação implementadas.

### ✅ Sistema de Navegação

Após o processamento do texto, o usuário pode:

* Visualizar o resultado da operação.
* Retornar ao menu principal.
* Reiniciar o processo de criptografia ou descriptografia.

### ✅ Tratamento de Entradas

* Verificação das opções selecionadas nos menus.
* Exibição de mensagens de erro quando o usuário informa opções inválidas.
* Tratamento de entradas que não podem ser convertidas para números inteiros.

## 📂 Estrutura do Projeto

CifraDeCesar/

├── main.py — inicialização, saudação e menu principal.

├── Cifra.py — implementação das operações de criptografia e descriptografia.

└── README.md — documentação do projeto.

## 🔄 Organização do Código

O programa foi dividido em dois arquivos principais para organizar melhor sua estrutura e separar as responsabilidades.

O arquivo `main.py` é responsável pela apresentação inicial, pela exibição do menu principal e pelo direcionamento do usuário para a funcionalidade de criptografia.

Já o arquivo `Cifra.py` concentra a lógica de transformação dos textos, incluindo a definição da sequência de caracteres utilizada, a chave de deslocamento e os processos de criptografia e descriptografia.

Essa separação facilita a compreensão do código e permite organizar as funcionalidades de maneira mais clara.

## 🔄 Funcionamento da Cifra

A Cifra de César funciona por meio do deslocamento dos caracteres de um texto dentro de uma sequência predefinida. Neste projeto, a chave utilizada é o número três, fazendo com que cada caractere reconhecido avance três posições durante a criptografia.

Na descriptografia, o processo é invertido, recuando três posições para recuperar os caracteres correspondentes ao texto original.

O programa utiliza o cálculo do resto da divisão para manter o deslocamento dentro dos limites da sequência definida, permitindo que o processo continue mesmo quando um caractere está próximo do final dela.

## 🔮 Melhorias Futuras

Futuramente, o projeto poderá receber melhorias para ampliar suas funcionalidades e tornar seu funcionamento mais flexível, como:

* Permitir que o usuário escolha a chave de deslocamento.
* Preservar as diferenças entre letras maiúsculas e minúsculas.
* Melhorar o tratamento de caracteres especiais e acentuados.
* Adicionar testes automatizados para verificar os resultados da criptografia e da descriptografia.
* Aprimorar a validação das entradas fornecidas pelo usuário.
* Desenvolver uma interface gráfica para tornar a utilização mais intuitiva.

Essas melhorias poderão ampliar a usabilidade do programa e contribuir para o aprofundamento dos conhecimentos sobre criptografia e desenvolvimento de software.

## 🎯 Considerações Finais

O projeto proporciona uma aplicação prática dos conceitos de programação em Python, demonstrando como estruturas condicionais, laços de repetição, funções e manipulação de strings podem ser utilizados na implementação de um método criptográfico.

Além disso, permite compreender os princípios básicos da transformação de mensagens e a relação entre criptografia e proteção de informações, utilizando um método histórico como ponto de partida para o estudo da segurança da informação.
