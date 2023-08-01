x = float(input('Digite o tamanho do primeiro segmento:  '))
y = float(input('Digite o tamanho do segundo segmento:  '))
z = float(input('Digite o tamanho do terceiro segmento:  '))
if x == y == z:
    print('\033[34mVocê formou um triângulo equilátero!\033[m')
elif x != y and x != z and y != z:
    print('\033[34mVocê formou um triângulo escaleno!\033[m')
elif x == y and x != z or x == z and x != y or y == z and y != x:
    print('\033[34mVocê formou um triângulo isósceles!\033[m')
else:
    print('\033[1;31mVocê não formou um triângulo\033[m')