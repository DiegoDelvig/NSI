# Diego Delvig 1G7

def viellisement(prix: int, pourcentage: int):
    """    Retourne l'année dans laquelle le prix des machines couteras la moitié du prix a l'achat    """
    nb_annee = 0
    moitie_prix = prix / 2

    while prix >= moitie_prix:
        prix = prix * (1 - pourcentage / 100)
        nb_annee = nb_annee + 1

    return nb_annee


prix_machine = float(input('Le prix de la machine: '))
pourcentage = int(input('Le pourcentage qui sera appliqué chaque année: '))
annee = 2019

print("La machine devra être revendu en ", annee + viellisement(prix_machine, pourcentage))
