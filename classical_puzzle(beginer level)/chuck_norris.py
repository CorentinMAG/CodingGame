import sys
import math

message = input() #le caractère ou mor qui doit être encodé en binaire façon chuck norris
result = ""
b_message = ""

# le 1er bloc vaut toujours 0 ou 00
# 0 -> si la série contient des 1
# 00 -> si la série contient des zéros
# ensuite que des zéros correspondant aux nombres de bits dans la série

## exemple
# C -> 1000011
# -> 0 0 00 0000 0 00

for c in message:
    c_bit = bin(ord(c))[2:].zfill(7)
    b_message += c_bit

for i,b in enumerate(b_message):
    if i >= 1 and b_message[i] == b_message[i - 1]:
        result += '0'
    else:
        if b == '1':
            result += ' 0 0'
        elif b == '0':
            result += ' 00 0'
print(result.strip()) # on enlève l'espace au tout début