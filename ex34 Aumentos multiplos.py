salario = float(input('Qual o Salario do funcionario: '))
if salario > 1250.00:
    ns = salario + (salario * (10 / 100))
if salario <= 1250.00:
    ns = salario + (salario * (15 / 100))
print('O novo salario sera de',ns)