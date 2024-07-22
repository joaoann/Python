# Retorna somente a primeira maior palavra

# def maior_palavra(lista):

#    palavra_mais_longa = ''

#    for palavra in lista:

#        if len(palavra) > len(palavra_mais_longa):
#            palavra_mais_longa = palavra
    
#    print(palavra_mais_longa)


#listagem_palavras = ['ana', 'lixo', 'casa']
#maior_palavra(listagem_palavras)




# Retorna um array com todas as palavras longas (mais refinado)


def maior_palavra(listagem):

    comprimento_max = 0
    maiores_palavras = ['']

    for palavra in listagem:

        comprimento = len(palavra)

        if comprimento > comprimento_max:
            maiores_palavras = [palavra]
            comprimento_max = comprimento
        elif comprimento == comprimento_max:
            maiores_palavras.append(palavra)
    
    print(maiores_palavras)

lista = ['maca', 'bueiro', 'beijo']
maior_palavra(lista)