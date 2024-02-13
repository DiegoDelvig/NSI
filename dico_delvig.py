# Diego Delvig 


def compare(mot1: str, mot2: str) -> int:
    """
    Retourne l'ordre alphabetique entre les deux mots passés en argument
    """
    reponse = ''
    i = 0
    run = True
    while run:
        if (mot1[i] < mot2[i]):
            reponse = f'{mot1} < {mot2}'
            run = False
        elif (mot1[i] > mot2[i]):
            reponse = f'{mot1} > {mot2}'
            run = False
        if (len(mot1) - 1 == i):
            reponse = f'{mot1} < {mot2}'
            run = False
        elif (len(mot2) - 1 == i):
            reponse = f'{mot1} > {mot2}'
            run = False
        if (len(mot1) - 1 == i and len(mot2) - 1 == i) and (mot1[i] == mot2[i]):
            reponse = f'{mot1} = {mot2}'
            run = False
        i += 1
    return reponse

def comp_liste(liste: list) -> str:
    """
    Retourne le permier mot de la liste passée en argument qui apparait dans le dictionnaire
    """
    petit = liste[0]
    for i in range(len(liste)):
        if (compare(petit, liste[i]) == f'{petit} > {liste[i]}'):
            petit = liste[i] 
    return petit 


reponse = int(input('1: comparer deux mot / 2: comparer des mots dans une liste  '))

if (reponse == 1):
    mot1 = input('Premier mot   ')
    mot2 = input('Deuxieme mot  ')
    print(compare(mot1, mot2))
    

if (reponse == 2):
    liste = input('mot1/mot2/mot3 ...   ').split('/')
    print(f'{comp_liste(liste)} est le premier mot qui apparait dans le dictionnaire dans la liste')

