import random
import time
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = random.choice(lista)
x = 0
cont = 0
while x !=y:
    x = int(input('Digite um número de 0 a 10: '))
    print('Processando...')
    time.sleep(1)
    print('Tente de novo!')
    cont = cont + 1
    if x == y:
        print('Você acertou! O computador escolheu {}. Fim de jogo'.format(y))
print('Foram necessárias {} tentativas para vencer'.format(cont))

