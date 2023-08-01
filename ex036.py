x = float(input('Quanto a casa custa?  '))
y = float(input('Qual é o seu salário?  '))
z = int(input('Em quantos anos você pretende pagar?  '))
print('O valor da prestação mensal será de R${:.2f}'.format(x/(z*12)))
if x/(z*12)>y*30/100:
    print('Infelizmente não será possível fazer o empréstimo!')
else:
    print('Parabéns! Seu empréstimo foi aprovado!')

