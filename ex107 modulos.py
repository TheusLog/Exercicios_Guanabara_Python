import uteis

p = float(input('Digite o preco: R$'))
print(f'A medade de {p} é {uteis.metade(p)}')
print(f'O dobro de {p} é {uteis.dobro(p)}')
print(f'Aumentando 10%, temos {uteis.aumentar(p, 10)}')
print(f'Reduzindo 13%, temos {uteis.diminuir(p, 13)}')