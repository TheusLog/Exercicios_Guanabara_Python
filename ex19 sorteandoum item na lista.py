import random
n1 = str(input('digite quatro nomes: '))
n2 = str(input(':'))
n3 = str(input(':'))
n4 = str(input(':'))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('O aluno escolhido foi',escolhido)