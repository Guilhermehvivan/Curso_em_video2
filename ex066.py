soma = 0
cont = 0
while True:
    n = int(input('Digite um número:  '))
    if n == 999:
        break
    cont = cont + 1
    soma = soma + n
print('A soma entre esses {} números foi de {}'.format(cont,soma))

