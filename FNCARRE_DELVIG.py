# Diego Delvig 1G7

from matplotlib.pyplot import *

axis([-3, 3, 0, 10])
grid(True)
xlabel('abscisse')
ylabel('ordonées')

pos_point = -3
for i in range(600):
	plot(pos_point, pos_point ** 2, 'kx')
	pos_point += 0.01

show()
