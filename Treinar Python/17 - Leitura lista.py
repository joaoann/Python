lista = [16, 14, 63, 65, 17, 99, 70, 11, 20, 48, 79, 32, 17, 89, 12, 25, 66]

tamanho_lista = len(lista)
maior_valor = 0
somatoria = sum(lista)

for i in lista:
    if i > maior_valor:
        maior_valor = i

menor_valor = maior_valor
for i in lista:
    if i < menor_valor:
        menor_valor = i

print(f'O tamanho da lista é {tamanho_lista} / A somatória dos valoes é {somatoria} / O menor valor é {menor_valor} / O maior valor é {maior_valor}')