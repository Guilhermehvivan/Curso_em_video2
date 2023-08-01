x = int(input('Digite um número inteiro: '))
y = int(input('Digite outro número inteiro: '))
if x>y:
    print('{} é o maior e {} é o menor'.format(x,y))
elif x<y:
    print('{} é o maior e {} é o menor'.format(y, x))
else:
    print('São dois números iguais')
