# Diego DELVIG 1G7

def test_bissextile(annee: int) -> bool:

    """    Retourne True si l'année en paramètre est bissextile et False si elle ne l'est pas   """

    bissextile = False

    if annee % 4 == 0 and annee % 100 != 0 or annee % 400 == 0:
        bissextile = True

    return bissextile




mois = [ 0, 3, 3, 6, 1, 4, 6, 2, 5, 0, 3 ,5 ]
jours = [ 'Dimanche', 'Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi' ]


date = input('ecrire une date sous la forme: jj/mm/aaaa ->  ')


# separer les informations
date = date.split('/')
dizainne = int(date[2][2:4])

# convertie en 'int'
date = [ int(i) for i in date ]

val_mois = mois[date[1] - 1]

# l'additions de la dizaines de l'année + un quart de cette dizaines + le jour + val_mois
val_finale = dizainne + dizainne // 4 + date[0] + val_mois

if date[2] >= 2000:
    val_finale -= 1


if test_bissextile(date[2]) and date[1] < 3:
    val_finale -= 1


val_finale %= 7

# Afficher le jour

print(f'Le {date[0]}/{date[1]}/{date[2]} est un {jours[val_finale]}')

