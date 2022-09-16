d = int(input('quantos dias alugados? '))
km = float(input('quantos km rodados? '))
pago = (d * 60) + (km *0.15)
print('o total a pagar é de R${:.2f}'.format(pago))