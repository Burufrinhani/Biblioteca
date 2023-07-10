import livro

livros = [("O Amor Proibido", "Romance", 350, "Em um mundo dividido por ódio e preconceito, dois jovens de famílias rivais se apaixonam intensamente, desafiando todas as expectativas e enfrentando grandes obstáculos para ficarem juntos.", 29.90), ("l2", "gen2", 2, "sin2", 0.50)]

referencias = []

for livs in livros:
    print(livs)

    l1 = livro.Livro(livs)

    referencias.append(l1)


for liv in referencias:
    print(liv)

# tupla       - ()
# lista       - []
# dicionario  - {}



















































livros = []



# livros.append(l1)
# livros.append(l2)
# livros.append(l3)

# livros.extend([l1, l2, l3])
# 
# print(livros)
# 
# for livro in livros:
#     print(livro[0])


def criaLivro():
    tup = ()

    tit = input("Título: ")
    tup = (tit,)

    gen = input("Gênero: ")
    tup += (gen,)

    qtd_pags = int(input("Quantidade de Páginas: "))
    tup += (qtd_pags,)

    sin = input("Sinopse: ")
    tup += (sin,)

    val = float(input("Valor: "))
    tup += (val,)

    return tup


info_livros = []
refs_livros = []

for c in range(0, 2):
    info_livros.append(criaLivro())

print(info_livros)

for liv in info_livros:
    obj_livro = livro.Livro(liv)
    refs_livros.append(obj_livro)

for liv in refs_livros:
    print(liv)