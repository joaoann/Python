frase = input('Digite sua frase: ')
pontuacao = '!.,?-@()}{[]'
for i in pontuacao:
    frase = frase.replace(i, '')
    
lista_palavras = []
frase_separada = frase.split()

for palavra in frase_separada:
    if len(palavra) >= 5:
        lista_palavras.append(palavra)

print(lista_palavras)



# ## Solução professor

# # Requisitando uma frase e separando-a pelos espaços. Usando replace para trocar
# # pontuações por espaço.
# frase = input("Digite uma frase: ")
# frase = frase.replace(',',' ').replace('.',' ').replace('!',' ').replace('?',' ').split()

# # Filtrando a frase no formato de lista, passando para a lista tamanho
# # apenas as palavras com 5 ou mais caracteres e imprimindo-a na tela
# tamanho = list(filter(lambda x: len(x) >= 5, frase))
# print(tamanho)

