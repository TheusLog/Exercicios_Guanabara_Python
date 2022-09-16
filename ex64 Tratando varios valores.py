n = 0
cont = 0
tot = 0
while n != 999:
    n = int(input('Digite um numero [999 para parar]: '))
    if n != 999:
        cont += n
        tot += 1
print('Voce digitou {} e a soma entre eles foi {}'.format(tot, cont))
