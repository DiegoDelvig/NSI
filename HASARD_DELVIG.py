# Diego Delvig 1G7


def lehmer(x, a, c, m):
    """ Retourne le terme qui suit suivant l'algorithme de lehmer """
    x = (a * x + c) % m
    return x

a = 25
c = 16
m = 256
x = 8497

alea = [x % 10]

for i in range(100):
    x = lehmer(x, a, c, m)
    alea.append(x % 10)

print(alea)


"""
EXERCICE:
a) Tous pairs, une boucle

b) Tous impaires, une bouclte

c) Que des pseudo-aleatoire "10"

d) l'unité augmente de 0 jusqu'a 9 en boucle

"""
