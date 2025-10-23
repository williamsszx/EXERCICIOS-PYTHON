km=float(input('Por quantos Km o carro percorreu?:  '))
dias=int(input('Por quantos dias o carro foi alugado: '))
pago=dias*60 + km*0.15
print('Valor a pagar: {:.2f}'.format(pago))