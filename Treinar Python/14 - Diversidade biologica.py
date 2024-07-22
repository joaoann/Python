dados = {
        'Área Norte': [2819, 7236],
        'Área Leste': [1440, 9492],
        'Área Sul': [5969, 7496],
        'Área Oeste': [14446, 49688],
        'Área Centro': [22558, 45148]
        }

media_especies = {}
maior_area = ''
maior_area_especies = 0

for area, especies in dados.items():
    media_especies[area] = int(sum(especies)/len(especies))

for area, especies in media_especies.items():
    print(f'Na {area} há uma média de {especies} espécies.')
    if especies > maior_area_especies:
        maior_area_especies = especies
        maior_area = area

print(f'A maior área é a {maior_area}! Com uma média de {maior_area_especies} espécies')


