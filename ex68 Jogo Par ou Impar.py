from random import randint
print('=-' * 20)
print('VAMOS JOGAR PAR OU IMPAR')
print('=-' * 20)
jogador = None
cont = 0
while True:
    while jogador == None:
        try:
            jogador = int(input('Diga um valor: '))
        except:
            print('Digite um valor valido')
    jogada = str(input('Par ou impar? [P/I] ')).strip().upper()
    print('-' * 40)
    pc = randint(0, 10)
    tot = jogador + pc
    r = tot % 2
    cont = 0
    if r == 1:
        print(f'Voce jogou {jogador} e o Computador {pc}. Total de {tot} deu IMPAR')
    else:
        print(f'Voce jogou {jogador} e o Computador {pc}. Total de {tot} deu PAR')
    print('-' * 40)
    if jogada == 'I':
        if r == 1:
            print('''Voce VENCEU!
            Vamos jogar novamente...''')
            print('=-' * 20)
            cont += 1
        else:
            print('Voce Perdeu! ')
            print('=-' * 20)
            print(f'GAME OVER! Voce venceu {cont} vezes.')
            break
    if jogada == 'P':
        if r == 1:
            print('Voce Perdeu! ')
            print('=-' * 20)
            print(f'GAME OVER! Voce venceu {cont} vezes.')
            break
        else:
            print('''Voce VENCEU!
                        Vamos jogar novamente...''')
            print('=-' * 20)
            cont += 1
    jogador = None