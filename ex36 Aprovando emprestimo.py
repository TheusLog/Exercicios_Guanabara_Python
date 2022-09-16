casa = float(input('Qual o valor da casa: '))
salario = float(input('Qual o seu salario: '))
anos = int(input('Em quantos anos vc quer pagar: '))
cond = salario * (30 / 100)
mes = anos * 12
prestacao = casa / mes
if prestacao <= cond:
    print('Parabens o emprestimo foi aprovado')
    print('ficara em {} de {:.2f}'.format(mes, prestacao))
else:
    print('o emprestimo foi negado')
    print('sua renda precisa ser superior a 30% do seu salario')
    print('30% da sua renda:',cond)
    print('Prestacao ficara em {:.2f}'.format(prestacao))
