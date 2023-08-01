import random
cont = 0
while True:
    computador = random.randint(0,5)
    print('='*30)
    print('Par ou Ímpar')
    print('='*30)
    jogador = int(input('Escolha um número de 0 a 5:  '))
    parimpar = str(input('Escolha Par ou Ímpar [P/I]:  ')).upper().strip()
    print('O computador escolheu {}'.format(computador))
    total = jogador + computador
    if total%2 == 0 and parimpar == 'P' or total%2 != 0 and parimpar == 'I':
        print('Você venceu!')
        cont = cont + 1
    else:
        print('Você perdeu!')
        break
print('Você venceu {} vezes'.format(cont))




