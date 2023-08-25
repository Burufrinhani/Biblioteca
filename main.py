from os import system
import biblioteca as bibli_arq
import uteis
# from tkinter import * 
# from tkinter import messagebox


system('cls')
biblioteca = bibli_arq.Biblioteca()

uteis.definirSaudacao()

while True:
    print('1. Entrada e saída de livros \n2. Busca de livros \n3. Opções de gêneros \n4. Localização dos títulos \n5. Alugar livro \n\n6. Sair')
    print("."*38)

    opcao = int(input('Insira a opção que deseja consultar: '))
    
    system('cls')

    if opcao == 1:
        uteis.formataTitulo('Entrada e saída de livros.')

        while True:
            print('1. Inserir livro \n2. Remover livro\n')
            entradaSaida = int(input("Digite a opção que deseja: "))

            if entradaSaida == 1:
                biblioteca.adicionarLivro()
                break

            elif entradaSaida == 2:
                biblioteca.removerLivro()
    

    elif opcao == 2:
        while True:
            uteis.formataTitulo('Busca de livros.')
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
        uteis.formataTitulo('Opções de gêneros.')
        biblioteca.opcoesGenero()


    elif opcao == 4:
        uteis.formataTitulo('Localização dos títulos')

        biblioteca.escolherLivro()
        

    elif opcao == 5:
        uteis.formataTitulo('Alugar livro')
        biblioteca.alugarLivros()
        break


    elif opcao == 6:
        break

    else:
        uteis.formataTitulo('Opçao inválida, digite novamente.')

print("Programa finalizado.")