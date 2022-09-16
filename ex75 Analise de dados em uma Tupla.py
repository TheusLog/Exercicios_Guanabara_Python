num = (int(input('Digite um valor: ')),
       int(input('Digite outro valor: ')),
       int(input('Digite mais um valor: ')),
       int(input('Digite o ultimo valor: ')))
print(f'Voce digitou os valors {num}')
print(f'O valor 9 apareceu {num.count(9)}')
if 3 in num:
    print(f'o valor 3 apareceu na {num.index(3)+1} posisao')
else:
    print('O valor 3 nao foi digitado em nenhuma posisao')
print('Os valores pares digitados foram', end=' ')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
