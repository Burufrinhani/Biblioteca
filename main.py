from os import system
import datetime
import biblioteca as bibli_arq

system('cls')
biblioteca = bibli_arq.Biblioteca()

def definirSaudacao():
    hora = int((datetime.datetime.now()).strftime("%H"))

    if hora < 12:
        saud = "Bom dia!"
    elif 12 <= hora < 18:
        saud = "Boa tarde!"
    else:
        saud = "Boa noite!"

    return saud

print(f'{definirSaudacao()}\nInsira a opção que deseja. \n')


while True:
    print('1. Entrada e saída de livros \n2. Busca de livros \n3. Opções de gêneros \n4. Localização dos títulos \n5. Sair')

    opcao = int(input('Insira a opção que deseja consultar: '))
    
    system('cls')

    if opcao == 1:
        print('Entrada e saída de livros. \n')

        while True:
            print('1.Inserir livro: \n2.Remover livro: ')
            entradaSaida = int(input())

            if entradaSaida == 1:
                biblioteca.adicionarLivro()

                break

            elif entradaSaida == 2:
                biblioteca.removerLivro()
    
    elif opcao == 2:
        
        while True:
            print('Busca de livros.\n')
            opOrdem = int(input('1. Alfabética.\n2. Número de páginas.\n3. Preço\n\nEscolha a ordem de exibição: '))

            if opOrdem == 1:
                biblioteca.exibirAlfabetica()
                
            elif opOrdem == 2:
                biblioteca.exibirNum()
                
            elif opOrdem == 3:  
                biblioteca.exibirPreco()
                
            else:
                system('cls')
                print('Opção inválida.')


    elif opcao == 3:
        print('Opções de gêneros.')

        biblioteca.opcoesGenero()


    elif opcao == 4:
        print('Localização dos títulos')

        biblioteca.exibirAlfabetica()
        livroEscolhido = int(input('Escolha o livro de que deseja, atráves de seu número: '))

        biblioteca.escolherLivro(livroEscolhido)
        

    elif opcao == 5:
        break


    else:
        print('Opçao inválida, digite novamente.')

print("Programa finalizado.")