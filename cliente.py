class Cliente: 
    def __init__(self, nome, telefone, endereco):
        self.nome = nome
        self.telefone = telefone
        self.endereco = endereco
        self.historico = []

    def __str__(self):
        return f'Nome: {self.nome}\nTelefone: {self.telefone}\nEndereço: {self.endereco}\nHistórico de livros alugados: {self.historico}'
    
    