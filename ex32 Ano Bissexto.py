import calendar
ano = int(input('Digite o ano: '))
B = calendar.isleap(ano)
if B is True:
    print(f'O ano de {ano} é bissexto')
else:
    print(f'O ano de {ano} não é bissexto')