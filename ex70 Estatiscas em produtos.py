print('-' * 40)
print('             LOJAS RINTT')
print('-' * 40)
total = menor = cont = cont1 = 0
preco = None
while True:
    produto = str(input('Nome do Produto: '))

    while preco == None:
        try:
            preco = float(input('Preço: '))
        except:
            print('Digite um valor valido')

    resp = ' '
    while resp not in 'SsNn':
        resp = str(input('Tem mais algun produto? [S/N] '))

    total += preco

    if preco >= 1000:
        cont1 += 1
    if cont == 0:
        menor = preco
        nome = produto
        cont += 1
    if preco <= menor:
        menor = preco
        nome = produto

    preco = None

    if resp in 'Nn':
        print(f'O total da compra foi de R${total:.2f}')
        print(f'Temos {cont1} prdutos custando mais de R$1000.00')
        print(f'O produto mais barato foi {nome} que custava {menor:.2f} ')
        break
