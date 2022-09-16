preço1 = float(input('Informe o preço do produto:'))
n = int(input("""Selecione a opção de pagamento:
[ 1 ] Dinheiro ou Cheque
[ 2 ] À vista no cartão
[ 3 ] Parcelado em 2 vezes no cartão
[ 4 ] Parcelado em 3 vezes ou mais

Sua opção:"""))
if 1 <= n <= 4:
    if n == 1:
        preço2 = preço1 * 0.9
        forma = 'em DINHEIRO ou CHEQUE'
    elif n == 2:
        preço2 = preço1 * 0.95
        forma = 'À VISTA no CARTÃO'
    elif n == 3:
        preço2 = preço1
        forma = 'PARCELADO em 2X'
    else:
        preço2 = preço1 * 1.2
        forma = 'PARCELADO em 3X'
    print('O preço {} será: R${:.2f}.'.format(forma, preço2))
else:
    print('Opção inválida, tente novamente.')