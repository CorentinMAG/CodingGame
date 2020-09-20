import sys
import math

w, h = [int(i) for i in input().split()] # taille de la carte (largeur , hauteur)
start_row, start_col = [int(i) for i in input().split()] # point de départ
maps = []
resultat = []
n = int(input()) # nombre de carte
for i in range(n):
    myMap = []
    for j in range(h):
        map_row = input()
        myMap.append(map_row)
    maps.append(myMap)  # on ajoute toutes les cartes dans maps

# renvoie le nombre de tentative pour trouver le trésor ou TRAP
def find_treasure(_map,x0,y0):
    previous_tuple = [] # contient les coordonnées déjà parcourus
    posX = x0
    posY = y0
    status = True
    tempt = 0 # nombre de tentative
    while status and (posX,posY) not in previous_tuple:   
        if _map[posX][posY] == '<':
            previous_tuple.append((posX,posY))
            tempt += 1
            posY -= 1
        elif _map[posX][posY] == '>':
            previous_tuple.append((posX,posY))
            if posY+1 < w:
                tempt +=1 
                posY += 1
            else:
                tempt = math.inf
                status = False
        elif _map[posX][posY] == 'v':
            previous_tuple.append((posX,posY))
            tempt +=1
            posX += 1
        elif _map[posX][posY] == '^':
            previous_tuple.append((posX,posY))
            tempt +=1
            posX -= 1
        elif _map[posX][posY] == 'T':
            tempt +=1
            status = False   
        else:
            tempt = math.inf
            status = False
    if (posX,posY) in previous_tuple:
        tempt = math.inf
    return tempt
            
for map_ in maps:
    index = find_treasure(map_,start_row,start_col)
    resultat.append(index)

if min(resultat) == math.inf:
    ind = 'TRAP'
else:
    ind = resultat.index(min(resultat))
print(ind)

