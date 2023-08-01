n = 0
soma = 0
cont = 0
while n != 999:
    n = int(input('Digite um número:  '))
    if n != 999:
        cont = cont + 1
        soma = soma + n
print('Foram {} números e a soma entre eles é de {}'.format(cont, soma))
print('Fim')