class Estante: 
    def __init__(self, listaLivro, capacidade, gen, num):
        self.livros = listaLivro
        self.qtdLivros = len(listaLivro)
        self.capacidade = capacidade
        self.gen = gen
        self.num = num

    def __str__(self):
        return f'Livro: {self.livros}\nQuantidade de Livros: {self.qtdLivros}\nGênero da estante: {self.gen}\nLocalização da estante: {self.num}\n'