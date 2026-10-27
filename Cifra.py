# Importa um módulo necessário para a funcionalidade indicada
import platform  # Identifica o sistema operacional utilizado
# Importa um módulo necessário para a funcionalidade indicada
import subprocess  # Permite executar comandos do sistema
# Importa um recurso específico de um módulo
from pathlib import Path  # Facilita o trabalho com caminhos de arquivos


# Define uma função reutilizável; o bloco indentado abaixo pertence a ela
def limpar_tela():  # Cria uma função para limpar o terminal
    # Escolhe o comando de limpeza de tela conforme o sistema operacional
    comando = "cls" if platform.system() == "Windows" else "clear"

    # Executa no sistema o comando escolhido para limpar o terminal
    subprocess.run(comando, shell=True)


# Define os caracteres que podem ser utilizados pela cifra
# Define a sequência ordenada de caracteres que a cifra pode transformar
base = 'abcdefghijklmnopqrstuvwxyzàáâãéêíóôõúüç.,;:!?(){}[]"-—_@#%&*+=/$§1234567890'

# Define quantas posições cada caractere avança ou retrocede na base
chave = 3


# Define uma função reutilizável; o bloco indentado abaixo pertence a ela
def obter_texto():  # Permite digitar um texto ou selecionar um arquivo .txt
    # Guarda a mensagem que será mostrada se ocorrer uma entrada ou operação inválida
    msg_erro = ""  # Inicializa a mensagem de erro

    # Repete o bloco enquanto a condição for verdadeira.
    while True:  # Mantém o menu funcionando até receber uma entrada válida
        # Chama a função que limpa a tela do terminal
        limpar_tela()

        print('─' * 40)  # Exibe 40 traços horizontais para fechar o menu
        print('・┆✦ COMO DESEJA INSERIR O TEXTO? ✦ ┆・'.center(40)) # Centraliza o título do menu
        print('─' * 40)  # Exibe 40 traços horizontais para fechar o menu
        print() 
        print('1 - Digitar texto'.center(38))  # Centraliza a primeira opção do menu
        print('2 - Abrir arquivo .txt'.center(38))  # Centraliza a segunda opção do menu
        print() 
        print('─' * 40)  # Exibe 40 traços horizontais para fechar o menu

        # Testa uma condição e executa o bloco abaixo somente se ela for verdadeira
        if msg_erro:  # Verifica se existe uma mensagem de erro
            # Exibe a mensagem ou o valor indicado no terminal
            print(msg_erro)  # Exibe a mensagem de erro
            msg_erro = ""  # Limpa a mensagem para não repeti-la

        # Inicia um bloco protegido para tratar possíveis erros/entradas inválidas
        try: 
            # Lê a opção do usuário e converte a entrada para número inteiro
            escolha = int(input('Opção: '))  

            # Testa uma condição e executa o bloco abaixo somente se ela for verdadeira
            if escolha == 1:  # Digitar texto
                # Encerra a função e devolve o valor indicado para quem a chamou
                return input('\nDigite o texto:\n')  # Retorna o texto digitado

            # Testa outra condição caso a condição anterior não tenha sido satisfeita
            elif escolha == 2:  # Abrir um arquivo

                # Inicia um bloco protegido para tratar possíveis erros
                try:  # Tenta abrir a janela de seleção de arquivos
                    import tkinter as tk  # Importa recursos da interface gráfica
                    from tkinter import filedialog  # Importa as janelas de seleção

                    # Cria a janela raiz necessária para usar os recursos gráficos do Tkinter
                    janela = tk.Tk()  
                    # Oculta a janela principal para mostrar apenas a caixa de diálogo
                    janela.withdraw()  

                    # Inicia um bloco protegido para tratar possíveis erros
                    try:
                        # Mantém a janela de seleção à frente das outras
                        janela.attributes('-topmost', True)

                        # Abre a caixa de diálogo para selecionar um arquivo e guarda seu caminho
                        caminho = filedialog.askopenfilename(
                            # Janela associada ao seletor
                            parent=janela,
                            # Titulo exibido.
                            title='Selecione o arquivo de texto',
                            # Tipo de arquivos que podem ser selecionados
                            filetypes=[
                                ('Arquivos de texto', '*.txt'),
                                ('Todos os arquivos', '*.*')
                            ]
                        )

                    # Garante que a janela seja fechada mesmo se ocorrer um erro
                    finally:
                        # Fecha a janela
                        janela.destroy()  

                # Se houver uma exceção, uma alternativa será utilizada
                except Exception:
                    # Usa o terminal se a janela gráfica não estiver disponível
                    print('\nNão foi possível abrir a janela de seleção.')
                    # Solicita uma informação ao usuário e guarda ou utiliza o texto digitado
                    caminho = input('Digite o caminho do arquivo .txt:\n').strip().strip('"') # 1- Remove espaços em branco; 2- Remove aspas duplas do início e do fim

                # Verifica se o usuário cancelou a seleção
                # Testa uma condição e executa o bloco abaixo somente se ela for verdadeira
                if not caminho:
                    # Guarda a mensagem que será mostrada se ocorrer uma entrada ou operação inválida.
                    msg_erro = '\nOperação cancelada. Escolha uma opção novamente.\n'
                    continue  # Volta ao menu

                # Converte o caminho em um objeto Path para manipular o arquivo
                arquivo_txt = Path(caminho).expanduser() # Expande o caminho para o diretório do usuário, se necessário

                # Verifica se o arquivo possui a extensão .txt
                # Testa uma condição e executa o bloco abaixo somente se ela for verdadeira
                if arquivo_txt.suffix.lower() != '.txt': # 1- Obtem a extensão do arquivo; 2- Converte para minúsculas para comparação
                    # Guarda a mensagem que será mostrada se ocorrer uma entrada ou operação inválida
                    msg_erro = '\nOperação cancelada. Escolha uma opção novamente.\n'
                    continue  # Volta ao menu

                
                with open(arquivo_txt, 'r', encoding='utf-8-sig') as arquivo: # 1- Abre o arquivo para leitura; 2- Usa a codificação UTF-8 com BOM opcional; 3- Garante que o arquivo será fechado após a leitura
                    # Encerra a função e devolve o valor indicado para quem a chamou
                    return arquivo.read()  

            else:  # Executa se a opção for diferente de 1 ou 2
                # Guarda a mensagem que será mostrada se ocorrer uma entrada ou operação inválida
                msg_erro = '\nOpção inválida! Escolha apenas 1 ou 2.\n'

        except ValueError:  # A entrada não é um número inteiro
            msg_erro = '\nEntrada inválida! Digite apenas números.\n'

        except FileNotFoundError:  # O arquivo não foi encontrado
            msg_erro = '\nArquivo não encontrado. Verifique o arquivo escolhido.\n'

        except UnicodeDecodeError:  # O conteúdo do arquivo não pôde ser lido com a codificação UTF-8
            msg_erro = '\nNão foi possível ler o arquivo usando UTF-8.\n'

        except OSError as erro:  # Ocorreu um erro relacionado ao sistema operacional ao tentar abrir o arquivo
            msg_erro = f'\nNão foi possível abrir o arquivo: {erro}\n'



# Define uma função reutilizável; o bloco indentado abaixo pertence a ela
def salvar_resultado(texto, forma):
    # Testa uma condição e executa o bloco abaixo somente se ela for verdadeira
    if forma == 1:
        # Escolhe o nome do arquivo de saída conforme a operação realizada
        nome = 'mensagem_criptografada.txt'
    # Executa este bloco quando as condições anteriores não forem satisfeitas
    else:
        # Escolhe o nome do arquivo de saída conforme a operação realizada
        nome = 'mensagem_descriptografada.txt'

    # Inicia um bloco protegido para tratar possíveis erros
    try:
        # No Chromebook, o programa roda no ambiente Linux
        # Testa uma condição e executa o bloco abaixo somente se ela for verdadeira
        if platform.system() == "Linux":
            # Define a pasta em que o resultado será salvo
            pasta_destino = Path.home() / "criptografia"

            # Cria a pasta caso ela ainda não exista.
            pasta_destino.mkdir(parents=True, exist_ok=True)

        # Executa este bloco quando as condições anteriores não forem satisfeitas
        else:
            # No Windows, permite escolher a pasta de destino
            # Inicia um bloco protegido para tratar possíveis erros
            try:
                import tkinter as tk
                from tkinter import filedialog

                # Cria a janela raiz necessária para usar os recursos gráficos do Tkinter
                janela = tk.Tk()
                # Oculta a janela principal para mostrar apenas a caixa de diálogo
                janela.withdraw()

                # Inicia um bloco protegido para tratar possíveis erros
                try:
                    janela.attributes('-topmost', True)
                    pasta_escolhida = filedialog.askdirectory(
                        # Janela associada ao seletor
                        parent=janela,
                        # Titulo exibido.
                        title='Escolha onde salvar o resultado'
                    )
                # Garante que a janela seja fechada mesmo se ocorrer um erro
                finally:
                    # Fecha a janela
                    janela.destroy()

            # Se houver uma exceção, uma alternativa será utilizada
            except Exception:
                # Guarda o caminho da pasta selecionada ou digitada
                pasta_escolhida = ""

            # Se a janela não abrir, permite informar o caminho
            # Testa uma condição e executa o bloco abaixo somente se ela for verdadeira
            if not pasta_escolhida:
                print('\nInforme o caminho da pasta onde deseja salvar.')
                print('Pressione Enter para cancelar o salvamento.')
                # Solicita uma informação ao usuário e guarda ou utiliza o texto digitado.
                pasta_escolhida = input('Pasta: ').strip().strip('"') # 1- Remove espaços em branco; 2- Remove aspas duplas do início e do fim

                # Testa uma condição e executa o bloco abaixo somente se ela for verdadeira
                if not pasta_escolhida:
                    print('\nSalvamento cancelado.')
                    # Encerra a função e devolve valoe nenhum
                    return None

            # Valida o caminho e solicita novamente se estiver incorreto
            # Define a pasta em que o resultado será salvo
            pasta_destino = Path(pasta_escolhida).expanduser()

            # Testa uma condição e executa o bloco abaixo somente se ela for verdadeira
            if not pasta_destino.is_dir(): # Verifica se o caminho informado é uma pasta válida
                print('\nO caminho informado não corresponde a uma pasta válida.')
                print('Digite um caminho de pasta válido (Enter para cancelar):')

                # Repete o bloco enquanto a condição for verdadeira.
                while True: # Mantém o loop até que o usuário informe um caminho válido ou cancele
                    pasta_escolhida = input().strip().strip('"') # 1- Remove espaços em branco; 2- Remove aspas duplas do início e do fim

                    # Testa uma condição e executa o bloco abaixo somente se ela for verdadeira
                    if not pasta_escolhida:
                        print('\nSalvamento cancelado.')
                        # Encerra a função e devolve o valor indicado para quem a chamou
                        return None

                    # Define a pasta em que o resultado será salvo.
                    pasta_destino = Path(pasta_escolhida).expanduser()

                    # Testa uma condição e executa o bloco abaixo somente se ela for verdadeira
                    if pasta_destino.is_dir():
                        # Interrompe o loop quando a condição for atendida
                        break

                    # Chama a função que limpa a tela do terminal
                    limpar_tela()
                    # Exibe a mensagem ou o valor indicado no terminal.
                    print('Digite um caminho de pasta válido (Enter para cancelar):')

        # Evita substituir arquivos que já existem
        # Monta o caminho completo do arquivo de saída
        caminho_arquivo = pasta_destino / nome
        # Inicializa o número usado para criar nomes alternativos sem sobrescrever arquivos
        contador = 2

        # Repete o bloco enquanto a condição for verdadeira.
        while caminho_arquivo.exists(): #verifica se o caminho ja existe e cria um nome alternativo caso exista
            nome_alternativo = (
                f'{Path(nome).stem}_{contador}{Path(nome).suffix}' # 1- Obtém o nome do arquivo sem a extensão; 2- Adiciona um número para diferenciar; 3- Mantém a extensão original
            )
            # Monta o caminho completo do arquivo de saída
            caminho_arquivo = pasta_destino / nome_alternativo
            # Incrementa o contador para tentar o próximo nome de arquivo
            contador += 1

        # Grava o texto no arquivo usando a codificação UTF-8
        caminho_arquivo.write_text(texto, encoding='utf-8')

        # Retorna o caminho para exibi-lo depois do resultado na tela
        return caminho_arquivo

    # Se ocorrer um erro relacionado ao sistema operacional, exibe uma mensagem de erro
    except OSError as erro:
        print(f'\nNão foi possível salvar o arquivo: {erro}')
        # Encerra a função e devolve o valor nenhum para quem a chamou
        return None

# Define uma função reutilizável; o bloco indentado abaixo pertence a ela
def criptografia():  # Controla a criptografia e a descriptografia
    msg_erro = ""  # Inicializa a mensagem de erro do menu principal

    # Repete o bloco enquanto a condição for verdadeira
    while True:  # Mantém o menu principal funcionando
        limpar_tela() 

        print('─' * 40) 
        print('・┆✦ O QUE VOCE DESEJA FAZER? ✦ ┆・'.center(38))
        print('─' * 40) 
        print()  
        print('1 - Criptografar'.center(33)) 
        print('2 - Descriptografar'.center(35))  
        print()  
        print('─' * 40) 

        # Testa uma condição e executa o bloco abaixo somente se ela for verdadeira
        if msg_erro:  # Verifica se existe uma mensagem de erro
            # Exibe a mensagem ou o valor indicado no terminal.
            print(msg_erro)  # Exibe a mensagem
            # Guarda a mensagem que será mostrada se ocorrer uma entrada ou operação inválida
            msg_erro = ""  # Limpa a mensagem

        # Inicia um bloco protegido para tratar possíveis erros.
        try:  
            # Lê a operação escolhida e converte a entrada para número inteiro.
            forma = int(input('Opção: '))  # Recebe a operação escolhida

            # Aceita somente as opções 1 e 2
            # Testa uma condição e executa o bloco abaixo somente se ela for verdadeira.
            if forma != 1 and forma != 2: # A entrada nao corresponde a nenhuma das opções válidas
                msg_erro = '\nOpção inválida! Escolha apenas 1 ou 2.\n'
                continue  # Retorna ao menu principal

        # Captura o tipo de erro indicado para evitar que o programa pare inesperadamente
        except ValueError:  # Trata entradas que não são números inteiros
            msg_erro = '\nEntrada inválida! Digite apenas números.\n'
            continue  # Retorna ao menu principal

        # Obtém o texto digitado pelo usuário ou lido de um arquivo.
        texto = obter_texto()  
        resultado = ""  # Inicializa a variável que armazenará o resultado

        # Percorre os elementos da sequência, um por vez.
        for caractere in texto:
            # Verifica se o caractere original era maiúsculo para preservar esse formato
            maiuscula = caractere.isupper() 
            # Converte temporariamente o caractere para minúsculo para procurar na base
            caractere_base = caractere.lower()  
            # Localiza o índice do caractere na base; retorna -1 se não for encontrado
            posicao = base.find(caractere_base) 

            # Verifica se o caractere foi encontrado na base
            if posicao != -1:

                if forma == 1:  # Executa se a operação for criptografar
                    # Avança a posição conforme o valor da chave
                    # Avança o índice pela chave e usa módulo para voltar ao início ao ultrapassar o fim
                    posicao = (posicao + chave) % len(base)

                else:  # Executa se a operação for descriptografar
                    # Retrocede a posição conforme o valor da chave
                    # Retrocede o índice pela chave e usa módulo para circular até o fim quando necessário
                    posicao = (posicao - chave) % len(base)

                # Obtém o caractere correspondente à nova posição
                novo_caractere = base[posicao]

                if maiuscula and novo_caractere.isalpha(): # Verifica se o caractere original era maiúsculo e se o novo caractere é uma letra
                    novo_caractere = novo_caractere.upper() # Converte o novo caractere para maiúsculo para preservar o formato original

                # Adiciona o caractere transformado ao resultado
                resultado += novo_caractere

            else:
                # Preserva espaços, quebras de linha e outros caracteres
                # Acrescenta o caractere atual ao texto final
                resultado += caractere

        limpar_tela()  

        caminho_salvo = salvar_resultado(resultado, forma) # 1- O texto já criptografado ou descriptografado; 2- A operação realizada criptografar ou descriptografar

        # Armazena a mensagem de erro do menu final.
        msg_erro_minimenu = ""  

        # Repete o bloco enquanto a condição for verdadeira.
        while True:  # Repete o menu até receber uma opção válida
            limpar_tela()
            
            # Mostra o texto final no terminal
            print('╰┈➤ O texto final fica:', resultado)

            if caminho_salvo: # Verifica se a função retornou um caminho válido ou none
                print(f'\nArquivo salvo em: {caminho_salvo}')
            
            print()  
            print('─' * 40) 
            print('・┆✦ O que deseja fazer agora? ✦ ┆・'.center(38))
            print('─' * 40)  
            print()  
            print('1 - Voltar ao menu principal'.center(38))
            print('2 - Voltar ao inicio'.center(38))
            print()  
            print('─' * 40)  #

            # Testa uma condição e executa o bloco abaixo somente se ela for verdadeira.
            if msg_erro_minimenu:  # Verifica se existe uma mensagem de erro
                # Exibe a mensagem ou o valor indicado no terminal.
                print(msg_erro_minimenu)  # Exibe a mensagem
                # Armazena a mensagem de erro do menu final.
                msg_erro_minimenu = ""  # Limpa a mensagem

            # Inicia um bloco protegido para tratar possíveis erros.
            try:  # Trata entradas inválidas
                minimenu = int(input('Opção: '))  # Recebe a opção escolhida

                if minimenu == 1 or minimenu == 2: # A condição e verdadeira quando a entrada corresponde a qualquer uma das opções válidas
                    break  # Sai do menu final

                # Executa este bloco quando as condições anteriores não forem satisfeitas.
                else:
                    # Armazena a mensagem de erro do menu final.
                    msg_erro_minimenu = ('\nOpção inválida! Escolha apenas 1 ou 2.\n')

            # Captura o tipo de erro indicado para evitar que o programa pare inesperadamente.
            except ValueError:  # Trata entradas que não são números inteiros
                msg_erro_minimenu = ( '\nEntrada inválida! Digite apenas números.\n')

        if minimenu == 1:  # Verifica se o usuário escolheu voltar ao menu
            return  # Encerra a função criptografia

        # Testa outra condição caso a condição anterior não tenha sido satisfeita.
        elif minimenu == 2:  # Verifica se deseja realizar outra operação
            msg_erro = ""  # Limpa mensagens de erro anteriores
            # O laço principal apresenta novamente o menu de operações
