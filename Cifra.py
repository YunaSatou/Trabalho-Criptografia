import os  # Importa o módulo para interagir com o sistema operacional
import platform  # Importa o módulo para identificar o sistema operacional atual (Windows, Linux ou Mac)
import subprocess  # Importa o módulo para executar comandos do sistema com segurança
from main import menu  # Importa a função menu do arquivo main.py para permitir o retorno ao menu principal

def limpar_tela():
    comando = "cls" if platform.system() == "Windows" else "clear"  # Define o comando de limpeza de tela com base no sistema operacional detectado
    subprocess.run(comando, shell=True)  # Envia o comando diretamente para a execução no terminal do sistema

base = 'abcdefghijklmnopqrstuvwxyzàáâãéêíóôõúüçABCDEFGHIJKLMNOPQRSTUVWXYZÀÁÂÃÉÊÍÓÔÕÚÜÇ.,;:!?(){}""-–—_@#%&*+=/$§1234567890'  # Define a lista de todos os caracteres válidos e possíveis para o processo
chave = 3  # Define o número de posições que serão puladas ou voltadas na cifra de César

def criptografia():
    msg_erro = ""  # Inicializa uma variável vazia para armazenar as mensagens de erro da escolha inicial
    
    while True:  # Cria o loop principal que mantém a tela de criptografia ativa até ser finalizada
        limpar_tela()  # Limpa o terminal a cada repetição do ciclo principal
        print('─' * 40)  # Desenha uma linha horizontal divisória com 40 caracteres
        print('・┆✦ O QUE VOCE DESEJA FAZER? ✦ ┆・'.center(38))  # Alinha o título dentro de uma área predefinida
        print('─' * 40)  # Desenha a linha horizontal de fechamento do cabeçalho
        print()  # Cria um espaçamento vertical em branco
        print('1 - Criptografar'.center(33))  # Exibe centralizada a opção número 1
        print('2 - Descriptografar'.center(35))  # Exibe centralizada a opção número 2
        print()  # Cria outro espaçamento vertical em branco
        print('─' * 40)  # Desenha a linha inferior de fechamento do menu de opções
        
        if msg_erro:
            print(msg_erro)  # Exibe o aviso de erro armazenado caso o usuário tenha digitado algo inválido antes
            msg_erro = ""  # Reseta o texto do erro para que ele suma na próxima atualização de tela

        try:
            forma = int(input('Opção: '))  # Lê a entrada do usuário e faz a conversão direta para um número inteiro
            if forma != 1 and forma != 2:
                msg_erro = '\nOpção inválida! Escolha apenas 1 ou 2.\n'  # Define a mensagem de erro se o número não for 1 ou 2
                continue  # Força o loop a recomeçar do topo, exibindo a mensagem de erro que acabou de ser criada
        except ValueError:
            msg_erro = '\nEntrada inválida! Digite apenas números.\n'  # Define a mensagem de erro se o usuário digitar letras ou símbolos
            continue  # Força o loop a recomeçar do topo para limpar a tela e mostrar o erro estruturado

        cripto = ''  # Cria ou limpa a variável que vai acumular a frase final gerada

        if forma == 1:
            texto = input('\nDigite o texto que deseja criptografar:\n')  # Solicita a string que passará pela cifra
            texto = texto.lower()  # Converte toda a entrada recebida para letras minúsculas para padronização

            for palavra in texto: 
                posicao = base.find(palavra)  # Procura o índice numérico do caractere atual dentro da variável base

                if posicao != -1:
                    posicao = (posicao + chave) % len(base)  # Avança o caractere de acordo com a chave e aplica o resto da divisão para não estourar o limite
                    cripto = cripto + base[posicao]  # Substitui pelo caractere criptografado e adiciona à string final
                else:
                    cripto = cripto + palavra  # Mantém o caractere original sem alterações se ele não fizer parte da base

        elif forma == 2:
            texto = input('\nDigite o texto que deseja descriptografar:\n')  # Solicita a string codificada que será decifrada
            texto = texto.lower()  # Transforma todo o texto em caracteres minúsculos

            for palavra in texto:
                posicao = base.find(palavra)  # Encontra em qual posição o caractere se localiza dentro da base estável
                
                if posicao != -1:
                    posicao = (posicao - chave) % len(base)  # Recua as posições usando a subtração da chave e ajusta o limite com a rotação matemática
                    cripto = cripto + base[posicao]  # Adiciona o caractere original recuperado ao acumulador de texto
                else:
                    cripto = cripto + palavra  # Conserva símbolos ou caracteres que não foram mapeados na lista base original

        msg_erro_minimenu = ""  # Cria uma variável vazia destinada exclusivamente aos erros do menu final de navegação

        while True:  # Abre o sub-loop encarregado de controlar as ações pós-criptografia sem perder o resultado da tela
            limpar_tela()  # Limpa o terminal a cada atualização das opções de destino do usuário
            print('╰┈➤ O texto final fica:', cripto)  # Exibe o resultado do processamento fixado na parte superior da tela

            print()  # Insere uma linha em branco para organização visual
            print('─' * 40)  # Desenha a linha divisória superior do novo submenu
            print('・┆✦ O que deseja fazer agora? ✦ ┆・'.center(38))  # Exibe a pergunta de destino de forma centralizada
            print('─' * 40)  # Desenha a linha divisória inferior da pergunta do cabeçalho
            print()  # Insere uma linha em branco
            print('1 - Voltar ao menu principal'.center(38))  # Apresenta a opção de retorno ao programa base
            print('2 - Voltar ao inicio'.center(38))  # Apresenta a opção de reiniciar este mesmo fluxo
            print()  # Outra quebra de linha em branco
            print('─' * 40)  # Conclui o design com o traço de fechamento da caixa de opções

            if msg_erro_minimenu:
                print(msg_erro_minimenu)  # Exibe a mensagem de erro específica deste menu se o usuário errar a escolha
                msg_erro_minimenu = ""  # Zera a variável de erro para evitar repetição contínua no terminal

            try:
                minimenu = int(input('Opção: '))  # Aguarda a resposta numérica do usuário para decidir o destino do fluxo
                if minimenu == 1 or minimenu == 2:
                    break  # Encerra este sub-loop específico se a opção informada for aceita
                else:
                    msg_erro_minimenu = '\nOpção inválida! Escolha apenas 1 ou 2.\n'  # Grava o erro caso o valor numérico seja incorreto
            except ValueError:
                msg_erro_minimenu = '\nEntrada inválida! Digite apenas números.\n'  # Grava o erro se a digitação contiver letras ou caracteres inválidos

        if minimenu == 1:
            return  # Direciona o fluxo de volta chamando o menu principal importado do main.py
            
        elif minimenu == 2:
            print('\nReiniciando...')  # Exibe um feedback rápido na tela antes de reiniciar o loop principal do arquivo

