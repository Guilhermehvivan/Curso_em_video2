from datetime import date
x = int(input('Digite seu ano de nascimento:  '))
if date.today().year-x<9:
    print('Você está na categoria mirim')
elif 9<=date.today().year-x<14:
    print('Você está na categoria infantil')
elif 14<=date.today().year-x<19:
    print('Você está na categoria junior')
elif 19<=date.today().year-x<20:
    print('Você está na categoria sênior')
else:
    print('Você está na categoria master')