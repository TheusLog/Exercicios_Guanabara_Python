num = int(input('Digite um numero inteiro: '))
print('''escolha uma das bases para conversao:
[ 1 ] converter para BINARIO
[ 2 ] Converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opc = int(input('Digite sua Opcao: '))
if opc == 1:
    print('{} convertido para BINARIO é igual a {}'.format(num, bin(num)[2:]))
elif opc == 2:
    print('{} Convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opc == 3:
    print('{} Convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Informacao incorreta, tente novamente.')