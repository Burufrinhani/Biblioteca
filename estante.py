class Estante: 
    def __init__(self, livros, qtdLivros, gen, num):
        self.livros = livros
        self.qtdLivros = qtdLivros
        self.gen = gen
        self.num = num

    def __str__(self):
        return f'Livro: {self.livros}\nQuantidade de Livros: {self.qtdLivros}\nGênero da estante: {self.gen}\nLocalização da estante: {self.num}\n'