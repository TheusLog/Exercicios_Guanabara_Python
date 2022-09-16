total = homem = mulher =0
idade = None
while True:

    print('-'*25)
    print('   CADASTRE UMA PESSOA')
    print('-'*25)

    while idade == None:
        try:
            idade = int(input('Idade: '))
        except:
            print('Digite um valor valido')

    sexo = ' '
    while sexo not in 'MmFf':
        sexo = str(input('Sexo: [M/F]'))
    print('-' * 25)

    continuar = ' '
    while continuar not in 'SsNn':
        continuar = str(input('Quer continuar? [S/N]'))
        print('Digite um valor valido')

    if idade >= 18:
        total += 1
    if sexo in 'Mm':
        homem += 1
    if idade <= 20 and sexo in 'Ff':
        mulher += 1

    if continuar in 'Nn':
        print(f'Total de pessoas com mais de 18 anos: {total}')
        print(f'Ao todo temos {homem} homens cadastrados')
        print(f'E temos {mulher} mulheres com menos de 20 anos.')
        break
    idade = None

