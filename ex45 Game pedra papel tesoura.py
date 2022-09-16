from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computrador = randint(0, 2)
print('''Suas opcoes:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=' *13)
print('Computador jogou {}'.format(itens[computrador]))
print('jogador jogou {}'.format(itens[jogador]))
print('-=' *13)
if computrador == 0: # computador jogou PEDRA
   if jogador == 0:
       print('EMPATE')
   elif jogador == 1:
       print('JOGADOR VENCE')
   elif jogador == 2:
       print('COMPUTADOR VENCE')
   else:
       print('JOGADA INVALIDA!')
elif computrador == 1: # computador jogou PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVALIDA!')
elif computrador == 2: # computador jogou TESOURA
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVALIDA!')
