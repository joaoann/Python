def identificar_pares(lista):
    pares = []
    for numero in lista:
        if numero % 2 == 0:
            pares.append(numero)
    return print(pares)


numeros = [1,2,3,4,5,6,7,9,18,239,428,238124,1249123,1294]
identificar_pares(numeros)