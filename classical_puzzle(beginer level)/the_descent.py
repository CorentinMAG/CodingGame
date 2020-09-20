import sys
import math

# game loop
while True:
    mountains = []
    for i in range(8):
        mountain_h = int(input())  # represents the height of one mountain.
        mountains.append(mountain_h)
    max_height = max(mountains)
    print(mountains.index(max_height))