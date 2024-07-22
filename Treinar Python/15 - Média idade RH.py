idades_rh = {
        'Setor A': [22, 26, 30, 30, 35, 38, 40, 56, 57, 65],
        'Setor B': [22, 24, 26, 33, 41, 49, 50, 54, 60, 64],
        'Setor C': [23, 26, 26, 29, 34, 35, 36, 41, 52, 56],
        'Setor D': [19, 20, 25, 27, 34, 39, 42, 44, 50, 65]
        }

media_idade_setor = {}
media_geral = 0
qtde_pessoas_acima_media = 0

for setor, idade in idades_rh.items():
    media_idade_setor[setor] = int(sum(idade) / len(idade))

media_geral = int(sum(media_idade_setor.values()) / len(media_idade_setor.values()))

for setor, idade in idades_rh.items():
    for i in idade:
        if i > media_geral:
            qtde_pessoas_acima_media += 1
        
for setor, idade in media_idade_setor.items():
    print(f'> A média de idade do {setor} é {idade} anos.')
print('---------')
print(f'> A média de idade entre todos os setores é de {media_geral} anos.')
print('---------')
print(f'> Atualmente {qtde_pessoas_acima_media} pessoas estão acima da média geral.')