import os  # Importa o módulo para interagir com o sistema operacional
import platform  # Importa o módulo para identificar o sistema operacional atual
import subprocess  # Importa o módulo para executar comandos do sistema com segurança

def limpar_tela():
    comando = "cls" if platform.system() == "Windows" else "clear"  # Define o comando de limpeza de tela baseado no sistema (Windows ou outros)
    subprocess.run(comando, shell=True)  # Executa o comando diretamente no terminal do sistema operacional

def saudacao():
    limpar_tela()  # Limpa o terminal antes de mostrar a mensagem inicial
    print('Bem-vindo(a) ao programa de criptografia.ᐟ.ᐟ\n')  # Exibe a mensagem de boas-vindas na tela
    print('O programa permite que você criptografe e descriptografe textos usando a cifra de César.\n')  # Explica o funcionamento básico
    input('Pressione Enter para continuar ↩ ')  # Pausa o programa e aguarda a tecla Enter do usuário

def menu():
    msg_erro = ""  # Cria uma variável vazia para armazenar as mensagens de erro temporariamente

    while True:
        limpar_tela()  # Limpa o terminal no início de cada repetição do menu
        print("─" * 30)  # Exibe uma linha divisória com 30 traços horizontais
        print('「 ✦ MENU ✦ 」'.center(25))  # Centraliza o título do menu em um espaço de 25 caracteres
        print("─" * 30)  # Exibe a linha divisória inferior do título
        print()  # Imprime uma linha em branco para dar espaçamento
        print('1 - Criptografar'.center(25))  # Centraliza a primeira opção do menu
        print('0 - Sair'.center(25))  # Centraliza a opção de fechar o programa
        print()  # Imprime outra linha em branco de espaçamento
        print("─" * 30)  # Desenha a linha horizontal que fecha o design do menu

        if msg_erro:
            print(msg_erro)  # Mostra a mensagem de erro salva caso a variável não esteja vazia
            msg_erro = ""  # Limpa o texto da variável para que o erro não se repita na próxima volta

        try:
            escolha = int(input('Opção: '))  # Recebe o valor digitado pelo usuário e tenta convertê-lo em número inteiro

            if escolha == 1:
                from Cifra import criptografia  # Importa a função de criptografia do arquivo externo Cifra.py apenas se o usuário escolher 1
                criptografia()  # Executa a função que foi importada
            elif escolha == 0:
                print('\nEncerrando o programa...')  # Avisa ao usuário que o script está sendo fechado
                break  # Interrompe o loop "while True" para encerrar a execução do menu
                
            else:
                msg_erro = '\nOpção inválida! Escolha apenas 1 ou 0.\n'  # Define a mensagem de erro caso o número digitado não seja 0 ou 1
        except ValueError:
            msg_erro = '\nEntrada inválida! Digite apenas números.\n'  # Define a mensagem de erro caso o usuário digite letras ou símbolos

if __name__ == "__main__":
    saudacao()  # Inicia o fluxo executando a função de boas-vindas
    menu()  # Abre o menu interativo logo após a saudação
