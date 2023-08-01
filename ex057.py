sexo = str(input('Qual é o seu sexo? [M/F]  ')).upper().strip()[0]
while sexo not in 'MF':
    sexo = str(input('Dado inválido. Digite corretamente:  '))
print('Sexo {} registrado'.format(sexo))




