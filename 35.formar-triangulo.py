c1=float(input('Digite o comprimento um: '))
c2=float(input('Digite o comprimento dois: '))
c3=float(input('Digite o comprimento três: '))
if (c1+c2)>c3 and (c2+c3)>c1:
    print('Os comprimentos formam um triângulo')
else:
    print('Os comprimentos não formam um triângulo')