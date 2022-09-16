num = int (input('Digite um tumero para ver sua tabuada: '))
print('{:=^40}'.format('TABUADA'))
for c in range(1, 11):
    print('{} x {} = {}'.format(num, c, num*c))
print('{:=^40}'.format('FIM!'))