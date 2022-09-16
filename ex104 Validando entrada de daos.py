def leiaint(txt):
    while True:
        print('-' * 45)
        n = str(input(txt))
        if n.isnumeric():
            print(f'Você acabou de digitar o número {n}')
            break
        else:
            print('ERRO! Digite um número inteiro válido.')


leiaint('Digite um número:')
