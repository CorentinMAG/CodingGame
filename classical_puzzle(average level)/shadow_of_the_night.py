import sys
import math

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]

# conditions de départ
# x va de 0 à w et y de 0 à h
x_f=0 
x_l = w 
y_f=0
y_l = h 

#quand on nous dit de nous déplacer, on resize les limites de la box (principe de la dicotomie)
# puis la case ou on doit sauter ça va être au centre de la nouvelle zone

# game loop
while True:
    bomb_dir = input()
    if 'U' in bomb_dir:
        y_l = y0 - 1
    elif 'D' in bomb_dir:
        y_f = y0 + 1
    if 'R' in bomb_dir:
        x_f = x0 + 1
    elif 'L' in bomb_dir:
        x_l = x0 - 1
    x0,y0 = (x_l + x_f) // 2 , (y_l + y_f) // 2
    
    print(x0,y0)
