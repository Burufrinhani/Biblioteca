from os import system
import datetime
import estante, livro, cliente

system('cls')

def definirSaudacao():
    hora = int((datetime.datetime.now()).strftime("%H"))

    if hora < 12:
        saud = "Bom dia!"
    elif 12 <= hora < 18:
        saud = "Boa tarde!"
    else:
        saud = "Boa noite!"

    return saud

# estante1 = estante.Estante("Qualquer coisa", 5, "Suspense", 1)
# 
# print(estante1)

print(f'{definirSaudacao()} Insira a opção que deseja. \n')

while True:
    print('1. Entrada e saída de livros \n2. Busca de livros \n3. Opções de gêneros \n4. Localização dos títulos \n5. Sair')

    opcao = int(input('Insira a opção que deseja consultar: '))
    
    system('cls')

    if opcao == 1:
        print('Entrada e saída de livros. \n')

    elif opcao == 2:
        print('Busca de livros.')

    elif opcao == 3:
        print('Opções de gêneros.')

    elif opcao == 4:
        print('Localização dos títulos')

    elif opcao == 5:
        break    

    else:
        print('Opçao inválida, digite novamente.')


print("Programa finalizado.")