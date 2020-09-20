import sys
import math

n = int(input())  # the number of temperatures to analyse
if n == 0:
    print(0)
elif n >= 0 and n < 10000:
    temp = [] #tableau des températures
    dist = [] #tableau des distances par rapport à 0
    for i in input().split():
        t = int(i)
        temp.append(t)
    for t in temp:
        dist.append(abs(t))
    min_t = min(dist) #on récupère la distance minimale, qui correspond à la température qu'on veut récupérer
    try:
        index = temp.index(min_t) #si on ne trouve pas l'index c'est que la température est négative et non positive
    except:
        index = temp.index(-min_t)
    finally:
        print(temp[index])