def metade(p=0, formato=False):
    resp = p / 2
    return resp if formato is False else moeda(resp)


def dobro(p=0, formato=False):
    resp = p * 2
    return resp if formato is False else moeda(resp)


def aumentar(p=0, n=0, formato=False):
    resp = p + (p * (n / 100))
    return resp if formato is False else moeda(resp)


def diminuir(p=0, n=0, formato=False):
    resp = p - (p * (n / 100))
    return resp if formato is False else moeda(resp)


def moeda(preco = 0, moeda = 'R$'):
    return f'{moeda}{preco:8>.2f}'.replace('.', ',')


def resumo(p, t1, t2):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preco analisado: \t\tR${p}'.replace('.', ','))
    print(f'A medade do preco: \t\t{metade(p, True)}')
    print(f'O dobro do preco: \t\t{dobro(p, True)}')
    print(f'80% de aumento: \t\t{aumentar(p, t1, True)}')
    print(f'12% de reducao: \t\t{diminuir(p, t2, True)}')
    print('-' * 30)