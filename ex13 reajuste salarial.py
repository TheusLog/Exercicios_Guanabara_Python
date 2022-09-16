s = float(input('qual é o salario autal: R$'))
ns = s + (s * (15 / 100) )
print('o funcionario que ganhava {:.2f}, com 15% de aumento ficara em {:.2f}'.format(s, ns))