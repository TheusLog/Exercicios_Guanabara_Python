r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 == r2 and r1 == r3:
       print('Os seguimentos acima PODEM FORMAR um triângulo EQUILÁTERO')
elif r1 == r2 or r1 == r3 or r3 == r2:
          print('Os segmentos acima PODEM FORMAR um triângulo ISÓSCELES')
elif r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
         print('Os segmentos acima PODEM FORMAR  triângulo ESCALENO')
else:
         print('Os Segmentos acima NÃO PODEM formar um triângulo')
