import sys
import math

n = int(input()) # nombre de chevaux
m = []
d = []
for i in range(n):
    pi = int(input())  # la puissance p de chaque cheval
    m.append(pi)

 # il faut renvoyer la différence entre les 2 puissances les plus proches

m.sort()
for i in range(n - 1):
    d.append(abs(m[i] - m[i + 1]))
print(min(d))