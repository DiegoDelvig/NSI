from random import randint
from matplotlib.pyplot import*

def dicho(v,tab):
    """
    Recherche une valeur dans un tableau
    """

    taille = len(tab)
    test = False
    a = 0
    b= taille - 1
    c = 0

    while test == False and b - a > 1:
        milieu = (a+b) // 2

        if tab[milieu] == v:
            position = milieu
            test = True

        elif tab[milieu] > v:
            b= milieu - 1
            c = c + 1

        else:
            a = milieu + 1
            c = c + 1

    if v == tab[a]:
        position = a

    elif v == tab[b]:
        position = b

    elif test==False:
        position = -1

    c = c + 1
    return position , c


x = []
y = []

for i in range(1, 201):
    x.append(i * 10)
    y.append(0)

for j in range(1, 201):
    cm = 0
    temp = []

    for k in range(1, 1 + j * 10):
        temp.append(k)

    for l in range(1, 101):
        cm = cm + dicho(randint(1, j * 10), temp)[1]

    y[j - 1] = (cm / 100)

axis([0,2000,0,15])
mode=True
grid(mode)
title("compléxité")
xlabel("x")
ylabel("y")
scatter(x,y, 1 ,"red")
show()



