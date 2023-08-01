import datetime
m = datetime.date.today().year
ma = 0
me = 0
for c in range(1,8):
    n = int(input('Qual é o ano de nascimento da pessoa {}?  '.format(c)))
    if m - n >= 21:
        ma = ma + 1
    else:
        me = me + 1
print('{} atingiram a maioridade'.format(ma))
print('{} ainda não atingiram a maioridade'.format(me))

