frase=str(input('Digite uma frase: ')).strip().upper()
print('A letra A aparece {} vez(es) na frase'.format(frase.count('A')))
print('A letra A apareceu a primeira vez na posição {}'.format(frase.find('A')+1))
print('A letra A apareceu a última vez na posição {}'.format(frase.rfind('A')))


