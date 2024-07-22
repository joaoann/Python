# Escolhe um número da lista
def numero_aleatorio_lista():
    from random import choice

    lista = [8, 12, 54, 23, 43, 1, 90, 87, 105, 77]

    print(choice(lista))

# Escolhe um número aleatorio até 100
def numero_aleatorio_ate_100():
    from random import randrange

    print(randrange(100))

# Calcula a potência de um número elevado a outro
def calcular_potencia():
    from math import pow

    primeiro_numero = int(input('Digite um número: '))
    segundo_numero = int(input('Digite outro número: '))

    potencia = pow(primeiro_numero, segundo_numero)

    print(f'{primeiro_numero} elevado a {segundo_numero} é igual a {potencia}')

# Devolver um número aleatório máximo que o usuário digita
def numero_participante():
    from random import randrange

    numero = int(input('Digite um número: '))

    participante = randrange(1, numero + 1)

    print(f'O ganhador é o parcitipante número {participante}!')

# Criando um token para um usuário
def token_de_acesso():
    from random import randrange

    nome = input('Digite o seu nome: ')
    token = randrange(1000, 9999)
    print(f'Olá, {nome}, o seu token de acesso é {token}! Seja bem-vindo(a)!')

# Selecionando frutas aleatórias para salada de frutas
def salada_misteriosa():
    from random import choices

    frutas = ["maçã", "banana", "uva", "pêra", 
            "manga", "coco", "melancia", "mamão",
            "laranja", "abacaxi", "kiwi", "ameixa"]

    salada = choices(frutas, k=3)

    print(salada)

# Calcular a raiz e retornar as inteiras
def verificar_raiz_inteira():

    from math import sqrt

    numeros = [2, 8, 16, 23, 91, 112, 256]
    raizes_inteiras = {}
    for i in numeros:
        if sqrt(i) % 2 == 0:
            raizes_inteiras[int(i)] = int(sqrt(i))

    print('As raizes inteiras na lista são:')
    for numero, raiz in raizes_inteiras.items():
        print(f'Raiz de {numero} que é igual a {raiz}')

# Calcular o preço de uma área circular (25 reais o m²)
def calcular_preco_area_circular():
    from math import pow, pi

    raio = int(input('Digite o raio do circulo em metros: '))
    area = pi * pow(raio, 2)
    valor_area = 25 * area

    print('O preço é de R$ ' + '%0.2f' % valor_area)
