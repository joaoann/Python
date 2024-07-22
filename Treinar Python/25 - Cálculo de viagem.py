cidades = ['salvador', 'fortaleza', 'natal', 'aracaju']
lista_distancia = [850, 800, 300, 550]
lista_passeio_alimentacao = [200, 400, 250, 300]
diaria_hotel = 150

cidade_desejada = input('Para qual cidade você quer viajar?')
dias = int(input('Quantos dias você irá ficar?'))
distancia = 0
passeio_alimentacao = 0

i = 0
while i < len(cidades):
    if cidades[i] == cidade_desejada.lower():
        distancia = lista_distancia[i]
        passeio_alimentacao = lista_passeio_alimentacao[i]
    i += 1

gasto_hotel = dias * diaria_hotel
gasto_gasolina = int(distancia/14 * 5)
gasto_passeio = passeio_alimentacao * dias
gasto_total = gasto_hotel + gasto_gasolina + gasto_passeio

print(f'Com base nos gastos definidos, uma viagem de {dias} dias para {cidade_desejada.capitalize()} saindo de Recife custaria {gasto_total} reais')