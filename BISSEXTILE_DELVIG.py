# Diego Delvig 1G7

def test_bissextile(annee: int) -> bool:

    """    Retourne True si l'année en paramètre est bissextile et False si elle ne l'est pas   """


    bissextile = False

    if annee % 4 == 0 and annee % 100 != 0 or annee % 400 == 0:
        bissextile = True

    return bissextile


reponse = int(input('Entrer une année:  '))

if test_bissextile(reponse) is True:
    print("L'année ", reponse," est bissextile")
else:
    print("L'année ", reponse," n'est pas bissextile")
