somaidade = 0
media = 0
nomevelho = ''
maioridadehomem = 0
mulher20 = 0
for x in range(0, 4):
    print('PESSOA {}'.format(x+1))
    s = str(input('Qual é o seu sexo? [M/F]  ')).strip()
    i = int(input('Qual é a sua idade?  '))
    n = str(input('Qual é o seu nome?  ')).strip()
    somaidade += i
    if x == 1 and s in 'Mm':
        maioridadehomem = i
        nomevelho = n
    if s in 'Mm' and i > maioridadehomem:
        maioridadehomem = i
        nomevelho = n
    if s in 'Ff' and i < 20:
        mulher20 += 1
media = somaidade/4
print('A média de idade do grupo é {}'.format(media))
print('São {} mulheres com menos de 20'.format(mulher20))
print('O homem mais velho se chama {}'.format(nomevelho))





