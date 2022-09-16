import random
n1 = str(input('Digite um nomo: '))
n2 = str(input('Ditite outro nome: '))
n3 = str(input('Digite mais um nome: '))
n4 = str(input('ultimo nome :'))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('a ordem sera')
print(lista)