from datetime import date
atual = date.today().year
nasc = int(input('Em que ano voce nasceu: '))
idade = atual - nasc
print('Voce tem {} anos por isso esta na'.format(idade))
if idade <= 9:
    print('Categoria mirim')
elif idade  >= 10 and idade <= 14:
    print('Categoria Infatil')
elif idade >=15 and idade <=19:
    print('Categoria junior')
elif idade >= 20 and idade <= 25:
    print('Categoria SENIOR')
elif idade > 25:
    print ('Categoria MASTER')