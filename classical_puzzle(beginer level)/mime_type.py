import sys
import math

n = int(input()) # nombre d'éléments de la table d'association 
q = int(input())  # nombre de fichier à analyser (dont il faut trouver le mime type)
dictionnaire = {}

for i in range(n):
    ext, mt = input().split()
    dictionnaire[ext.lower()] = mt # les extensions sont les clés du dictionnaire et le mime type les valeurs

for i in range(q):
    fname = input() 
    if '.' in fname and len(fname.split('.')[-1]) > 0:
        fext = fname.split('.')[-1].lower()
    else:
        fext = None
    if fext in dictionnaire.keys():
        print(dictionnaire[fext])
    else:
        print("UNKNOWN")
