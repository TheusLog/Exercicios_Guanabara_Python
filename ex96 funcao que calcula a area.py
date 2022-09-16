def area(a, b):
    c = a * b
    print(f'A area de um terreno {a}x{b} é igual a de {c:.1f}')


L = float(input('Largura (m): '))
C = float(input('Comprimento (m): '))
print(area(L, C))