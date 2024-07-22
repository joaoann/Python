vendas = {'Produto A': 300,
          'Produto B': 80,
          'Produto C': 60,
          'Produto D': 200,
          'Produto E': 250,
          'Produto F': 30}
total_vendas = 0
mais_vendido = ''

for produto, valor in vendas.items():
    total_vendas = total_vendas + valor

maior_valor = 0
for produto, valor in vendas.items():
    if valor > maior_valor:
        mais_vendido = produto
        maior_valor = valor

print(f'O total de vendas é {total_vendas} unidades')
print(f'O produto mais vendido é o {mais_vendido}, com uma venda de {vendas[mais_vendido]} unidades')
