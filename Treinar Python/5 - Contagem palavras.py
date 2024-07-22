
def contagem_palavras(frase):

    frase = frase.lower()
    pontuacao = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for caractere in pontuacao:
        frase = frase.replace(caractere, "")

    frase_separada = frase.split()

    contagem = {}

    for palavra in frase_separada:
        if palavra in contagem:
            contagem[palavra] =+ 1
        else:
            contagem[palavra] = 1

    return contagem

frase_usuario = input('Digite uma frase: ')
resultado = contagem_palavras(frase_usuario)

for palavra, quantidade in resultado.items():
    print(f'{palavra}: {quantidade}')