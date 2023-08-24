class Caneta:
    def __init__ (self, marca, cor, preco):
        self.marca = marca
        self.cor = cor
        self.preco = preco
        self.tampa = True

    def __str__(self):
        return f'Marca: {self.marca}, Cor: {self.cor}, Preço: {self.preco}, Tampa: {self.tampa}'
    
marca = 'bic'
cor = 'azul'
preco = 1.50

caneta1 = Caneta(marca, cor, 1.50)
caneta2 = Caneta('bic', 'azul', 1.50)

print(caneta1)
print(caneta2)


# Lista/Tupla --> elemento por índice
#     nomeLista[indice]


# Dicionário --> elemento pela chave
#     nomeDicionatio['chave']


# Objeto --> Atributo
#     nomeObjeto.Atributo


# Objeto --> Método
#     nomeObjeto.Método()



# -------------> MÉTODO DE ALUGAR LIVROS: <-------------
# 1º - Mostrar os livros

# 2º - Fazer o cliente selecionar o livro desejado

# 3º - Acessar livro na LISTA de livros (atributo da biblioteca) através da OPÇÃO ESCOLHIDA. 
#      (acesso a elemento da lista = nomeLista[indice])

# 3.5º - Mostrar a lista de clientes (JA EXISTE) e fazer a pessoa selecionar quem ela é

# 3.75 - Acessar cliente na LISTA de clientes (atributo da biblioteca) atraves da OPÇÃO ESCOLHIDA;
#      (acesso a elemento da lista = nomeLista[indice])

# 4º - Adicionar o livro acessado no atributo histórico (lista) da classe Cliente

# 5º - Exibir mensagem para informar que o livro foi alugado com sucesso.
