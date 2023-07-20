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
