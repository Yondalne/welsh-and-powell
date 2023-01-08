graphe = [
    [ 0, 1, 0, 0, 0, 1, 1 ],
    [ 1, 0, 1, 0, 0, 0, 1 ],
    [ 0, 1, 0, 0, 0, 0, 1 ],
    [ 0, 0, 0, 0, 1, 0, 0 ],
    [ 0, 0, 0, 1, 0, 1, 1 ],
    [ 1, 0, 0, 0, 1, 0, 1 ],
    [ 1, 1, 1, 0, 1, 1, 0 ],
    ]

listColor = ["vert", "rouge", "bleu", "blanc", "noir", "violet", "jaune"]
print(graphe[0][0])

# [index, couleur, degre]
ordreSommet = [
    [0, "", 0],
    [1, "", 0],
    [2, "", 0],
    [3, "", 0],
    [4, "", 0],
    [5, "", 0],
    [6, "", 0],
]

for i in range(len(ordreSommet)):
    ordreSommet[i][2] = graphe[i].count(1)

#ranger les sommet dans l'ordre decroissant des degre
ordreSommet.sort(key = lambda x: x[2], reverse = True)

usedColor = []
for i in range(len(ordreSommet)):
    # Si le sommet n'a pas de couleur
    if not ordreSommet[i][1]:
        ordreSommet[i][1] = listColor[i] # On lui attribur la couleur actuelle 

        for j in range(i+1, len(ordreSommet)):
            # si le sommet n'est pas un voisin et n'a pas de couleur, on lui attribue la couleur actuelle
            if (not ordreSommet[j][1]) and (graphe[ordreSommet[i][0]][ordreSommet[j][0]] == 0):
                ordreSommet[j][1] = listColor[i]
        
        # Ajout de la couleur a la liste des couleur utilisees et passage a la suivante        
        usedColor.append(listColor[i])

print("Il faut ", str(len(usedColor)), " couleurs au minimum")
print("Couleurs utilisees : ", usedColor)
print("indexSommet / couleur / degre : \n", ordreSommet)