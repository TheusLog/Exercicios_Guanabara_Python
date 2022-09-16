import math
an = float(input('digite um angulo: '))
se = math.sin(math.radians(an))
print('o angulo de {} tem o seno de {:.2f}!'.format(an, se))
co = math.cos(math.radians(an))
print('o angulo de {} tem o cosseno de {:.2f}!'.format(an, co))
tan = math.tan(math.radians(an))
print('o angulo de {} tem a tangente de {:.2f}!'.format(an, tan))