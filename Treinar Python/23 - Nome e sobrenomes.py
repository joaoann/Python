nomes = ["joão", "MaRia", "JOSÉ"]
sobrenomes = ["SILVA", "souza", "Tavares"]

nomes_formatado = []
sobrenomes_formatado = []

for i in nomes:
    nomes_formatado.append(i.capitalize())

for i in sobrenomes:
    sobrenomes_formatado.append(i.capitalize())

nomes_completos = []
i = 0
while i < len(nomes):
    nomes_completos.append(nomes_formatado[i] + ' ' + sobrenomes_formatado[i])
    i += 1

print(nomes_completos)
    

## Solução professor

# # Nomes dos estudantes
# nomes = ["joão", "MaRia", "JOSÉ"]
# sobrenomes = ["SILVA", "souza", "Tavares"]

# # Função lambda que recebe duas listas e itera em cada uma concatenando seu nome e sobrenome
# # na forma desejada
# nome_completo = map(lambda nome, sobrenome: f'{nome.title()} {sobrenome.title()}', nomes, sobrenomes)

# # Leitura do objeto mapa(iterável)
# for n in nome_completo:
#   print(f'Nome completo: {n}')