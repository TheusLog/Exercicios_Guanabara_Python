def ficha(j='<desconhecido>', gol=0):
    print(f'o jogador {j} fez {g} gols no campeonato')


n = str(input('Nome do jogador: '))
g = str(input('Numeros de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)