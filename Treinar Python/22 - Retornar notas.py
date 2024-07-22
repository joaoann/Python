notas = []

def solicitar_notas():
    x = 1
    while x <= 4:
        nota = float(input(f'Digite a {x}ª nota: '))
        notas.append(nota)
        x += 1

solicitar_notas()
nota_maior = max(notas)
nota_menor = min(notas)
media = sum(notas) / len(notas)
situacao = ''

if media >= 6:
    situacao = 'aprovado(a)'
else:
    situacao = 'reprovado(a)'

print(f'O(a) estudante obteve uma média de '+ '%.2f' % media + f', com a sua maior nota de {nota_maior} pontos e a menor nota de {nota_menor} pontos e foi {situacao}')