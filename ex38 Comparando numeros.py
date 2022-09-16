n1 = int(input('Digite um numero inteiro: '))
n2 = int(input('Digiti outro numero inteiro: '))
if n1 < n2:
    print('{} é maior!'.format(n2))
elif n1 > n2:
    print('{} é maior!'.format(n1))
elif n1 == n2:
    print('Os dois sao iguais')
else:
    print('Informacao incorreta.')