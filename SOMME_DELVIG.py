# Diego Delvig 1G7

def somme(n: int) -> int:
    """
    Retourne la somme des premiers entier consecutifs non nul de n (n= le nombre choisie par l'utilisateurs)
    """

    resultat = 0

    for i in range(n + 1):
        resultat = resultat + i

    return resultat

reponse = int(input('Nombre:    '))

if reponse > 0:
    print(somme(reponse))
