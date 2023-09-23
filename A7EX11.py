largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))

area = altura * largura 

tinta = area // 2

print('Você vai precisar de {} latas de tinta.'.format(tinta))