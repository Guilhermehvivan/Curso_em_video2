soma1 = 0
cont = 0
maior = 0
menor = 0
continuar = 'S'
while continuar == 'S':
    n = int(input('Digite um número:  '))
    continuar = str(input('Quer continuar?[S/N]  ')).upper().strip()
    cont = cont + 1
    soma1 = soma1 + n
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
print('A média entre esses {} números foi de {}'.format(cont,soma1/cont))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))

