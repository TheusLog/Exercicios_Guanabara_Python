dicionario = dict()
dicionario['nome'] = str(input("Nome do jogador: "))
gols = list()
somaGols = 0
partidas = int(input(f"Quantas partidas o {dicionario['nome']} jogou? "))
for i in range(partidas):
    gols.append(int(input(f'Quantos gols na {i+1}° partida? ')))
    somaGols += gols[i]
dicionario['gols'] = gols
dicionario['total'] = somaGols
print("-=" * 20)
print(dicionario)
print("-=" * 20)
for k,v in dicionario.items():
    print(f'O campo {k} tem o valor {v}')
print("-=" * 20)
print(f'O jogador {dicionario["nome"]} jogou {partidas} partidas.')
for x in range(5):
    print(f'=> Na partida {x} fez {gols[x]} gols.')
print(f'Foi um total de {dicionario["total"]} gols.')