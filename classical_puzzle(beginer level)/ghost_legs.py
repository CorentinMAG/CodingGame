import sys
import math

w, h = [int(i) for i in input().split()]

top = input().split()

diagram = []

for i in range(1,h-1):
    line = input()
    diagram.append(line)

bottom = input().split() 

#  A  B  C      A2
#  |  |  |      B1
#  |--|  |      C3
#  |  |--|
#  |  |--|
#  |  |  |
#  1  2  3


for i,t in enumerate(top):
    x,y= 0, i*3
    pos = i
    while x != h - 2:
        if y + 1 < w - 1:
            if diagram[x][y+1] == '-':
                pos+=1
                y+=3
            elif diagram[x][y-1] == '-':
                pos-=1
                y-=3
            x+=1
        else:
            if diagram[x][y-1]=='-':
                pos-=1
                y-=3
            x+=1
    print(t+str(bottom[pos]))