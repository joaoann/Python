# Divisão de dois floats com tratamento para erro divisivel por zero e entrada string
def exercicio_1():
    try:
        numero_1 = float(input('Digite o primeiro número: '))
        numero_2 = float(input('Digite o segundo número: '))
        resultado = numero_1 / numero_2
    except ValueError:
        print('O valor digitado não é um número')
    except ZeroDivisionError:
        print('Não é possível dividir por zero')
    else:
        print(resultado)

# Retornar a idade e uma lista de nomes
def exercicio_2():
    try:
        idades = {'Júlia': 16, 'Carol': 23, 'Alberto': 19, 'Roberta': 17}
        nome = input('Digite um nome: ')
        print(idades[nome])
    except KeyError:
        print('Nome não encontrado')

# Converter os elementos de uma lista para float. Se der erro, informar o erro.
def exercicio_3():
    try:
        lista = [2, 32, '54', 4.23]
        lista_convertida = []
        for i in range(len(lista)):
            lista_convertida.append(float(lista[i]))
    except Exception as e:
        print(f'Erro: {e}')
    else:
        print(lista_convertida)
    finally:
        print('Fim da excução da função')

# Juntar duas listas e somar
def exercicio_4():
    try:
        lista_1 = [1, 4, 6, 9]
        lista_2 = [2, 3, 4, 3]
        listas_juntas = [(lista_1[i], lista_2[i], lista_1[i] + lista_2[i]) for i in range(len(lista_1))]
    except IndexError:
        print('A quantidade de elementos em cada lista é diferente')
    except TypeError:
        print('Um dos valores não é um número')
    except Exception as e:
        print(f'Erro {e}')
    else:
        print(listas_juntas)

# Verificar gabarito com apenas 5 respostas e 4 letras como resposta
def exercicio_5():
    respostas = [['D', 'A', 'B', 'C', 'D'], ['C', 'A', 'A', 'C', 'A'], ['D', 'B', 'A', 'C', 'A']]
    gabarito = ['D', 'A', 'B', 'C', 'A']
    notas = []

    # Verificar se as respostas são válidas
    for lista in respostas:
        for letra in lista:
            if letra not in ['A', 'B', 'C', 'D']:
                raise ValueError(f'A alternativa {letra} não é uma opção de alternativa válida')
            elif len(lista) != 5:
                raise IndexError(f'Uma das notas tem menos que 5 alternativas')
            
    # Verificar notas
    for lista in respostas:
        somatoria = 0
        for i in range(len(lista)):
            if lista[i] == gabarito[i]:
                somatoria += 1
        notas.append(somatoria)

    print(notas)

# Ver se há pontuação nas palavras de uma lista
def exercicio_6():
    try:    
        # lista_tratada = ['Python', 'é', 'uma', 'linguagem', 'de', 'programação', 'poderosa', 'versátil', 'e', 'fácil', 'de', 'aprender', 'utilizada', 'em', 'diversos', 'campos', 'desde', 'análise', 'de', 'dados', 'até', 'inteligência', 'artificial']
        # lista_nao_tratada = ['Python', 'é', 'uma', 'linguagem', 'de', 'programação', 'poderosa,', 'versátil', 'e', 'fácil,', 'de', 'aprender', 'utilizada', 'em', 'diversos', 'campos,', 'desde', 'análise', 'de', 'dados', 'até', 'inteligência', 'artificial!']

        lista = ['Python', 'é', 'uma', 'linguagem', 'de', 'programação', 'poderosa', 'versátil',
                    'e', 'fácil', 'de', 'aprender', 'utilizada', 'em', 'diversos', 'campos', 'desde',
                    'análise', 'de', 'dados', 'até', 'inteligência', 'artificial']

        pontuacao = list(',.!?')
        palavras_com_pontuacao = []

        for palavra in lista:
            for letra in palavra:
                if letra in pontuacao:
                    palavras_com_pontuacao.append(palavra)

        if len(palavras_com_pontuacao) != 0:
            raise ValueError(f'O texto apresenta pontuações na(s) palavra(s) "{palavras_com_pontuacao}"')
    except Exception as e:
        print(e)
    else:
        print('As palavas da lista não contém pontuação')

# Fazer a divisão entre duas listas
def exercicio_7():
    try: 
        pressoes = [100, 120, 140, 160, 180]
        temperaturas = [20, 25, 30, 35, 40]
        resultado = []

        if len(pressoes) != len(temperaturas):
            raise ValueError('O tamanho das listas de pressões e temperaturas precisam ser iguais')

        for i in range(len(pressoes)):
            resultado.append(round(pressoes[i]/temperaturas[i], 2))

    except ZeroDivisionError:
        print('Não é possível dividir por zero, verifique os valores inseridos')
    except ValueError as e:
        print(e)
    else:
        print(resultado)


        