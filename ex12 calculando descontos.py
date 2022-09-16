p = float(input('qual é o preco do produto: R$'))
np = p - (p * (5 / 100) )
print('o produto que custava {:.2f}, com 5% de desconto ficara em {:.2f}'.format(p, np))