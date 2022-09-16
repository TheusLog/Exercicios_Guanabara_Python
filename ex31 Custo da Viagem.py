km = int(input('Olá, Otimo dia. Qual sera a distancia percorrida em km:'))
if km > 200:
    print('O valor total da viagem fica em {:.2f}'.format(km*0.50))
if km <= 200:
    print('O valor total da viagem fica em {:.2f}'.format(km*0.45))
