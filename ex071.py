print('-'*30)
print('Caixa eletrônico')
print('-'*30)
valor = int(input('Digite o valor que você deseja sacar: R$  '))
if valor % 50 == 0:
    print('Total de {:.0f} cédulas de R$50'.format(valor/50))
elif (valor % 50) % 20 == 0:
    print('Total de {:.0f} cédulas de R$50'.format(valor // 50))
    print('Total de {:.0f} cédulas de R$20'.format((valor % 50) // 20))
elif ((valor % 50) % 20) % 10 == 0:
    print('Total de {:.0f} cédulas de R$50'.format(valor // 50))
    print('Total de {:.0f} cédulas de R$20'.format((valor % 50) // 20))
    print('Total de {:.0f} cédulas de R$10'.format(((valor % 50) % 20) // 10))
elif (((valor % 50) % 20) % 10) % 1 == 0:
    print('Total de {:.0f} cédulas de R$50'.format(valor // 50))
    print('Total de {:.0f} cédulas de R$20'.format((valor % 50) // 20))
    print('Total de {:.0f} cédulas de R$10'.format(((valor % 50) % 20) // 10))
    print('Total de {:.0f} cédulas de R$1'.format((((valor % 50) % 20) % 10) // 1))
print('Fim')