import sys
import math

light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

# game loop
while True:
    choix = ''
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.
    if light_y - initial_ty > 0 :
        choix += 'S'
        initial_ty += 1
    elif light_y - initial_ty < 0:
        choix +='N'
        initial_ty -= 1
    if light_x - initial_tx > 0:
        choix += 'E'
        initial_tx += 1
    elif light_x - initial_tx < 0:
        choix += 'W'
        initial_tx -= 1
    print(choix)
