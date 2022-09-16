list = []
resp = ''
while True:
    num = (int(input('Digite um valor: ')))
    if num not in list:
        list.append(num)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Nao vou adicionar')
    resp = str(input('Deseja continuar: [S/N]')).strip().upper()
    if resp == 'S':
        continue
    if resp == 'N':
        break
print(f'Sua lista ficou assim {list} com {len(list)} elementos')
list.reverse()
print(f'sua lista em reverso ficara {list}')
if 5 in list:
    print(f'O valor 5 foi encontrado na lista')
else:
    print('Nao encontramos o valor 5 na lista')