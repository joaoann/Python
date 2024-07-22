gols_marcados = [2, 1, 3, 1, 0]
gols_sofridos = [1, 2, 2, 1, 3]

def calcula_pontos(marcados, sofridos):

    vitorias = 0
    empates = 0
    derrotas = 0

    i = 0
    while i < len(marcados):
        resultado = marcados[i] - sofridos[i]
        if resultado > 0:
            vitorias += 1
        elif resultado < 0:
            derrotas += 1
        else:
            empates += 1
        i += 1

    pontuacao_maxima = len(marcados) * 3
    pontuacao_final = vitorias * 3 + empates
    aproveitamento = (pontuacao_final / pontuacao_maxima) * 100

    return pontuacao_final, aproveitamento

pontuacao_final, aproveitamento = calcula_pontos(gols_marcados, gols_sofridos)
print(f'A pontuação do time foi de {pontuacao_final} e seu aproveitamento foi de ' + '%.2f' % aproveitamento + '%')

