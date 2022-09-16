def fatorial(n):
    fat = 1
    i = 2
    while i <= n:
        fat = fat*i
        i = i + 1

    print(f'O fatorial de {n} é = {fat}')


n = int(input('Digite um numero:'))
print(fatorial(n))