def separacao_produtos(lista):

    amargos = []
    doces = []

    for id in produtos:

        if id % 2 == 0:
            doces.append(id)
        else:
            amargos.append(id)

    qtde_doces = len(doces)
    qtde_amargos = len(amargos)

    return print(f'Há {qtde_doces} produtos doces e {qtde_amargos} produtos amargos')


produtos = [1, 29, 290, 43, 89, 44, 45, 1239]
separacao_produtos(produtos)