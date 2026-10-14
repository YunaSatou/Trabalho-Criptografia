import os  # Permite trabalhar com arquivos e caminhos
import platform  # Identifica o sistema operacional utilizado
import subprocess  # Permite executar comandos do sistema
from pathlib import Path  # Facilita o trabalho com caminhos de arquivos


def limpar_tela():  # Cria uma função para limpar o terminal
    # Escolhe o comando adequado para o sistema operacional
    comando = "cls" if platform.system() == "Windows" else "clear"

    # Executa o comando para limpar a tela
    subprocess.run(comando, shell=True)


# Define os caracteres que podem ser utilizados pela cifra
# A base contém letras minúsculas, acentuadas, símbolos e números
base = 'abcdefghijklmnopqrstuvwxyzàáâãéêíóôõúüç.,;:!?(){}"-–—_@#%&*+=/$§1234567890'

# Define a quantidade de posições que cada caractere será deslocado
chave = 3


def obter_texto():  # Permite digitar um texto ou selecionar um arquivo .txt
    msg_erro = ""  # Inicializa a mensagem de erro

    while True:  # Mantém o menu funcionando até receber uma entrada válida
        limpar_tela()  # Limpa o terminal

        print('─' * 40)  # Exibe a linha superior do menu
        print('・┆✦ COMO DESEJA INSERIR O TEXTO? ✦ ┆・'.center(40))
        print('─' * 40)  # Exibe uma linha divisória
        print()  # Pula uma linha
        print('1 - Digitar texto'.center(38))  # Opção para digitar texto
        print('2 - Abrir arquivo .txt'.center(38))  # Opção para selecionar arquivo
        print()  # Pula uma linha
        print('─' * 40)  # Exibe a linha inferior do menu

        if msg_erro:  # Verifica se existe uma mensagem de erro
            print(msg_erro)  # Exibe a mensagem de erro
            msg_erro = ""  # Limpa a mensagem para não repeti-la

        try:  # Inicia o tratamento de entradas inválidas
            escolha = int(input('Opção: '))  # Recebe a opção do usuário

            if escolha == 1:  # Verifica se o usuário escolheu digitar texto
                return input('\nDigite o texto:\n')  # Retorna o texto digitado

            elif escolha == 2:  # Verifica se o usuário escolheu abrir um arquivo

                try:  # Tenta abrir a janela de seleção de arquivos
                    import tkinter as tk  # Importa recursos da interface gráfica
                    from tkinter import filedialog  # Importa as janelas de seleção

                    janela = tk.Tk()  # Cria a janela principal do Tkinter
                    janela.withdraw()  # Esconde a janela principal

                    try:
                        # Mantém a janela de seleção à frente das outras
                        janela.attributes('-topmost', True)

                        # Abre uma janela para escolher o arquivo de entrada
                        caminho = filedialog.askopenfilename(
                            parent=janela,
                            title='Selecione o arquivo de texto',
                            filetypes=[
                                ('Arquivos de texto', '*.txt'),
                                ('Todos os arquivos', '*.*')
                            ]
                        )

                    finally:
                        janela.destroy()  # Fecha a janela do Tkinter

                except Exception:
                    # Usa o terminal se a janela gráfica não estiver disponível
                    print('\nNão foi possível abrir a janela de seleção.')
                    caminho = input(
                        'Digite o caminho do arquivo .txt:\n'
                    ).strip().strip('"')

                # Verifica se o usuário cancelou a seleção
                if not caminho:
                    msg_erro = '\nNenhum arquivo foi selecionado.\n'
                    continue  # Volta ao menu

                # Converte o caminho informado em um objeto Path
                arquivo_txt = Path(caminho).expanduser()

                # Verifica se o arquivo possui a extensão .txt
                if arquivo_txt.suffix.lower() != '.txt':
                    msg_erro = '\nArquivo inválido! Escolha um arquivo .txt.\n'
                    continue  # Volta ao menu

                # Abre o arquivo usando UTF-8 e aceita BOM no início do texto
                with open(arquivo_txt, 'r', encoding='utf-8-sig') as arquivo:
                    return arquivo.read()  # Lê e retorna todo o conteúdo

            else:  # Executa se a opção for diferente de 1 ou 2
                msg_erro = '\nOpção inválida! Escolha apenas 1 ou 2.\n'

        except ValueError:  # Trata entradas que não são números inteiros
            msg_erro = '\nEntrada inválida! Digite apenas números.\n'

        except FileNotFoundError:  # Trata arquivos que não foram encontrados
            msg_erro = '\nArquivo não encontrado. Verifique o arquivo escolhido.\n'

        except UnicodeDecodeError:  # Trata problemas de codificação do arquivo
            msg_erro = '\nNão foi possível ler o arquivo usando UTF-8.\n'

        except OSError as erro:  # Trata outros problemas de acesso ao arquivo
            msg_erro = f'\nNão foi possível abrir o arquivo: {erro}\n'



def salvar_resultado(texto, forma):
    if forma == 1:
        nome = 'mensagem_criptografada.txt'
    else:
        nome = 'mensagem_descriptografada.txt'

    try:
        # No Chromebook, o programa roda no ambiente Linux.
        if platform.system() == "Linux":
            pasta_destino = Path.home() / "criptografia"

            # Cria a pasta caso ela ainda não exista.
            pasta_destino.mkdir(parents=True, exist_ok=True)

        else:
            # No Windows, permite escolher a pasta de destino.
            try:
                import tkinter as tk
                from tkinter import filedialog

                janela = tk.Tk()
                janela.withdraw()

                try:
                    janela.attributes('-topmost', True)
                    pasta_escolhida = filedialog.askdirectory(
                        parent=janela,
                        title='Escolha onde salvar o resultado'
                    )
                finally:
                    janela.destroy()

            except Exception:
                pasta_escolhida = ""

            # Se a janela não abrir, permite informar o caminho.
            if not pasta_escolhida:
                print('\nInforme o caminho da pasta onde deseja salvar.')
                print('Pressione Enter para cancelar o salvamento.')
                pasta_escolhida = input('Pasta: ').strip().strip('"')

                if not pasta_escolhida:
                    print('\nSalvamento cancelado.')
                    return

            pasta_destino = Path(pasta_escolhida).expanduser()

            if not pasta_destino.is_dir():
                print('\nA pasta não existe ou não está acessível.')
                return

        # Evita substituir arquivos que já existem.
        caminho_arquivo = pasta_destino / nome
        contador = 2

        while caminho_arquivo.exists():
            nome_alternativo = (
                f'{Path(nome).stem}_{contador}{Path(nome).suffix}'
            )
            caminho_arquivo = pasta_destino / nome_alternativo
            contador += 1

        # Salva o resultado em formato de texto.
        caminho_arquivo.write_text(texto, encoding='utf-8')

        print(f'\nArquivo salvo em: {caminho_arquivo}')

    except OSError as erro:
        print(f'\nNão foi possível salvar o arquivo: {erro}')

def criptografia():  # Controla a criptografia e a descriptografia
    msg_erro = ""  # Inicializa a mensagem de erro do menu principal

    while True:  # Mantém o menu principal funcionando
        limpar_tela()  # Limpa o terminal

        print('─' * 40)  # Exibe a linha superior
        print('・┆✦ O QUE VOCE DESEJA FAZER? ✦ ┆・'.center(38))
        print('─' * 40)  # Exibe uma linha divisória
        print()  # Pula uma linha
        print('1 - Criptografar'.center(33))  # Opção de criptografia
        print('2 - Descriptografar'.center(35))  # Opção de descriptografia
        print()  # Pula uma linha
        print('─' * 40)  # Exibe a linha inferior

        if msg_erro:  # Verifica se existe uma mensagem de erro
            print(msg_erro)  # Exibe a mensagem
            msg_erro = ""  # Limpa a mensagem

        try:  # Trata entradas inválidas
            forma = int(input('Opção: '))  # Recebe a operação escolhida

            # Aceita somente as opções 1 e 2
            if forma != 1 and forma != 2:
                msg_erro = '\nOpção inválida! Escolha apenas 1 ou 2.\n'
                continue  # Retorna ao menu principal

        except ValueError:  # Trata entradas que não são números inteiros
            msg_erro = '\nEntrada inválida! Digite apenas números.\n'
            continue  # Retorna ao menu principal

        texto = obter_texto()  # Obtém o texto digitado ou lido do arquivo
        resultado = ""  # Inicializa a variável que armazenará o resultado

        # Percorre cada caractere do texto original
        for caractere in texto:
            maiuscula = caractere.isupper()  # Verifica se era maiúsculo
            caractere_base = caractere.lower()  # Converte temporariamente para minúsculo
            posicao = base.find(caractere_base)  # Procura o caractere na base

            # Verifica se o caractere foi encontrado na base
            if posicao != -1:

                if forma == 1:  # Executa se a operação for criptografar
                    # Avança a posição conforme o valor da chave
                    posicao = (posicao + chave) % len(base)

                else:  # Executa se a operação for descriptografar
                    # Retrocede a posição conforme o valor da chave
                    posicao = (posicao - chave) % len(base)

                # Obtém o caractere correspondente à nova posição
                novo_caractere = base[posicao]

                # Mantém a letra maiúscula quando o original era maiúsculo
                if maiuscula and novo_caractere.isalpha():
                    novo_caractere = novo_caractere.upper()

                # Adiciona o caractere transformado ao resultado
                resultado += novo_caractere

            else:
                # Preserva espaços, quebras de linha e outros caracteres
                resultado += caractere

        limpar_tela()  # Limpa a tela antes de exibir o resultado

        # Mostra o texto final no terminal
        print('╰┈➤ O texto final fica:', resultado)

        # Abre a seleção de pasta e salva o resultado
        salvar_resultado(resultado, forma)

        msg_erro_minimenu = ""  # Inicializa o erro do menu final

        while True:  # Repete o menu até receber uma opção válida
            print()  # Pula uma linha
            print('─' * 40)  # Exibe a linha superior
            print('・┆✦ O que deseja fazer agora? ✦ ┆・'.center(38))
            print('─' * 40)  # Exibe uma linha divisória
            print()  # Pula uma linha
            print('1 - Voltar ao menu principal'.center(38))
            print('2 - Voltar ao inicio'.center(38))
            print()  # Pula uma linha
            print('─' * 40)  # Exibe a linha inferior

            if msg_erro_minimenu:  # Verifica se existe uma mensagem de erro
                print(msg_erro_minimenu)  # Exibe a mensagem
                msg_erro_minimenu = ""  # Limpa a mensagem

            try:  # Trata entradas inválidas
                minimenu = int(input('Opção: '))  # Recebe a opção escolhida

                # Verifica se a opção é válida
                if minimenu == 1 or minimenu == 2:
                    break  # Sai do menu final

                else:
                    msg_erro_minimenu = (
                        '\nOpção inválida! Escolha apenas 1 ou 2.\n'
                    )

            except ValueError:  # Trata entradas que não são números inteiros
                msg_erro_minimenu = (
                    '\nEntrada inválida! Digite apenas números.\n'
                )

        if minimenu == 1:  # Verifica se o usuário escolheu voltar ao menu
            return  # Encerra a função criptografia

        elif minimenu == 2:  # Verifica se deseja realizar outra operação
            msg_erro = ""  # Limpa mensagens de erro anteriores
            # O laço principal apresenta novamente o menu de operações
