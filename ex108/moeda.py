def metade(p=0):
    resp = p / 2
    return resp


def dobro(p=0):
    resp = p * 2
    return resp


def aumentar(p=0, n=0):
    resp = p + (p * (n / 100))
    return resp


def diminuir(p=0, n=0):
    resp = p - (p * (n / 100))
    return resp


def moeda(preco = 0, moeda = 'R$'):
    return f'{moeda}{preco:8>.2f}'.replace('.', ',')
