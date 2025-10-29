dis=float(input('Digite a distância da viagem: '))
if dis<=200:
    print('O custo de sua viagem será {}'.format(dis*0.50))
else:
    print('O custo de sua viagem será {:.2f}'.format(dis*0.45))