x = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases de conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
o = int(input('Digite sua escolha: '))
if o == 1:
    print('{} convertido para binário é {}'.format(x,bin(x)[2:]))
elif o == 2:
    print('{} convertido para octal é {}'.format(x, oct(x)[2:]))
elif o == 3:
    print('{} convertido para hexadecimal é {}'.format(x, hex(x)[2:]))
else:
    print('Tente novamente!')
