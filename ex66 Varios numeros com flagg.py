cont = tot = 0
while True:
    n = None
    while n == None:
        try:
            n = int(input('Digite um numero [999 para parar]: '))
        except:
            print('Digite um número válido')
    if n == 999:
        break
    cont += n
    tot += 1
print(f'Voce digitou {tot} e a soma entre eles foi {cont}')