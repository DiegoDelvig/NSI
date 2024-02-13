from matplotlib.pyplot import*

def mini(tab, index_debut):
    """ détermine le rang de l'élément le plus petit du début au dernier élément du tableau tab """
    minimum = tab[index_debut]
    index_mini = index_debut
    taille = len(tab)

    for i in range(index_debut, taille):
        if minimum > tab[i]:
            minimum = tab[i]
            index_mini = i
    return index_mini


def tri_selection(tab):
    taille = len(tab)

    for i in range(0, taille - 1):
        index_mini = mini(tab, i)
        a = tab[i]
        tab[i] = tab[index_mini]
        tab[index_mini] = a
    return tab



x1 = []
y1 = []
x2 = []
y2 = []

tab = []
for i in range(10):
    tab.append(1 + (-1) ** i * i)
    x1.append(i)
    y1.append(tab[i])


tab = tri_selection(tab)

for i in range(0, 10):
    x2.append(i)
    y2.append(tab[i])


axis([0,20,-10, 20])
mode=True
grid(mode)
title("selection")
xlabel("x")
ylabel("y")
scatter(x1, y1, 5 ,"red")
scatter(x2, y2, 5, "blue")


show()







