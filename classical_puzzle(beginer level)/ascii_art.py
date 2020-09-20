import sys
import math

chaine = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ?'

l = int(input()) # la largeur d'une lettre en art ascii
h = int(input()) # la hauteur d'une lettre en art ascii
t = input() # le mot qui doit être traduit en art ascii
answer=""

### c'est les rows

 #  ##   ## ##  ### ###  ## # # ###  ## # # #   # # ###  #  ##   #  ##   ## ### # # # # # # # # # # ### ### 
# # # # #   # # #   #   #   # #  #    # # # #   ### # # # # # # # # # # #    #  # # # # # # # # # #   #   # 
### ##  #   # # ##  ##  # # ###  #    # ##  #   ### # # # # ##  # # ##   #   #  # # # # ###  #   #   #   ## 
# # # # #   # # #   #   # # # #  #  # # # # #   # # # # # # #    ## # #   #  #  # # # # ### # #  #  #       
# # ##   ## ##  ### #    ## # # ###  #  # # ### # # # #  #  #     # # # ##   #  ###  #  # # # #  #  ###  #  

### 

for i in range(h):
    row = input()
    for letter in t:
        try:
            index = chaine.index(letter.upper())
        except:
            index = chaine.index('?')  #le caractère n'est pas dans la liste donc on doit renvoyer un ?
        answer += row[ index * l : index*l + l ]
    answer += '\n'
print(answer)
