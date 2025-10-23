l=float(input('Digite a largura em metros da sua parede: '))
a=float(input('Digite a altura em metros de sua parede: '))
mq=l*a
t=mq/2
print('Sua parede tem {} metros quadrados, e para pintar, você precisa de {} litros de tinta'.format(mq, t))