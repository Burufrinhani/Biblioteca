class Livro:
    def __init__ (self, informacoes):
        self.titulo = informacoes[0]
        self.genero = informacoes[1]
        self.pgs = informacoes[2]
        self.sinopse = informacoes[3]
        self.valor = informacoes[4]

    def __str__(self):
        return f'Título: {self.titulo}\nGênero: {self.genero}\nNúmero de páginas: {self.pgs}\nSinopse: {self.sinopse}\nValor: {self.valor}\n'
    