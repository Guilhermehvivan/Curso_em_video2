from datetime import date
x = int(input('Digite o seu ano de nascimento:  '))
if date.today().year-x<18:
    print('Você ainda precisa se alistar nos próximos anos')
    y = 18-(date.today().year-x)
    print('Faltam {} anos para o seu alistamento'.format(y))
elif date.today().year-x == 18:
    print('Você precisa se alistar neste ano')
else:
    print('Você já passou do tempo de se alistar')
    z = (date.today().year-x)-18
    print('Já se passaram {} anos da data do seu alistamento'.format(z))

