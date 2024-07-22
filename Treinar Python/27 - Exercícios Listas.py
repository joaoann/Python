# Soma dos elementos de cada lista da lista
def exercicio_1():
    lista_de_listas = [[4,6,5,9], [1,0,7,2], [3,4,1,8]]

    somatoria = [sum(lista) for lista in lista_de_listas]
    print(somatoria)

# Armazena o terceiro elemento de cada tupla
def exercicio_2():
    lista_de_tuplas = [('Pedro', 1.74, 81), ('Júlia', 1.65, 67), ('Otávio', 1.81, 83)]

    terceiro_elemento = [lista_de_tuplas[i][2] for i in range(len(lista_de_tuplas))]
    print(terceiro_elemento)

# A partir de uma lista retornar uma tupla com o nome e a posição do nome
def exercicio_3():
    lista = ['Pedro', 'Júlia', 'Otávio', 'Eduardo']
    lista_de_tuplas = []
    posicao = 1

    for i in range(len(lista)):
        lista_de_tuplas.append((posicao, lista[i]))
        posicao += 1

    print(lista_de_tuplas)

# Retornar uma lista com apenas os alugueis de apartamentos
def exercicio_4():
    aluguel = [('Apartamento', 1700), ('Apartamento', 1400), ('Casa', 2150), ('Apartamento', 1900), ('Casa', 1100)]
    aluguel_apt = [aluguel[i][1] for i in range(len(aluguel)) if aluguel[i][0] == 'Apartamento']

    print(aluguel_apt)

# Associar cada mês a um valor e fazer um dicionario
def exercicio_5():
    meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
    despesa = [860, 490, 1010, 780, 900, 630, 590, 770, 620, 560, 840, 360]

    dicionario = {meses[i]: despesa[i] for i in range(len(meses))}
    print(dicionario)

# Retornas anos de 2022 e com venda maior que 6000
def exercicio_6():
    vendas = [('2023', 4093), ('2021', 4320), ('2021', 5959), ('2022', 8883), ('2023', 9859), ('2022', 5141), ('2022', 7688), ('2022', 9544), ('2023', 4794), ('2021', 7178), ('2022', 3030), ('2021', 7471), ('2022', 4226), ('2022', 8190), ('2021', 9680), ('2022', 5616)]

    vendas_filtrada = [vendas[i][1] for i in range(len(vendas)) if vendas[i][0] == '2022' and vendas[i][1] > 6000]
    print(vendas_filtrada)

# Retorna o nivel da glicose e o valor
def exercicio_7():
    glicemia = [129, 82, 60, 97, 101, 65, 62, 167, 87, 53, 58, 92, 66, 120, 109, 62, 86, 96, 103, 88, 155, 52, 89, 73]

    # Glicose igual ou inferior a 70: 'Hipoglicemia'
    # Glicose entre 70 a 99: 'Normal'
    # Glicose entre 100 e 125: 'Alterada'
    # Glicose superior a 125: 'Diabetes'

    rotulos = [('Hipoglicemia', glicose) if glicose <= 70 else ('Normal', glicose) if glicose < 100 else ('Alterada', glicose) if glicose < 125 else ('Diabetes', glicose) for glicose in glicemia]
    print(rotulos)

# O e-commerce precisa estruturar esses dados em uma tabela contendo o valor 
# total da venda, que é obtida multiplicando a quantidade pelo preço unitário. 
# Além disso, a tabela precisa conter um cabeçalho indicando 
# as colunas: 'id', 'quantidade', 'preco' e 'total'.
def exercicio_8():

    id = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    quantidade = [15, 12, 1, 15, 2, 11, 2, 12, 2, 4]
    preco = [93.0, 102.0, 18.0, 41.0, 122.0, 14.0, 71.0, 48.0, 14.0, 144.0]
    tabela = [('id', 'quantidade', 'preco', 'total')]
    
    tabela += [(id[i], quantidade[i], preco[i], quantidade[i] * preco[i]) for i in range(len(id))]

    print(tabela)

# Crie um dicionário usando dict comprehension com a chave sendo 
# o nome de um Estado e o valor sendo a contagem de vezes em que o Estado aparece na lista.
def exercicio_9():
    estados = ['SP', 'ES', 'MG', 'MG', 'SP', 'MG', 'ES', 'ES', 'ES', 'SP', 'SP',
            'MG', 'ES', 'SP', 'RJ', 'MG', 'RJ', 'SP', 'MG', 'SP', 'ES', 'SP', 'MG']

    estados_unicos = list(set(estados))
    listagem_unica = []

    for estado in estados_unicos:
        lista = [uf for uf in estados if uf == estado]
        listagem_unica.append(lista)

    qtde_estados = {listagem_unica[i][0]: len(listagem_unica[i]) for i in range(len(listagem_unica))}
    print(qtde_estados)

# Dicionário em que as chaves são os nomes dos Estados e os valores são a soma de funcionários por Estado.
def exercicio_10():
    funcionarios = [('SP', 16), ('ES', 8), ('BA', 99) , ('MG', 9), ('MG', 6), ('SP', 10), ('MG', 4), ('ES',9), ('ES', 7),
                    ('ES', 12), ('SP', 7),('SP', 11), ('MG',8), ('ES',8), ('SP',9), ('RJ', 13), ('MG', 5), 
                    ('RJ', 9), ('SP', 12), ('MG', 10), ('SP', 7), ('ES', 14), ('SP', 10), ('MG', 12), ('BA', 4),
                    ('AL', 2), ('SP', 9)]

    estados_unicos = list(set([tupla[0] for tupla in funcionarios]))
    qtde_total = []

    for estado in estados_unicos:
        qtde = sum([func[1] for func in funcionarios if func[0] == estado])
        qtde_total.append(qtde)

    func_por_estado = {estados_unicos[i]: qtde_total[i] for i in range(len(estados_unicos))}
    print(func_por_estado)

