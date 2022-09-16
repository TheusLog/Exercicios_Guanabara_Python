print('A via é de 80KM/h')
v = int(input('Voce passou em qual velocidade:  '))
if v > 80:
    print('Voce foi multado em {:.2f}'.format((v - 80) * 7))
else:
    print('Tenha uma boa Viagem')
