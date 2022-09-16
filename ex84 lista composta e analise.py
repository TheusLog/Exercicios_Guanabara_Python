lista = []
dados = []
resp = ''
maior = menor = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(int(input('peso: ')))

    if len(lista) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]

    lista.append(dados[:])
    dados.clear()
    resp = str(input('Deseja continuar: [S/N]')).strip().upper()

    if resp == 'S':
        continue
    if resp == 'N':
        break

print(f'Ao todo, voce cadastrou {len(lista)} pessoas. ')
print(f'O maior peso foi de {maior}Kg de', end='')
for p in lista:
    if p[1] == maior:
        print(f' {p[0]}')
print(f'O menor peso foi {menor}Kg de', end='')
for p in lista:
    if p[1] == menor:
        print(f' {p[0]}')