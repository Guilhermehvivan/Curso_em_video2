x = float(input('Digite sua altura em metros: '))
y = float(input('Digite seu peso em kg: '))
imc = y/(x**2)
print('Seu IMC é {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso ideal.')
elif 18.5 <= imc < 25:
    print('Você está com o peso ideal.')
elif 25 <= imc < 30:
    print('Você está com sobrepeso.')
elif 30 <= imc < 40:
    print('Você está com obesidade.')
else:
    print('Você está com obesidade mórbida.')