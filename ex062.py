a1 = int(input('Digite o primeiro termo da progressão aritmética:  '))
r = int(input('Digite a razão da progressão aritmética: '))
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(a1, end=' ')
        a1 = a1 + r
        cont = cont + 1
    mais = int(input('\nQuantos termos você quer ver a mais?'  ))
print('\nFim')