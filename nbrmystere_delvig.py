# Delvig Diego 1G7

import random


def plus_ou_moins():
    """
    jeux du juste prix
    """
    n = random.randint(0, 100)
    nbessai = 10
    i = 0
    while nbessai > i:

        question = int(input('Nombre:   '))

        if (question < n):
            print('plus')

        elif (question > n):
            print('moins')

        elif (question == n):
            print('gagné')
            i = nbessai
        i += 1


plus_ou_moins()

