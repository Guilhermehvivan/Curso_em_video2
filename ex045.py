import random
import time
itens = ('Pedra', 'Papel', 'Tesoura')
computador = random.randint(0,2)
print('=-'*20)
print('JOKENPÔ')
print('=-'*20)
print('''Escolha uma das opções abaixo:
[ 0 ] para PEDRA
[ 1 ] para PAPEL
[ 2 ] para TESOURA''')
jogador = int(input('Digite um dos números acima:  '))
print('O computador escolheu {}'.format(itens[computador]))
print('O jogador escolheu {}'.format(itens[jogador]))
print('PROCESSANDO...')
time.sleep(2)
if computador == jogador:
    print('Empate...')
elif computador == 0 and jogador == 2:
    print('Você perdeu!!')
elif computador == 0 and jogador == 1:
    print('Parabéns!Você venceu!')
elif computador == 1 and jogador == 0:
    print('Você perdeu!!')
elif computador == 1 and jogador == 2:
    print('Parabéns!Você venceu!')
elif computador == 2 and jogador == 0:
    print('Parabéns!Você venceu!')
elif computador == 2 and jogador == 1:
    print('Você perdeu!!')
else:
    print('Digite uma opção válida.')