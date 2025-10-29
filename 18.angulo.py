import math
a=float(input('Digite o ângulo: '))
ar=math.radians(a)
seno=math.sin(ar)
cosseno=math.cos(ar)
tangente=math.tan(ar)
print('Seno: {:.2f} \nCosseno: {:.2f} \nTangente: {:.2f}'.format(seno, cosseno, tangente))
