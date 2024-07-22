notas = []
x = 1

while x <= 5:
    nota = float(input(f'Digite a nota {x}: '))
    notas.append(nota)
    x += 1

nota_maxima = max(notas)
nota_minima = min(notas)

notas.pop(notas.index(nota_maxima))
notas.pop(notas.index(nota_minima))

media = sum(notas) / len(notas)
print(f'Nota da manobra: {media}')