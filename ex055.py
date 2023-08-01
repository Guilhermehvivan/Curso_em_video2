lista = []
for i in range(0,5):
    peso = float(input('Peso da pessoa {}:  '.format(i+1)))
    lista.append(peso)
maiorPeso = max(lista)
menorPeso = min(lista)
print('O maior peso é {} e o menor é {}'.format(maiorPeso, menorPeso))



