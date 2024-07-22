
# Tabela de votos da marca
# Design 1 - 1334 votos
# Design 2 - 982 votos
# Design 3 - 1751 votos
# Design 4 - 210 votos
# Design 5 - 1811 votos

desings_e_votos = {}

numero_desing = 1
votos = 0

while votos != 's':

    votos = input(f'Digite o número de votos para o Design {numero_desing} (Digite s para parar): ')

    if votos.lower() != 's':
        desings_e_votos[f'Design {numero_desing}'] = int(votos)
        numero_desing += 1

total_votos = 0
for design, nota in desings_e_votos.items():
    total_votos = total_votos + nota

maior_voto = 0
design_mais_votado = ''
for design, nota in desings_e_votos.items():
    if nota > maior_voto:
        maior_voto = nota
        design_mais_votado = design

porcentagem = int(maior_voto/total_votos * 100)

print(f'O {design_mais_votado} é o design vencedor com {porcentagem}% do total de votos!')
