while True:
    n = int(input('Digite um número inteiro de 0 a 10 para saber a sua tabuada:  '))
    if n < 0:
        break
    print('--'*20)
    for c in range(0, 11):
        print(c, end='')
        print(' x  ', end='')
        print(n, end='')
        print(' = ', end='')
        print(c*n)
    print('--'*20)
print('Acabou!')