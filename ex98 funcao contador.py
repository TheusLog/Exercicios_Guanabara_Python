from time import sleep


def contador(i, f, p):
    print(f'Contagem de {i} ate o {f} de {p} em {p}')

    if p < 0:
        p *= -1
    if p == 0:
        p = 1


    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont += p
        print('Fim!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont -= p
        print('Fim!')



contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua fez de me falar a contagem')
ini = int(input('Inincio: '))
fim = int(input('Fim: '))
pas = int(input('passo: '))
contador(ini, fim, pas)