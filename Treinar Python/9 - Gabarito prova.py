
def calcular_nota(gabarito):

    gabarito_resposta = gabarito.upper().split()
    nota = 0
    questao = 1

    for letra in gabarito_resposta:

        resposta = input('Resposta da questão ' + str(questao) + ': ')

        if resposta.upper() == letra:
            nota += 1
            questao += 1
            print('Correto!')
        else:
            questao += 1
            print(f'Incorreto. Resposta certa: {letra}')
    
    return print(f'Nota final: {nota}')


gabarito = 'd a c b a d c c a b'
calcular_nota(gabarito)
