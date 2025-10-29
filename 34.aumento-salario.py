sal=float(input('Digite seu salário: '))
if sal>1250:
    print('Seu novo salário é R${:.2f}'.format(sal+(sal*10/100)))
else:
    print('Seu novo salário é R${:.2f}'.format(sal+(sal*15/100)))