soma = cont1 = cont2 = menor = 0
barato = ''
print('-'*30)
print('Loja')
print('-'*30)
while True:
    nome = str(input('Digite o nome do produto:  ')).strip()
    preco = float(input('Digite o preço do produto:  R$'))
    continuar = str(input('Quer continuar?[S/N]  ')).upper().strip()
    cont2 = cont2 + 1
    soma = soma + preco
    if preco > 1000:
        cont1 = cont1 + 1
    if cont2 == 1:
        menor = preco
        barato = nome
    else:
        if preco < menor:
            menor = preco
            barato = nome
    if continuar == 'N':
        print('Acabou')
        break
print('O preço total é de {}, {} produtos custaram acima de R$1000 e {} tem o menor preço, {}'.format(soma, cont1, barato, menor))



