from random import randint
from time import sleep
pc = randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um numero de 0 a 5 ')
print('-=-' * 20)
player = int(input('Tente adivinhar:'))
print('PROCESSANDO...')
sleep(3)
if player == pc:
    print('Parabens voce acertou pensei no',pc)
else:
    print('Gahei, pensei no {} e nao no {}'.format(pc, player))













