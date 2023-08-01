cont1 = cont2 = cont3 = 0
while True:
    x = int(input('Digite sua idade:  '))
    y = str(input('Digite seu sexo [M/F]:  ')).upper().strip()
    print('-'*30)
    continuar = str(input('Quer continuar?[S/N]  ')).upper().strip()
    print('-' * 30)
    if continuar == 'S':
        if x > 18:
            cont1 = cont1 + 1
        elif y == 'M':
            cont2 = cont2 + 1
        elif y == 'F' and x < 20:
            cont3 = cont3 + 1
    if continuar == 'N':
        print('Acabou!')
        break
print('Foram {} pessoas com mais de 18 anos, {} homens e {} mulheres com menos de 20 anos'.format(cont1, cont2, cont3))


