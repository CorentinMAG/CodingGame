import sys
import math

width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis
tab=[]
for i in range(height):
    line = input()  # width characters, each either 0 or .
    t = [c for c in line]
    tab.append(t)

for index,n in enumerate(tab): # [[0,0,.],[0,.,.]]
    for i,p in enumerate(n): # pour chaque noeud (0) on affiche ses coordonnées ainsi que les coordonnées de ses voisins
        if p =='0':
            x1,y1 = i,index
            e,r=[1]*2
            g,h=[True]*2
            x2,y2,x3,y3 = [-1]*4
            while e < width - i and g:
                if n[i+e]=='0':
                    x2,y2 = i+e,index
                    g=False
                e +=1
            while r < height - index and h:
                if tab[index+r][i]=='0':
                    x3,y3 = i,index+r
                    h=False
                r+=1
            print(x1,y1,x2,y2,x3,y3)