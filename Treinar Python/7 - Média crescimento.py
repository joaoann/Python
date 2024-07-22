bacterias = [1.2, 2.1, 3.3, 5.0, 7.8, 11.3, 16.6, 25.1, 37.8, 56.9]
total_dias = len(bacterias)
dia = 0
crescimento = []

while dia < total_dias:

    amostra_atual = bacterias[dia]
    amostra_anterior = bacterias[dia - 1]

    if dia != 0:
        porcetagem = 100 * (amostra_atual - amostra_anterior) / amostra_anterior
        crescimento.append(porcetagem)
        dia += 1
    else:
        dia += 1

print(crescimento)
dia = 0
while dia < total_dias:

    if dia != 0:
        print(f'O crescimento do dia {dia - 1} para o {dia} foi de ' + "%.0f" % crescimento[dia - 1] + "%")
        dia += 1
    else:
        dia += 1



        