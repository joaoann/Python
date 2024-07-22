salarios = [1172, 1644, 2617, 5130, 5532, 6341, 6650, 7238, 7685, 7782, 7903]
salarios_com_abono = {}
total_do_abono = 0
funcionarios_abono_minimo = 0

for i in range(0, len(salarios)):
    if salarios[i] * 0.1 < 200:
        salarios_com_abono[salarios[i]] = salarios[i] + 200
        total_do_abono = total_do_abono = 200
        funcionarios_abono_minimo = funcionarios_abono_minimo + 1
    else:
        salarios_com_abono[salarios[i]] = salarios[i] * 1.1
        total_do_abono = total_do_abono + salarios[i] * 0.1

maior_abono = 0
for salario_normal, salario_abonado in salarios_com_abono.items():
    if salario_abonado - salario_normal > maior_abono:
        maior_abono = salario_abonado - salario_normal

print('> O total de gastos com abono é de: R$ ' + '%0.2f' % total_do_abono)
print(f'> {funcionarios_abono_minimo} funcionários receberam o abono mínimo')
print('> R$ ' + '%0.2f' % maior_abono + ' é o maior abono')