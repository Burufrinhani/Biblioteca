import livro as liv_arq
import estante as est_arq
from os import system

livros = [("Amor Proibido", "Romance", 350, "Em um mundo dividido por ódio e preconceito, dois jovens de famílias rivais se apaixonam intensamente, desafiando todas as expectativas e enfrentando grandes obstáculos para ficarem juntos.", 34.90), 
("A Promessa de um Novo Amanhã", "Romance", 400, "Após uma grande perda, uma mulher decide recomeçar sua vida em uma cidade pequena. Lá, ela conhece um homem misterioso que a ajuda a curar seu coração ferido e a encontrar a felicidade novamente.", 44.90),
("Entre Dois Mundos", "Romance", 280, "Uma história de amor que transcende fronteiras e culturas. Um casal improvável luta contra as diferenças e as adversidades para viver um amor verdadeiro, enfrentando o desafio de conciliar suas identidades e raízes.", 27.90),
("A Melodia do Coração", "Romance", 320, "Uma talentosa musicista encontra o amor em um enigmático compositor. Juntos, eles descobrem que a música pode curar feridas e conectar almas, enquanto enfrentam seus próprios medos e inseguranças.", 31.90),
("Destinos Entrelaçados", "Romance", 350, "Em um encontro inesperado, dois estranhos descobrem uma conexão profunda e inexplicável. Ao longo do tempo, seus caminhos continuam se cruzando, revelando que o destino pode ser mais poderoso do que imaginavam.", 34.90),

("Além do Horizonte", "Ficção Científica", 400, "Em um futuro distante, a humanidade descobre uma forma revolucionária de viagem espacial. Uma equipe de exploradores embarca em uma jornada além dos limites conhecidos do universo, desvendando segredos cósmicos e enfrentando dilemas éticos que desafiam a própria essência da humanidade.", 44.90),
("A Cidade das Máquinas", "Ficção Científica", 350, "Em uma sociedade dominada por máquinas inteligentes, um grupo de rebeldes busca libertar a humanidade do controle opressivo. Nessa batalha entre homens e máquinas, segredos antigos são revelados, e a esperança de um futuro livre depende de uma escolha impossível.", 34.90),
("O Último Horizonte", "Ficção Científica", 300, "Em um mundo devastado por catástrofes naturais, a humanidade luta pela sobrevivência. Uma equipe de cientistas e aventureiros parte em uma missão desesperada para encontrar um novo lar em outro planeta. A jornada é repleta de perigos desconhecidos e dilemas éticos, enquanto eles enfrentam o fim da civilização como a conhecemos.", 29.90),
("A Realidade Virtual", "Ficção Científica", 280, "Em um futuro próximo, a tecnologia de realidade virtual atinge um nível avançado, permitindo que as pessoas vivam em mundos digitais perfeitos. Porém, à medida que a linha entre realidade e virtualidade se torna tênue, um grupo de hackers tenta desvendar uma conspiração que ameaça a liberdade de toda a humanidade.", 27.90),
("Conexão Quântica", "Ficção Científica", 320, "Um cientista brilhante descobre uma maneira de viajar entre realidades paralelas por meio da física quântica. Enquanto explora esses mundos alternativos, ele se depara com versões diferentes de si mesmo e enfrenta um dilema moral: até onde ele está disposto a ir para salvar sua própria realidade?", 31.90),

("Legado entre Reinos", "Fantasia", 400, "Em um mundo onde a magia foi esquecida, um jovem descobre que é o herdeiro de um antigo reino encantado. Ele deve embarcar em uma jornada perigosa para restaurar a magia e derrotar as forças das trevas que ameaçam dominar o mundo.", 44.90),
("Filha dos Elementos", "Fantasia", 350, "Uma garota com poderes misteriosos é a única esperança para restaurar o equilíbrio entre os quatro elementos: terra, fogo, ar e água. Ela precisa dominar suas habilidades e enfrentar uma antiga profecia para salvar o mundo da destruição iminente.", 34.90),
("Portal dos Sonhos", "Fantasia", 300, "Uma jovem descobre um portal mágico que a transporta para um mundo de sonhos e imaginação. Lá, ela encontra criaturas fantásticas, desvenda enigmas antigos e aprende lições valiosas sobre coragem, amizade e autodescoberta.", 29.90),
("A Espada do Destino", "Fantasia", 380, " Uma antiga profecia anuncia a chegada de um herói destinado a empunhar a lendária Espada do Destino e derrotar o mal que assola o reino. Acompanhe a jornada desse jovem guerreiro enquanto ele enfrenta criaturas místicas, supera desafios e descobre seu verdadeiro propósito.", 37.90),
("O Reino Esquecido", "Fantasia", 320, "Em um reino esquecido pelos livros de história, um grupo de aventureiros se reúne para desvendar os segredos de um passado perdido. Eles enfrentam perigosas criaturas mágicas, exploram ruínas antigas e desenterram uma conspiração que poderia abalar os alicerces do mundo conhecido.", 31.90),

("O Enigma da Mansão Sinclair", "Mistério", 320, " Quando um famoso magnata é encontrado morto em circunstâncias misteriosas, um detetive renomado é chamado para desvendar o crime. Ele se vê preso em um emaranhado de segredos familiares, intrigas e revelações chocantes enquanto investiga a sombria mansão Sinclair em busca da verdade.", 31.90),
("A Trama Oculta", "Mistério", 400, "Uma escritora de sucesso recebe um manuscrito anônimo que revela segredos obscuros de sua própria vida. Determinada a descobrir a identidade do autor e a verdade por trás das revelações, ela mergulha em uma trama complexa e perigosa que ameaça destruir tudo o que ela conhece.", 44.90),
("O Caso do Relógio Desaparecido", "Mistério", 280, "Um detetive excêntrico e perspicaz é chamado para resolver o desaparecimento de um valioso relógio antigo em uma cidade pacata. À medida que ele segue as pistas, segredos sombrios vêm à tona, levando-o a desvendar uma teia de mentiras e traições.", 27.90),
("A Marca do Silêncio", "Mistério", 350, "Uma série de assassinatos brutais assombra uma pequena cidade. Uma jovem repórter, determinada a descobrir a verdade, se envolve em uma perigosa investigação, onde nada é o que parece. Enquanto ela segue o rastro do assassino, ela se vê confrontando segredos obscuros que ameaçam sua própria vida.", 34.90),
("O Mistério da Herança Perdida", "Mistério", 300, "Um jovem herda uma mansão isolada e uma fortuna considerável de um parente distante, mas logo descobre que há muito mais do que dinheiro em jogo. Ele se vê envolvido em uma trama complexa de mistérios familiares, segredos enterrados e perigos iminentes enquanto tenta desvendar o mistério da herança perdida.", 29.90),

("Rindo às Gargalhadas", "Comédia", 280, "A vida de um comediante em ascensão é repleta de situações hilárias e encontros improváveis. Ele enfrenta os desafios do mundo do humor, desde os palcos até os bastidores, enquanto tenta equilibrar sua vida profissional e pessoal com muito bom humor.", 27.90),
("Confusões em Série", "Comédia", 350, "Um protagonista azarado e desastrado se envolve em uma série interminável de confusões hilárias. Desde mal-entendidos embaraçosos até situações absurdas do dia a dia, ele vive uma comédia de erros que arranca risadas do leitor em cada capítulo.", 34.90),
("As Aventuras do Desastrado", "Comédia", 320, "Um personagem atrapalhado e cheio de boa vontade se mete em diversas situações cômicas enquanto tenta encontrar seu lugar no mundo. Com uma sequência de desventuras e equívocos hilariantes, ele nos faz rir com suas desajeitadas aventuras.", 31.90),
("Amores e Desventuras", "Comédia", 400, "Uma história repleta de encontros e desencontros amorosos, com personagens excêntricos e situações divertidas. O protagonista se envolve em uma série de relacionamentos malucos, causando situações hilárias e imprevistos cômicos ao longo do caminho.", 44.90),
("Rir é o Melhor Remédio", "Comédia", 300, "Um livro repleto de piadas, trocadilhos e histórias engraçadas para alegrar o dia a dia do leitor. Com uma seleção diversificada de humor, desde piadas clássicas até anedotas contemporâneas, o livro oferece momentos de riso e descontração em cada página.", 29.90)]

romance = []
ficcao = []
fantasia = []
misterio = []
comedia = []

ref_Livro = []

for livs in livros:
    l1 = liv_arq.Livro(livs)

    ref_Livro.append(l1)


for livro in ref_Livro:
    if livro.genero == "Romance":
        romance.append(livro)
    
    elif livro.genero == "Ficção Científica":
        ficcao.append(livro)

    elif livro.genero == "Fantasia":
        fantasia.append(livro)

    elif livro.genero == "Mistério":
        misterio.append(livro)

    elif livro.genero == "Comédia":
        comedia.append(livro)


generos = {'Romance': romance, 'Ficção Científica': ficcao, 'Fantasia': fantasia, 'Mistério': misterio, 'Comédia': comedia}

ref_estante = []

c = 1
for k, v in generos.items():
    e1 = est_arq.Estante(v, 30, k, c)
    c += 1

    ref_estante.append(e1)

class Biblioteca:
    def __init__(self):
        self.livros = ref_Livro
        self.generos = generos
        self.estantes = ref_estante

    def opcoesGenero(self):
        c = 1
        for k in generos.keys():
            print(f'{c}. {k}')
            c += 1
        print('0. Sair')
        opt = int(input("Digite o gênero que deseja: "))

        if opt == 1:
            self.opcoesLivro(generos["Romance"])
        elif opt == 2:
            self.opcoesLivro(generos["Ficção Científica"])
        elif opt == 3:
            self.opcoesLivro(generos["Fantasia"])
        elif opt == 4:
            self.opcoesLivro(generos["Mistério"])
        elif opt == 5:
            self.opcoesLivro(generos["Comédia"])
        elif opt == 0:
            self.sair()
        else:
            print("Opção Inválida")
            
    def opcoesLivro(self, genero):
        system('cls')

        for livro in genero:
            print(f'- {livro.titulo}')

    def exibirAlfabetica(self, saida=True):
        self.livros = sorted(self.livros, key=lambda livros: livros.titulo)

        c = 1
        for livro in self.livros:
            print(f'{c}. {livro.titulo}')
            c += 1

        if saida:
            self.sair()
            
    def exibirNum(self):
        self.livros = sorted(self.livros, key=lambda livros: livros.pgs)

        for livro in self.livros:
            print(f'{livro.titulo}: {livro.pgs} páginas')

        self.sair()

    def exibirPreco(self):
        self.livros = sorted(self.livros, key=lambda livros: livros.valor)
        
        for livro in self.livros:
            print(f'{livro.titulo}: R$ {livro.valor}')

        self.sair()

    def escolherLivro(self):
        self.exibirAlfabetica()

        livroEscolhido = int(input('\nEscolha o livro de que deseja, atráves de seu número: '))

        system('cls')

        liv = self.livros[livroEscolhido - 1]

        for estante in self.estantes:
            for livro in estante.livros:
                if livro.titulo == liv.titulo:
                    gen = estante.gen
                    est = estante.num

        print(f'O livro {liv.titulo} está na estante {est}, com gênero {gen}.')

        self.sair()

    def adicionarLivro(self):
        titulo = str(input("Informe o título do livro: "))
        genero = str(input("Informe o gênero do livro: "))
        paginas = int(input("Informe a quantidade de páginas do livro: "))
        sinopse = str(input("Informe a sinopse do livro: "))
        preco = float(input("Informe o preço do livro: "))

        info = (titulo, genero, paginas, sinopse, preco)

        novo_livro = liv_arq.Livro(info)

        ref_Livro.append(novo_livro)

        print(f'O livro "{titulo}" foi adicionado à biblioteca.')

    def removerLivro(self):
        self.exibirAlfabetica(False)
        indice = int(input('\nDigite o índice do livro que deseja remover: '))

        livroRemovido = self.livros[indice - 1]

        self.livros.pop(indice - 1)

        print(f'O livro \"{livroRemovido.titulo}\" foi removido')

    def sair(self):
        while True:
            txt = str(input('\nDigite \"voltar\" para retornar ao menu principal: '))

            if txt.lower().strip() == "voltar":
                system('cls')
                break

    def alugarLivros(self):
        self.exibirAlfabetica()

        livroAlugado = int(input('\nDigite o índice do livro de deseja alugar: '))

        livro = self.livros[livroAlugado - 1]

        system('cls')

        print(f'\nO livro que deseja alugar é "{livro.titulo}"?')
        opcao = int(input((f'\nDigite 1 para confirmar e 2 para selecionar outro título.\n')))

        system('cls')

        if opcao == 1:
            print('Livro selecionado.')
            nome = str(input('Informe seu nome para criar um cadatro na biblioteca: ')).strip()

            system('cls')

            print(f'{nome}, o livro "{livro.titulo}" foi registrado em seu nome!\nContamos que mantenha-o num bom estado e que a devolução seja feita no prazo estipulado.')

            self.sair()

        else:
            self.exibirAlfabetica()

            livroAlugado = int(input('\nDigite o índice do livro de deseja alugar: '))

            livro = self.livros[livroAlugado - 1]

            print(f'O livro que deseja alugar é {livro.titulo}?')
            opcao = input((f'Digite 1 para confirmar e 2 para selecionar outro título.\n'))
                