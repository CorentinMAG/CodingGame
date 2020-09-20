import sys
import math

passerelles = []

li1 = []
li2 = []

n, l, e = [int(i) for i in input().split()] # nb totaux de noeuds, nb de liens, nb de passerelles
for i in range(l):
    n1, n2 = [int(j) for j in input().split()] # lien entre les noeuds
    li1.append(n1)
    li2.append(n2)

for i in range(e):
    ei = int(input())  # position des passerelles de sorties
    passerelles.append(ei)

def neighbours(node):
    v = []
    if node in li1:
        for i,e in enumerate(li1):
            if e == node:
                v.append(li2[i])
    if node in li2:
        for i,e in enumerate(li2):
            if e == node:
                v.append(li1[i])
    return v

def find_next_passerelle(nodes):
    for el in nodes:
        if el in passerelles:
            return el
    return passerelles[0]


while True:
    si = int(input())  # position de l'agent
    si_neighbours = neighbours(si) # les noeuds voisins du skynet
    passerelle = find_next_passerelle(si_neighbours) # la passerelle la plus proche du skynet
    nodes = neighbours(passerelle) # les voisins de la passerelle
    if si in nodes:
        node = si
    else:
        node = nodes[0]
    print("{} {}".format(passerelle,node))
