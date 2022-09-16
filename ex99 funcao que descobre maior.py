from time import sleep


def Maior(*num):
    print('=-' * 30)
    print('Analisando os valores passado...')
    cont = maior = 0
    for valor in num:
        print(f'{valor} ', end='')
        sleep(0.5)
        cont += 1

        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor

    print(f'Foram informados {cont} valores.')
    print(f'O maior valor informado foi {maior}')


Maior(2, 5, 9, 4, 13, 11)
Maior(7, 4, 6, 9, )
Maior(7)
Maior(8, 9, 10, 103)
