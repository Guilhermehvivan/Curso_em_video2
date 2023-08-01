a1 = int(input('Digite o primeiro termo da progressão aritmética:  '))
r = int(input('Digite a razão da progressão aritmética: '))
cont = 0
while cont < 10:
    print(a1, end=' ')
    a1 = a1 + r
    cont = cont + 1
print('\nFim')