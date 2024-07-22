
def verificar_palindromo():
    # variáveis
    string = input('Digite uma palavra ou frase: ') # string sem formatação
    string_inversa = '' # futuramente a string inversa
    string_formatada = string.replace(' ', '').lower() # string sem espaço e minuscula
    tamanho_palavra = len(string_formatada)
    index_letra = tamanho_palavra - 1 # posição da letra na string, usada para inversão

    # receber a palavra inversa
    while index_letra >= 0:
            string_inversa = string_inversa + string_formatada[index_letra]
            indx_letra -= 1

    # comparar a palavra inversa com a original, se verdadeiro, é um palindromo
    if string_formatada == string_inversa:
            print('É um palindromo')
    else:
            print('Não é um palindromo')

verificar_palindromo() #chamando a função




################ solução do chatgpt para a inversão da string:

# string_inversa = string_formatada[::-1]