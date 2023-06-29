class Livro:
    def __init__ (self, titulo, genero, pgs, sinopse, valor):
        self.titulo = titulo
        self.genero = genero
        self.pgs = pgs
        self.sinopse = sinopse
        self.valor = valor

    def __str__(self):
        return f'Título: {self.titulo}\nGênero: {self.genero}\nNúmero de páginas: {self.pgs}\nSinopse: {self.sinopse}\nValor: {self.sinopse}'