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
