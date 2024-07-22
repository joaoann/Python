def tabuada(valor):

    x = 0
    print(f'Tabuada do {valor}:')
    while x <= 10:
        print(f'{valor} x {x} = {valor * x}')
        x += 1

numero = int(input('Digite um número para receber sua tabuada: '))

tabuada(numero)