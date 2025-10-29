velo=float(input('Qual a velocidade do carro: '))
if velo>80:
    print('Você levou uma multa de R${:.2f}'.format((velo-80)*7))
else:
    print('Ok, velocidade permitida')