
while True:
    num = None
    while num == None:
        try:
            num = int(input('Digite um tumero para ver sua tabuada: '))
        except:
            print('Digite um valor valido')

    print('{:=^40}'.format('TABUADA'))
    for c in range(1, 11):
        if num < 1:
            print('Programa encerrado')
            break
        print(f'{num} x {c} = {num*c}')
print('{:=^40}'.format('FIM!'))