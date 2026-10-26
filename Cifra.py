# Importa um módulo necessário para a funcionalidade indicada.
import platform  # Identifica o sistema operacional utilizado
# Importa um módulo necessário para a funcionalidade indicada.
import subprocess  # Permite executar comandos do sistema
# Importa um recurso específico de um módulo.
from pathlib import Path  # Facilita o trabalho com caminhos de arquivos


# Define uma função reutilizável; o bloco indentado abaixo pertence a ela.
def limpar_tela():  # Cria uma função para limpar o terminal
    # Escolhe o comando adequado para o sistema operacional
    # Escolhe o comando de limpeza de tela conforme o sistema operacional.
    comando = "cls" if platform.system() == "Windows" else "clear"

    # Executa o comando para limpar a tela
    # Executa no sistema o comando escolhido para limpar o terminal.
    subprocess.run(comando, shell=True)


# Define os caracteres que podem ser utilizados pela cifra
# A base contém letras minúsculas, acentuadas, símbolos e números
# Define a sequência ordenada de caracteres que a cifra pode transformar.
base = 'abcdefghijklmnopqrstuvwxyzàáâãéêíóôõúüç.,;:!?(){}"-–—_@#%&*+=/$§1234567890'

# Define a quantidade de posições que cada caractere será deslocado
# Define quantas posições cada caractere avança ou retrocede na base.
chave = 3


# Define uma função reutilizável; o bloco indentado abaixo pertence a ela.
def obter_texto():  # Permite digitar um texto ou selecionar um arquivo .txt
    # Guarda a mensagem que será mostrada se ocorrer uma entrada ou operação inválida.
    msg_erro = ""  # Inicializa a mensagem de erro

    # Repete o bloco enquanto a condição for verdadeira.
    while True:  # Mantém o menu funcionando até receber uma entrada válida
        # Chama a função que limpa a tela do terminal.
        limpar_tela()  # Limpa o terminal

        # Exibe a mensagem ou o valor indicado no terminal.
        print('─' * 40)  # Exibe a linha superior do menu
        # Exibe a mensagem ou o valor indicado no terminal.
        print('・┆✦ COMO DESEJA INSERIR O TEXTO? ✦ ┆・'.center(40))
        # Exibe a mensagem ou o valor indicado no terminal.
        print('─' * 40)  # Exibe uma linha divisória
        # Exibe a mensagem ou o valor indicado no terminal.
        print()  # Pula uma linha
        # Exibe a mensagem ou o valor indicado no terminal.
        print('1 - Digitar texto'.center(38))  # Opção para digitar texto
        # Exibe a mensagem ou o valor indicado no terminal.
        print('2 - Abrir arquivo .txt'.center(38))  # Opção para selecionar arquivo
        # Exibe a mensagem ou o valor indicado no terminal.
        print()  # Pula uma linha
        # Exibe a mensagem ou o valor indicado no terminal.
        print('─' * 40)  # Exibe a linha inferior do menu

        # Testa uma condição e executa o bloco abaixo somente se ela for verdadeira.
        if msg_erro:  # Verifica se existe uma mensagem de erro
            # Exibe a mensagem ou o valor indicado no terminal.
            print(msg_erro)  # Exibe a mensagem de erro
            # Guarda a mensagem que será mostrada se ocorrer uma entrada ou operação inválida.
            msg_erro = ""  # Limpa a mensagem para não repeti-la

        # Inicia um bloco protegido para tratar possíveis erros.
        try:  # Inicia o tratamento de entradas inválidas
            # Lê a opção do usuário e converte a entrada para número inteiro.
            escolha = int(input('Opção: '))  # Recebe a opção do usuário

            # Testa uma condição e executa o bloco abaixo somente se ela for verdadeira.
            if escolha == 1:  # Verifica se o usuário escolheu digitar texto
                # Encerra a função e devolve o valor indicado para quem a chamou.
                return input('\nDigite o texto:\n')  # Retorna o texto digitado

            # Testa outra condição caso a condição anterior não tenha sido satisfeita.
            elif escolha == 2:  # Verifica se o usuário escolheu abrir um arquivo

                # Inicia um bloco protegido para tratar possíveis erros.
                try:  # Tenta abrir a janela de seleção de arquivos
                    # Importa um módulo necessário para a funcionalidade indicada.
                    import tkinter as tk  # Importa recursos da interface gráfica
                    # Importa um recurso específico de um módulo.
                    from tkinter import filedialog  # Importa as janelas de seleção

                    # Cria a janela raiz necessária para usar os recursos gráficos do Tkinter.
                    janela = tk.Tk()  # Cria a janela principal do Tkinter
                    # Oculta a janela principal para mostrar apenas a caixa de diálogo.
                    janela.withdraw()  # Esconde a janela principal

                    # Inicia um bloco protegido para tratar possíveis erros.
                    try:
                        # Mantém a janela de seleção à frente das outras
                        # Tenta manter a janela de seleção acima das demais janelas.
                        janela.attributes('-topmost', True)

                        # Abre uma janela para escolher o arquivo de entrada
                        # Abre a caixa de diálogo para selecionar um arquivo e guarda seu caminho.
                        caminho = filedialog.askopenfilename(
                            # Atribui à variável à esquerda o valor ou resultado calculado à direita.
                            parent=janela,
                            # Atribui à variável à esquerda o valor ou resultado calculado à direita.
                            title='Selecione o arquivo de texto',
                            # Atribui à variável à esquerda o valor ou resultado calculado à direita.
                            filetypes=[
                                # Continua a expressão ou a lista iniciada nas linhas anteriores.
                                ('Arquivos de texto', '*.txt'),
                                # Continua a expressão ou a lista iniciada nas linhas anteriores.
                                ('Todos os arquivos', '*.*')
                            # Continua a expressão ou a lista iniciada nas linhas anteriores.
                            ]
                        # Continua a expressão ou a lista iniciada nas linhas anteriores.
                        )

                    # Executa este bloco sempre, ocorrendo erro ou não.
                    finally:
                        # Fecha e libera os recursos da janela gráfica.
                        janela.destroy()  # Fecha a janela do Tkinter

                # Captura o tipo de erro indicado para evitar que o programa pare inesperadamente.
                except Exception:
                    # Usa o terminal se a janela gráfica não estiver disponível
                    # Exibe a mensagem ou o valor indicado no terminal.
                    print('\nNão foi possível abrir a janela de seleção.')
                    # Solicita uma informação ao usuário e guarda ou utiliza o texto digitado.
                    caminho = input(
                        # Fornece um valor textual como argumento da chamada iniciada anteriormente.
                        'Digite o caminho do arquivo .txt:\n'
                    # Continua a expressão ou a lista iniciada nas linhas anteriores.
                    ).strip().strip('"')

                # Verifica se o usuário cancelou a seleção
                # Testa uma condição e executa o bloco abaixo somente se ela for verdadeira.
                if not caminho:
                    # Guarda a mensagem que será mostrada se ocorrer uma entrada ou operação inválida.
                    msg_erro = '\nOperação cancelada. Escolha uma opção novamente.\n'
                    # Executa a instrução indicada nesta linha.
                    continue  # Volta ao menu

                # Converte o caminho informado em um objeto Path
                # Converte o caminho em um objeto Path para manipular o arquivo.
                arquivo_txt = Path(caminho).expanduser()

                # Verifica se o arquivo possui a extensão .txt
                # Testa uma condição e executa o bloco abaixo somente se ela for verdadeira.
                if arquivo_txt.suffix.lower() != '.txt':
                    # Guarda a mensagem que será mostrada se ocorrer uma entrada ou operação inválida.
                    msg_erro = '\nArquivo inválido! Escolha um arquivo .txt.\n'
                    # Executa a instrução indicada nesta linha.
                    continue  # Volta ao menu

                # Abre o arquivo usando UTF-8 e aceita BOM no início do texto
                # Abre o recurso indicado e garante seu fechamento ao sair do bloco.
                with open(arquivo_txt, 'r', encoding='utf-8-sig') as arquivo:
                    # Encerra a função e devolve o valor indicado para quem a chamou.
                    return arquivo.read()  # Lê e retorna todo o conteúdo

            # Executa a instrução indicada nesta linha.
            else:  # Executa se a opção for diferente de 1 ou 2
                # Guarda a mensagem que será mostrada se ocorrer uma entrada ou operação inválida.
                msg_erro = '\nOpção inválida! Escolha apenas 1 ou 2.\n'

        # Captura o tipo de erro indicado para evitar que o programa pare inesperadamente.
        except ValueError:  # Trata entradas que não são números inteiros
            # Guarda a mensagem que será mostrada se ocorrer uma entrada ou operação inválida.
            msg_erro = '\nEntrada inválida! Digite apenas números.\n'

        # Captura o tipo de erro indicado para evitar que o programa pare inesperadamente.
        except FileNotFoundError:  # Trata arquivos que não foram encontrados
            # Guarda a mensagem que será mostrada se ocorrer uma entrada ou operação inválida.
            msg_erro = '\nArquivo não encontrado. Verifique o arquivo escolhido.\n'

        # Captura o tipo de erro indicado para evitar que o programa pare inesperadamente.
        except UnicodeDecodeError:  # Trata problemas de codificação do arquivo
            # Guarda a mensagem que será mostrada se ocorrer uma entrada ou operação inválida.
            msg_erro = '\nNão foi possível ler o arquivo usando UTF-8.\n'

        # Captura o tipo de erro indicado para evitar que o programa pare inesperadamente.
        except OSError as erro:  # Trata outros problemas de acesso ao arquivo
            # Guarda a mensagem que será mostrada se ocorrer uma entrada ou operação inválida.
            msg_erro = f'\nNão foi possível abrir o arquivo: {erro}\n'



# Define uma função reutilizável; o bloco indentado abaixo pertence a ela.
def salvar_resultado(texto, forma):
    # Testa uma condição e executa o bloco abaixo somente se ela for verdadeira.
    if forma == 1:
        # Escolhe o nome do arquivo de saída conforme a operação realizada.
        nome = 'mensagem_criptografada.txt'
    # Executa este bloco quando as condições anteriores não forem satisfeitas.
    else:
        # Escolhe o nome do arquivo de saída conforme a operação realizada.
        nome = 'mensagem_descriptografada.txt'

    # Inicia um bloco protegido para tratar possíveis erros.
    try:
        # No Chromebook, o programa roda no ambiente Linux.
        # Testa uma condição e executa o bloco abaixo somente se ela for verdadeira.
        if platform.system() == "Linux":
            # Define a pasta em que o resultado será salvo.
            pasta_destino = Path.home() / "criptografia"

            # Cria a pasta caso ela ainda não exista.
            # Cria a pasta de destino e as pastas intermediárias, se necessário.
            pasta_destino.mkdir(parents=True, exist_ok=True)

        # Executa este bloco quando as condições anteriores não forem satisfeitas.
        else:
            # No Windows, permite escolher a pasta de destino.
            # Inicia um bloco protegido para tratar possíveis erros.
            try:
                # Importa um módulo necessário para a funcionalidade indicada.
                import tkinter as tk
                # Importa um recurso específico de um módulo.
                from tkinter import filedialog

                # Cria a janela raiz necessária para usar os recursos gráficos do Tkinter.
                janela = tk.Tk()
                # Oculta a janela principal para mostrar apenas a caixa de diálogo.
                janela.withdraw()

                # Inicia um bloco protegido para tratar possíveis erros.
                try:
                    # Tenta manter a janela de seleção acima das demais janelas.
                    janela.attributes('-topmost', True)
                    # Abre a caixa de diálogo para selecionar uma pasta.
                    pasta_escolhida = filedialog.askdirectory(
                        # Atribui à variável à esquerda o valor ou resultado calculado à direita.
                        parent=janela,
                        # Atribui à variável à esquerda o valor ou resultado calculado à direita.
                        title='Escolha onde salvar o resultado'
                    # Continua a expressão ou a lista iniciada nas linhas anteriores.
                    )
                # Executa este bloco sempre, ocorrendo erro ou não.
                finally:
                    # Fecha e libera os recursos da janela gráfica.
                    janela.destroy()

            # Captura o tipo de erro indicado para evitar que o programa pare inesperadamente.
            except Exception:
                # Guarda o caminho da pasta selecionada ou digitada.
                pasta_escolhida = ""

            # Se a janela não abrir, permite informar o caminho.
            # Testa uma condição e executa o bloco abaixo somente se ela for verdadeira.
            if not pasta_escolhida:
                # Exibe a mensagem ou o valor indicado no terminal.
                print('\nInforme o caminho da pasta onde deseja salvar.')
                # Exibe a mensagem ou o valor indicado no terminal.
                print('Pressione Enter para cancelar o salvamento.')
                # Solicita uma informação ao usuário e guarda ou utiliza o texto digitado.
                pasta_escolhida = input('Pasta: ').strip().strip('"')

                # Testa uma condição e executa o bloco abaixo somente se ela for verdadeira.
                if not pasta_escolhida:
                    # Exibe a mensagem ou o valor indicado no terminal.
                    print('\nSalvamento cancelado.')
                    # Encerra a função e devolve o valor indicado para quem a chamou.
                    return None

            # Valida o caminho e solicita novamente se estiver incorreto.
            # Define a pasta em que o resultado será salvo.
            pasta_destino = Path(pasta_escolhida).expanduser()

            # Testa uma condição e executa o bloco abaixo somente se ela for verdadeira.
            if not pasta_destino.is_dir():
                # Exibe a mensagem ou o valor indicado no terminal.
                print('\nO caminho informado não corresponde a uma pasta válida.')
                # Exibe a mensagem ou o valor indicado no terminal.
                print('Digite um caminho de pasta válido (Enter para cancelar):')

                # Repete o bloco enquanto a condição for verdadeira.
                while True:
                    # Solicita uma informação ao usuário e guarda ou utiliza o texto digitado.
                    pasta_escolhida = input().strip().strip('"')

                    # Testa uma condição e executa o bloco abaixo somente se ela for verdadeira.
                    if not pasta_escolhida:
                        # Exibe a mensagem ou o valor indicado no terminal.
                        print('\nSalvamento cancelado.')
                        # Encerra a função e devolve o valor indicado para quem a chamou.
                        return None

                    # Define a pasta em que o resultado será salvo.
                    pasta_destino = Path(pasta_escolhida).expanduser()

                    # Testa uma condição e executa o bloco abaixo somente se ela for verdadeira.
                    if pasta_destino.is_dir():
                        # Encerra imediatamente o laço atual.
                        break

                    # Limpa a tela para ocultar as tentativas anteriores.
                    # Chama a função que limpa a tela do terminal.
                    limpar_tela()
                    # Exibe a mensagem ou o valor indicado no terminal.
                    print('Digite um caminho de pasta válido (Enter para cancelar):')

        # Evita substituir arquivos que já existem.
        # Monta o caminho completo do arquivo de saída.
        caminho_arquivo = pasta_destino / nome
        # Inicializa o número usado para criar nomes alternativos sem sobrescrever arquivos.
        contador = 2

        # Repete o bloco enquanto a condição for verdadeira.
        while caminho_arquivo.exists():
            # Cria um nome alternativo preservando o nome-base e a extensão.
            nome_alternativo = (
                # Executa a instrução indicada nesta linha.
                f'{Path(nome).stem}_{contador}{Path(nome).suffix}'
            # Continua a expressão ou a lista iniciada nas linhas anteriores.
            )
            # Monta o caminho completo do arquivo de saída.
            caminho_arquivo = pasta_destino / nome_alternativo
            # Incrementa o contador para tentar o próximo nome de arquivo.
            contador += 1

        # Salva o resultado em formato de texto.
        # Grava o texto no arquivo usando a codificação UTF-8.
        caminho_arquivo.write_text(texto, encoding='utf-8')

        # Retorna o caminho para exibi-lo depois do resultado na tela.
        # Encerra a função e devolve o valor indicado para quem a chamou.
        return caminho_arquivo

    # Captura o tipo de erro indicado para evitar que o programa pare inesperadamente.
    except OSError as erro:
        # Exibe a mensagem ou o valor indicado no terminal.
        print(f'\nNão foi possível salvar o arquivo: {erro}')
        # Encerra a função e devolve o valor indicado para quem a chamou.
        return None

# Define uma função reutilizável; o bloco indentado abaixo pertence a ela.
def criptografia():  # Controla a criptografia e a descriptografia
    # Guarda a mensagem que será mostrada se ocorrer uma entrada ou operação inválida.
    msg_erro = ""  # Inicializa a mensagem de erro do menu principal

    # Repete o bloco enquanto a condição for verdadeira.
    while True:  # Mantém o menu principal funcionando
        # Chama a função que limpa a tela do terminal.
        limpar_tela()  # Limpa o terminal

        # Exibe a mensagem ou o valor indicado no terminal.
        print('─' * 40)  # Exibe a linha superior
        # Exibe a mensagem ou o valor indicado no terminal.
        print('・┆✦ O QUE VOCE DESEJA FAZER? ✦ ┆・'.center(38))
        # Exibe a mensagem ou o valor indicado no terminal.
        print('─' * 40)  # Exibe uma linha divisória
        # Exibe a mensagem ou o valor indicado no terminal.
        print()  # Pula uma linha
        # Exibe a mensagem ou o valor indicado no terminal.
        print('1 - Criptografar'.center(33))  # Opção de criptografia
        # Exibe a mensagem ou o valor indicado no terminal.
        print('2 - Descriptografar'.center(35))  # Opção de descriptografia
        # Exibe a mensagem ou o valor indicado no terminal.
        print()  # Pula uma linha
        # Exibe a mensagem ou o valor indicado no terminal.
        print('─' * 40)  # Exibe a linha inferior

        # Testa uma condição e executa o bloco abaixo somente se ela for verdadeira.
        if msg_erro:  # Verifica se existe uma mensagem de erro
            # Exibe a mensagem ou o valor indicado no terminal.
            print(msg_erro)  # Exibe a mensagem
            # Guarda a mensagem que será mostrada se ocorrer uma entrada ou operação inválida.
            msg_erro = ""  # Limpa a mensagem

        # Inicia um bloco protegido para tratar possíveis erros.
        try:  # Trata entradas inválidas
            # Lê a operação escolhida e converte a entrada para número inteiro.
            forma = int(input('Opção: '))  # Recebe a operação escolhida

            # Aceita somente as opções 1 e 2
            # Testa uma condição e executa o bloco abaixo somente se ela for verdadeira.
            if forma != 1 and forma != 2:
                # Guarda a mensagem que será mostrada se ocorrer uma entrada ou operação inválida.
                msg_erro = '\nOpção inválida! Escolha apenas 1 ou 2.\n'
                # Executa a instrução indicada nesta linha.
                continue  # Retorna ao menu principal

        # Captura o tipo de erro indicado para evitar que o programa pare inesperadamente.
        except ValueError:  # Trata entradas que não são números inteiros
            # Guarda a mensagem que será mostrada se ocorrer uma entrada ou operação inválida.
            msg_erro = '\nEntrada inválida! Digite apenas números.\n'
            # Executa a instrução indicada nesta linha.
            continue  # Retorna ao menu principal

        # Obtém o texto digitado pelo usuário ou lido de um arquivo.
        texto = obter_texto()  # Obtém o texto digitado ou lido do arquivo
        # Inicializa a string que acumulará o texto transformado.
        resultado = ""  # Inicializa a variável que armazenará o resultado

        # Percorre cada caractere do texto original
        # Percorre os elementos da sequência, um por vez.
        for caractere in texto:
            # Registra se o caractere original era maiúsculo para preservar esse formato.
            maiuscula = caractere.isupper()  # Verifica se era maiúsculo
            # Converte temporariamente o caractere para minúsculo para procurar na base.
            caractere_base = caractere.lower()  # Converte temporariamente para minúsculo
            # Localiza o índice do caractere na base; retorna -1 se não for encontrado.
            posicao = base.find(caractere_base)  # Procura o caractere na base

            # Verifica se o caractere foi encontrado na base
            # Testa uma condição e executa o bloco abaixo somente se ela for verdadeira.
            if posicao != -1:

                # Testa uma condição e executa o bloco abaixo somente se ela for verdadeira.
                if forma == 1:  # Executa se a operação for criptografar
                    # Avança a posição conforme o valor da chave
                    # Avança o índice pela chave e usa módulo para voltar ao início ao ultrapassar o fim.
                    posicao = (posicao + chave) % len(base)

                # Executa a instrução indicada nesta linha.
                else:  # Executa se a operação for descriptografar
                    # Retrocede a posição conforme o valor da chave
                    # Retrocede o índice pela chave e usa módulo para circular até o fim quando necessário.
                    posicao = (posicao - chave) % len(base)

                # Obtém o caractere correspondente à nova posição
                # Seleciona da base o caractere que está na nova posição calculada.
                novo_caractere = base[posicao]

                # Mantém a letra maiúscula quando o original era maiúsculo
                # Testa uma condição e executa o bloco abaixo somente se ela for verdadeira.
                if maiuscula and novo_caractere.isalpha():
                    # Atribui à variável à esquerda o valor ou resultado calculado à direita.
                    novo_caractere = novo_caractere.upper()

                # Adiciona o caractere transformado ao resultado
                # Acrescenta o caractere atual ao texto final.
                resultado += novo_caractere

            # Executa este bloco quando as condições anteriores não forem satisfeitas.
            else:
                # Preserva espaços, quebras de linha e outros caracteres
                # Acrescenta o caractere atual ao texto final.
                resultado += caractere

        # Chama a função que limpa a tela do terminal.
        limpar_tela()  # Limpa a tela antes de exibir o resultado

        # Abre a seleção de pasta e salva o resultado
        # Atribui à variável à esquerda o valor ou resultado calculado à direita.
        caminho_salvo = salvar_resultado(resultado, forma)

        # Armazena a mensagem de erro do menu final.
        msg_erro_minimenu = ""  # Inicializa o erro do menu final

        # Repete o bloco enquanto a condição for verdadeira.
        while True:  # Repete o menu até receber uma opção válida
            # Chama a função que limpa a tela do terminal.
            limpar_tela()
            
            # Mostra o texto final no terminal
            # Exibe a mensagem ou o valor indicado no terminal.
            print('╰┈➤ O texto final fica:', resultado)

            # Mostra o local do arquivo depois de exibir o resultado.
            # Testa uma condição e executa o bloco abaixo somente se ela for verdadeira.
            if caminho_salvo:
                # Exibe a mensagem ou o valor indicado no terminal.
                print(f'\nArquivo salvo em: {caminho_salvo}')
            
            # Exibe a mensagem ou o valor indicado no terminal.
            print()  # Pula uma linha
            # Exibe a mensagem ou o valor indicado no terminal.
            print('─' * 40)  # Exibe a linha superior
            # Exibe a mensagem ou o valor indicado no terminal.
            print('・┆✦ O que deseja fazer agora? ✦ ┆・'.center(38))
            # Exibe a mensagem ou o valor indicado no terminal.
            print('─' * 40)  # Exibe uma linha divisória
            # Exibe a mensagem ou o valor indicado no terminal.
            print()  # Pula uma linha
            # Exibe a mensagem ou o valor indicado no terminal.
            print('1 - Voltar ao menu principal'.center(38))
            # Exibe a mensagem ou o valor indicado no terminal.
            print('2 - Voltar ao inicio'.center(38))
            # Exibe a mensagem ou o valor indicado no terminal.
            print()  # Pula uma linha
            # Exibe a mensagem ou o valor indicado no terminal.
            print('─' * 40)  # Exibe a linha inferior

            # Testa uma condição e executa o bloco abaixo somente se ela for verdadeira.
            if msg_erro_minimenu:  # Verifica se existe uma mensagem de erro
                # Exibe a mensagem ou o valor indicado no terminal.
                print(msg_erro_minimenu)  # Exibe a mensagem
                # Armazena a mensagem de erro do menu final.
                msg_erro_minimenu = ""  # Limpa a mensagem

            # Inicia um bloco protegido para tratar possíveis erros.
            try:  # Trata entradas inválidas
                # Lê a opção escolhida no menu final.
                minimenu = int(input('Opção: '))  # Recebe a opção escolhida

                # Verifica se a opção é válida
                # Testa uma condição e executa o bloco abaixo somente se ela for verdadeira.
                if minimenu == 1 or minimenu == 2:
                    # Executa a instrução indicada nesta linha.
                    break  # Sai do menu final

                # Executa este bloco quando as condições anteriores não forem satisfeitas.
                else:
                    # Armazena a mensagem de erro do menu final.
                    msg_erro_minimenu = (
                        # Fornece um valor textual como argumento da chamada iniciada anteriormente.
                        '\nOpção inválida! Escolha apenas 1 ou 2.\n'
                    # Continua a expressão ou a lista iniciada nas linhas anteriores.
                    )

            # Captura o tipo de erro indicado para evitar que o programa pare inesperadamente.
            except ValueError:  # Trata entradas que não são números inteiros
                # Armazena a mensagem de erro do menu final.
                msg_erro_minimenu = (
                    # Fornece um valor textual como argumento da chamada iniciada anteriormente.
                    '\nEntrada inválida! Digite apenas números.\n'
                # Continua a expressão ou a lista iniciada nas linhas anteriores.
                )

        # Testa uma condição e executa o bloco abaixo somente se ela for verdadeira.
        if minimenu == 1:  # Verifica se o usuário escolheu voltar ao menu
            # Encerra a função e devolve o valor indicado para quem a chamou.
            return  # Encerra a função criptografia

        # Testa outra condição caso a condição anterior não tenha sido satisfeita.
        elif minimenu == 2:  # Verifica se deseja realizar outra operação
            # Guarda a mensagem que será mostrada se ocorrer uma entrada ou operação inválida.
            msg_erro = ""  # Limpa mensagens de erro anteriores
            # O laço principal apresenta novamente o menu de operações
