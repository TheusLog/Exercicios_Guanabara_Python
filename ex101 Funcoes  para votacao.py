def votar(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'com {idade} anos  nao pode votar ainda'
    elif 16 <= idade < 18 or idade > 65:
        return f'com {idade} anos o voto é opcional'
    else:
        return f'com {idade} anos o voto é OBRIGATORIO!'


nasc = int(input('Em que ano voce nasceu? '))
print(votar(nasc))
