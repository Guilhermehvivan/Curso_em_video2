import random
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
aleatorio1 = random.choice(lista)
aleatorio2 = random.choice(lista)
aleatorio3 = random.choice(lista)
x = float(input('Digite um número:  '))
y = float(input('Digite outro número:  '))
print('''Escolha uma das opções abaixo:
[ 1 ] se quiser somar
[ 2 ] se quiser multiplicar
[ 3 ] se quiser saber qual é o maior
[ 4 ] se quiser novos números
[ 5 ] se quiser sair do programa''')
escolha = int(input('Digite sua escolha:  '))
while escolha != 5:
    if escolha == 1:
        print('O resultado da soma entre os números foi de {}'.format(x + y))
        escolha = int(input('Digite sua escolha:  '))
    elif escolha == 2:
        print('O resultado da multiplicação entre os números foi de {}'.format(x*y))
        escolha = int(input('Digite sua escolha:  '))
    elif escolha == 3:
        if x > y:
            print('{} é maior'.format(x))
            escolha = int(input('Digite sua escolha:  '))
        elif y > x:
            print('{} é maior'.format(y))
            escolha = int(input('Digite sua escolha:  '))
        else:
            print('São iguais')
            escolha = int(input('Digite sua escolha:  '))
    elif escolha == 4:
        print('O computador gerou os números {}, {} e {}'.format(aleatorio1, aleatorio2, aleatorio3))
        escolha = int(input('Digite sua escolha:  '))
print('O programa acabou')

