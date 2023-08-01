x = float(input('Digite sua nota: '))
y = float(input('Digite sua segunda nota: '))
m = (x+y)/2
if m<5:
    print('Você foi reprovado!!Estude mais')
elif 5<=m<7:
    print('Você ficou de recuperação!')
else:
    print('Parabéns!Você foi aprovado!')
