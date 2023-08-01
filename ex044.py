x = float(input('Qual é o preço das compras?  '))
print('''Escolha uma das formas de pagamento
[ 1 ] para pagar à vista com dinheiro/cheque, tendo 10% de desconto
[ 2 ] para pagar à vista com cartão, tendo 5% de desconto
[ 3 ] para pagar em até 2x no cartão, mantendo o preço
[ 4 ] para pagar em 3x ou mais no cartão, tendo 20% de juros''')
o = int(input('Digite sua opção:  '))
if o == 1:
    um = x-x*10/100
    print('O preço final a pagar será R${:.2f}'.format(um))
elif o == 2:
    dois = x-(x*5/100)
    print('O preço final a pagar será R${:.2f}'.format(dois))
elif o == 3:
    tres = x/2
    print('O preço final a pagar será de duas parcelas de R${:.2f}, totalizando {:.2f}'.format(tres, x))
elif o == 4:
    y = int(input('Serão quantas parcelas?  '))
    if y >= 3:
        quatro = x + (x * 20 / 100)
        print('O preço a pagar será de {} parcelas de R${:.2f}, totalizando {:.2f}'.format(y, quatro/y, quatro))
    if y < 3:
        print('Essa opção não é válida')
else:
    print('Digite uma opção válida')