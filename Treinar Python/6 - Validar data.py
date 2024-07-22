
def verificar_data(dia, mes, ano):
    if mes == 2:

        dia_maximo = 0
        if (ano % 4 == 0) and (ano % 400 == 0 or ano % 100 != 0):
            dia_maximo = 29
        else:
            dia_maximo = 28

        if dia >= 1 and dia <= dia_maximo:
            print(f'A data {dia}/{mes}/{ano} é válida!')
        else:
            print(f'A data {dia}/{mes}/{ano} é inválida.')

    elif mes in [1, 3, 5, 7, 8, 10, 12]:

        if dia >= 1 and dia <= 31:
            print(f'A data {dia}/{mes}/{ano} é válida!')
        else:
            print(f'A data {dia}/{mes}/{ano} é inválida.')

    elif mes in [2, 4, 6, 9, 11]:
        if dia >= 1 and dia <= 30:
            print(f'A data {dia}/{mes}/{ano} é válida!')
        else:
            print(f'A data {dia}/{mes}/{ano} é inválida.')
    else:
        print(f'A data {dia}/{mes}/{ano} é inválida.')


dia_usuario = int(input('Digite o dia: '))
mes_usuario = int(input('Digite o mês: '))
ano_usuario = int(input('Digite o ano no formato AAAA: '))

verificar_data(dia_usuario, mes_usuario, ano_usuario)