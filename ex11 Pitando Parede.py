l = float(input('Digite a largura da parede: '))
a = float(input('Digite a altura da parede: '))
print('Sua parede tem a dimensão de {} x {} e sua área é de {:.2f} m².'.format(l, a, (l*a)))
print('Para pintar essa parede, você precisará de {:.3}'.format((l*a)/2))