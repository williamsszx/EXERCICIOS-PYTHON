import random
from time import sleep
print('='*50)
print('Estou pensando em um número de 0 a 5.......')
print('='*50)
sleep(3)
escolhido=random.randint(0, 5)
número=int(input('Pensei, agora tente adivinhar em que número eu pensei: '))
print('='*50)
print('Processando.......')
print('='*50)
sleep(3)
if número==escolhido:
    print('Parabéns, você me venceu!, eu realmente pensei no número {}'.format(número))
else:
    print('Você perdeu!, eu pensei no número {}'.format(escolhido))
