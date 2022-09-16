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
list.sort()
print(f'Sua lista ficou assim {list}')

