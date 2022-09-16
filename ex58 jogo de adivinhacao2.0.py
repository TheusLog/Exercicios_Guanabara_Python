from random import randint
pc = randint(0, 10)
jogador = int(input('Digite um numero de 0 a 10: '))
palpites = 1
if jogador < pc:
    print('Mais... tente denovo')
elif jogador > pc:
    print('Menos... tente denovo')
while jogador != pc:
    jogador = int(input('Numero errado tente novamente, 0 a 10: '))
    palpites += 1
    if jogador < pc:
        print('Mais... tente denovo')
    elif jogador > pc:
        print('Menos... tente denovo')
print('eu estava pensando no {} vc acertou em  {} jogadas'.format(pc, palpites))