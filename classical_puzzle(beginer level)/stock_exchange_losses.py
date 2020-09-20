import sys
import math

n = int(input()) # le nombre de valeurs en bourse
v_list = []

for i in input().split():
    v = int(i)  # les valeurs
    v_list.append(v) 

val = v_list[0]
diff = 0

for i in range(1,len(v_list)):
    loss = v_list[i] - val
    val = max(val,v_list[i])
    diff = min(diff,loss)
print(diff)
        


