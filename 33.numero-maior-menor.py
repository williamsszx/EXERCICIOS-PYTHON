n1=int(input('Digite o número um: '))
n2=int(input('Digite o número dois: '))
n3=int(input('Digite o número três: '))
if n1>n2 and n1>n3:
    print('O número um é o maior')
elif n2>n1 and n2>n3:
    print('O número dois é o maior')
else:
    print('O número três é o maior')
if n1<n2 and n1<n3:
    print('O número um é o menor')
elif n2<n1 and n2<n3:
    print('O número dois é o menor')
else:
    print('O número três é o menor')