import os  # Permite trabalhar com pastas, caminhos e arquivos
import platform  # Identifica o sistema operacional utilizado
import subprocess  # Permite executar comandos do sistema

def limpar_tela():  # Cria uma função para limpar o terminal
    comando = "cls" if platform.system() == "Windows" else "clear"  # Escolhe o comando conforme o sistema operacional
    subprocess.run(comando, shell=True)  # Executa o comando para limpar a tela

base = 'abcdefghijklmnopqrstuvwxyzàáâãéêíóôõúüç.,;:!?(){}"-–—_@#%&*+=/$§1234567890'  # Define os caracteres utilizados na cifra, sem duplicar as letras maiúsculas
chave = 3  # Define o número de posições que cada caractere será deslocado
pasta_destino = r"E:\Mensagens_Criptografadas"  # Define a pasta em que os arquivos serão salvos no pendrive

def obter_texto():  # Cria uma função para digitar um texto ou abrir um arquivo
    msg_erro = ""  # Inicializa a mensagem de erro

    while True:  # Mantém o menu funcionando até receber uma entrada válida
        limpar_tela()  # Limpa o terminal
        print('─' * 40)  # Exibe a linha superior do menu
        print('・┆✦ COMO DESEJA INSERIR O TEXTO? ✦ ┆・'.center(40))  # Exibe o título centralizado
        print('─' * 40)  # Exibe uma linha divisória
        print()  # Pula uma linha
        print('1 - Digitar texto'.center(38))  # Exibe a opção para digitar um texto
        print('2 - Abrir arquivo .txt'.center(38))  # Exibe a opção para abrir um arquivo
        print()  # Pula uma linha
        print('─' * 40)  # Exibe a linha inferior do menu

        if msg_erro:  # Verifica se existe uma mensagem de erro
            print(msg_erro)  # Exibe a mensagem de erro
            msg_erro = ""  # Limpa a mensagem para não repeti-la

        try:  # Inicia o tratamento de possíveis entradas inválidas
            escolha = int(input('Opção: '))  # Recebe a opção digitada pelo usuário

            if escolha == 1:  # Verifica se o usuário escolheu digitar um texto
                return input('\nDigite o texto:\n')  # Recebe e retorna o texto digitado

            elif escolha == 2:  # Verifica se o usuário escolheu abrir um arquivo
                caminho = input('\nDigite o caminho do arquivo .txt:\n').strip().strip('"')  # Recebe o caminho e remove espaços e aspas externas

                if not caminho.lower().endswith('.txt'):  # Verifica se o caminho termina em .txt
                    msg_erro = '\nArquivo inválido! Escolha um arquivo .txt.\n'  # Define a mensagem de erro
                    continue  # Retorna ao menu sem exigir que o usuário aperte Enter

                with open(caminho, 'r', encoding='utf-8-sig') as arquivo:  # Abre o arquivo para leitura
                    return arquivo.read()  # Lê e retorna todo o conteúdo do arquivo

            else:  # Executa se o usuário escolher uma opção diferente de 1 ou 2
                msg_erro = '\nOpção inválida! Escolha apenas 1 ou 2.\n'  # Define a mensagem de erro

        except ValueError:  # Trata entradas que não podem ser convertidas em números inteiros
            msg_erro = '\nEntrada inválida! Digite apenas números.\n'  # Define a mensagem de erro

        except FileNotFoundError:  # Trata situações em que o arquivo não foi encontrado
            msg_erro = '\nArquivo não encontrado. Verifique o caminho.\n'  # Define a mensagem de erro

        except UnicodeDecodeError:  # Trata problemas de leitura relacionados à codificação do arquivo
            msg_erro = '\nNão foi possível ler o arquivo usando a codificação esperada.\n'  # Define a mensagem de erro

        except OSError as erro:  # Trata outros problemas ao acessar o arquivo
            msg_erro = f'\nNão foi possível abrir o arquivo: {erro}\n'  # Mostra o motivo do erro


def salvar_resultado(texto, forma):  # Cria uma função para salvar automaticamente o resultado
    nome = 'mensagem_criptografada.txt' if forma == 1 else 'mensagem_descriptografada.txt'  # Define o nome de acordo com a operação
    nome_base, extensao = os.path.splitext(nome)  # Separa o nome do arquivo de sua extensão
    contador = 2  # Define o primeiro número para criar nomes alternativos

    try:  # Inicia o tratamento de erros durante o salvamento
        os.makedirs(pasta_destino, exist_ok=True)  # Cria a pasta de destino caso ela ainda não exista

        caminho_completo = os.path.join(pasta_destino, nome)  # Monta o caminho completo do arquivo

        while os.path.exists(caminho_completo):  # Verifica se já existe um arquivo com esse nome
            nome = f'{nome_base}_{contador}{extensao}'  # Cria um nome alternativo para não sobrescrever o arquivo
            caminho_completo = os.path.join(pasta_destino, nome)  # Atualiza o caminho completo
            contador += 1  # Incrementa o contador para a próxima tentativa

        with open(caminho_completo, 'w', encoding='utf-8') as arquivo:  # Cria o arquivo no destino definido
            arquivo.write(texto)  # Escreve o resultado no arquivo

        print(f'\nArquivo salvo em: {caminho_completo}')  # Informa onde o arquivo foi salvo

    except OSError as erro:  # Trata problemas como pendrive desconectado ou falta de permissão
        print(f'\nNão foi possível salvar o arquivo: {erro}')  # Exibe o motivo do erro


def criptografia():  # Cria a função principal de criptografia e descriptografia
    msg_erro = ""  # Inicializa a mensagem de erro do menu

    while True:  # Mantém o menu funcionando até o usuário decidir voltar
        limpar_tela()  # Limpa o terminal
        print('─' * 40)  # Exibe a linha superior do menu
        print('・┆✦ O QUE VOCE DESEJA FAZER? ✦ ┆・'.center(38))  # Exibe o título centralizado
        print('─' * 40)  # Exibe uma linha divisória
        print()  # Pula uma linha
        print('1 - Criptografar'.center(33))  # Exibe a opção de criptografar
        print('2 - Descriptografar'.center(35))  # Exibe a opção de descriptografar
        print()  # Pula uma linha
        print('─' * 40)  # Exibe a linha inferior do menu

        if msg_erro:  # Verifica se existe uma mensagem de erro
            print(msg_erro)  # Exibe a mensagem de erro
            msg_erro = ""  # Limpa a mensagem para a próxima repetição

        try:  # Inicia o tratamento de entradas inválidas
            forma = int(input('Opção: '))  # Recebe a opção escolhida pelo usuário

            if forma != 1 and forma != 2:  # Verifica se a opção é diferente de 1 e 2
                msg_erro = '\nOpção inválida! Escolha apenas 1 ou 2.\n'  # Define a mensagem de erro
                continue  # Retorna ao início do menu

        except ValueError:  # Trata entradas que não são números inteiros
            msg_erro = '\nEntrada inválida! Digite apenas números.\n'  # Define a mensagem de erro
            continue  # Retorna ao início do menu

        texto = obter_texto()  # Obtém o texto digitado ou o conteúdo de um arquivo
        resultado = ""  # Inicializa a variável que armazenará o resultado

        for caractere in texto:  # Percorre cada caractere do texto original
            maiuscula = caractere.isupper()  # Verifica se o caractere original é uma letra maiúscula
            caractere_base = caractere.lower()  # Converte temporariamente o caractere para minúscula
            posicao = base.find(caractere_base)  # Procura a posição do caractere na base

            if posicao != -1:  # Verifica se o caractere foi encontrado na base
                if forma == 1:  # Verifica se a operação escolhida foi criptografar
                    posicao = (posicao + chave) % len(base)  # Avança a posição conforme a chave
                else:  # Executa quando a operação escolhida é descriptografar
                    posicao = (posicao - chave) % len(base)  # Retrocede a posição conforme a chave

                novo_caractere = base[posicao]  # Obtém o caractere correspondente à nova posição

                if maiuscula and novo_caractere.isalpha():  # Verifica se a letra original era maiúscula
                    novo_caractere = novo_caractere.upper()  # Mantém a letra transformada em maiúscula

                resultado += novo_caractere  # Adiciona o caractere transformado ao resultado

            else:  # Executa quando o caractere não está na base
                resultado += caractere  # Preserva espaços, quebras de linha e caracteres não reconhecidos

        limpar_tela()  # Limpa o terminal antes de apresentar o resultado
        print('╰┈➤ O texto final fica:',resultado)  # Mostra o texto criptografado ou descriptografado

        salvar_resultado(resultado, forma)  # Salva automaticamente o resultado no destino definido

        msg_erro_minimenu = ""  # Inicializa a mensagem de erro do menu final

        while True:  # Mantém o menu final funcionando até receber uma opção válida
            print()  # Pula uma linha
            print('─' * 40)  # Exibe a linha superior
            print('・┆✦ O que deseja fazer agora? ✦ ┆・'.center(38))  # Exibe o título centralizado
            print('─' * 40)  # Exibe uma linha divisória
            print()  # Pula uma linha
            print('1 - Voltar ao menu principal'.center(38))  # Exibe a opção de voltar ao menu principal
            print('2 - Voltar ao inicio'.center(38))  # Exibe a opção de realizar outra operação
            print()  # Pula uma linha
            print('─' * 40)  # Exibe a linha inferior

            if msg_erro_minimenu:  # Verifica se existe uma mensagem de erro
                print(msg_erro_minimenu)  # Exibe a mensagem de erro
                msg_erro_minimenu = ""  # Limpa a mensagem

            try:  # Inicia o tratamento de entradas inválidas
                minimenu = int(input('Opção: '))  # Recebe a opção escolhida

                if minimenu == 1 or minimenu == 2:  # Verifica se a opção é válida
                    break  # Encerra o menu final
                else:  # Executa se a opção não for 1 nem 2
                    msg_erro_minimenu = '\nOpção inválida! Escolha apenas 1 ou 2.\n'  # Define a mensagem de erro

            except ValueError:  # Trata entradas que não são números inteiros
                msg_erro_minimenu = '\nEntrada inválida! Digite apenas números.\n'  # Define a mensagem de erro

        if minimenu == 1:  # Verifica se o usuário escolheu voltar ao menu principal
            return  # Encerra a função de criptografia

        elif minimenu == 2:  # Verifica se o usuário escolheu realizar outra operação
            msg_erro = ""  # Limpa mensagens de erro anteriores
