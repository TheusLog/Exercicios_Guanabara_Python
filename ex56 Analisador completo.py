somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totalmulheres20 = 0
for p in range(1, 5):
    print('----- {} PESSOA -----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mn':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if idade < 20 and sexo in 'Ff':
        totalmulheres20 += 1
mediaidade = somaidade / 4
print('A media de idade do grupo é de {:.1f} anos'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadehomem, nomevelho))
print('O numero de mulheres com menos de 20 anos sao {}'.format(totalmulheres20))