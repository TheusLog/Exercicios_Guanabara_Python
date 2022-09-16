valor1 = int(input('Digite um valor: '))
valor2 = int(input('Digite outro valor: '))
opc = 0
while opc != 5:
    print('''MENU 
    [ 1 ] Soma
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos numeros
    [ 5 ] Sair do programa''')
    opc = int(input('Qual sua opcao: '))
    if opc == 1:
        print('a soma entre {} e {} é {}'.format(valor1, valor2, (valor1 + valor2)))
    elif opc == 2:
        print('A multiplicacao entre {} e {} é {}'.format(valor1, valor2, (valor1 * valor2)))
    elif opc == 3:
        if valor1 > valor2:
            print('o maior valor entre {} e {} é {}'.format(valor1, valor2, valor1))
        else:
            print('o maior valor entre {} e {} é {}'.format(valor1, valor2, valor2))
    elif opc == 4:
        print('informe os valores novamente')
        valor1 = int(input('Digite um valor: '))
        valor2 = int(input('Digite outro valor: '))

print('Fim do Programa volte sempre!')