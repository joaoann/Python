temperaturas = [26.7, 28.2, 30, 31.5, 27.9, 26.8, 27, 24.5, 22.6, 21, 24.3, 27]
media_anual = sum(temperaturas)/12

meses = dict(Janeiro=temperaturas[0],
             Fevereiro=temperaturas[1],
             Marco=temperaturas[2],
             Abril=temperaturas[3],
             Maio=temperaturas[4],
             Junho=temperaturas[5],
             Julho=temperaturas[6],
             Agosto=temperaturas[7],
             Setembro=temperaturas[8],
             Outubro=temperaturas[9],
             Novembro=temperaturas[10],
             Dezembro=temperaturas[11])
meses_maior_media = {}

def verificar_media_mes():
        
    if meses['Janeiro'] > media_anual:
            meses_maior_media['Janeiro'] = meses['Janeiro']

    if meses['Fevereiro'] > media_anual:
            meses_maior_media['Fevereiro'] = meses['Fevereiro']

    if meses['Marco'] > media_anual:
            meses_maior_media['Marco'] = meses['Marco']

    if meses['Abril'] > media_anual:
            meses_maior_media['Abril'] = meses['Abril']

    if meses['Maio'] > media_anual:
            meses_maior_media['Maio'] = meses['Maio']

    if meses['Junho'] > media_anual:
            meses_maior_media['Junho'] = meses['Junho']

    if meses['Julho'] > media_anual:
            meses_maior_media['Julho'] = meses['Julho']

    if meses['Agosto'] > media_anual:
            meses_maior_media['Agosto'] = meses['Agosto']

    if meses['Setembro'] > media_anual:
            meses_maior_media['Setembro'] = meses['Setembro']

    if meses['Outubro'] > media_anual:
            meses_maior_media['Outubro'] = meses['Outubro']

    if meses['Novembro'] > media_anual:
            meses_maior_media['Novembro'] = meses['Novembro']

    if meses['Dezembro'] > media_anual:
            meses_maior_media['Dezembro'] = meses['Dezembro']

verificar_media_mes()
print('A temperatura média anual é ' + '%.1f' % media_anual + '°C')
for mes, temperatura in meses_maior_media.items():
    print(f'No mês de {mes} a temperatura média foi {temperatura}°C')







###### Solução professor

# # Coletamos a lista de temperaturas
# temperaturas_mensais = []
# for i in range(0,12):
#   temperaturas_mensais.append(float(input(f'Digite a média de temperatura do mês {i+1}: ')))
# # Criamos uma lista auxiliar para os nomes dos meses
# meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
# # Calculamos a média
# media_anual = sum(temperaturas_mensais) / len(temperaturas_mensais)

# #Resultado
# print('Temperaturas acima da média em: ')
# for i in range(0,12):
#   # Verificamos todas as temperaturas de acordo com a média anual
#   if temperaturas_mensais[i] > media_anual:
#     # Como os índices dos meses correspondem às temperaturas,
#     # podemos imprimir eles sob o mesmo índice
#     print(f'No mês de {meses[i]} a temperatura foi {temperaturas_mensais[i]}')