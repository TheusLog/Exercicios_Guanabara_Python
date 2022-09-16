from datetime import date
ano = int(input('Informe seu ano de nascimento '))
idade = date.today().year - ano
if idade == 18:
    print('\033[33mHora de se alistar!!!\033[m')
elif idade < 18:
    print(f'\033[34mAinda falta {18 - idade} anos para você se alistar')
    print(f'Seu alistamento será em {date.today().year + 18 - idade}\033[m')
elif idade > 18:
    print(f'\033[31mVocê está atrasado {idade - 18} anos!!')
    print(f'Seu alistamento foi em {date.today().year - (idade - 18)}')