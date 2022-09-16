list = []
for c in range(0, 5):
    list.append(int(input('Digite um numero: ')))
print(f'O maior valor digitado foi o {max(list)} na posicao {list.index(max(list))}')
print(f'O menor foi o {min(list)} na posicao {list.index((min(list)))}')
