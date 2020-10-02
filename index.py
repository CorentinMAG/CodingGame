# coding: utf-8

"""
 * Objectif générale de l'exercice :
 * J'ai des échanges de messages entre des applicatifs.
 * Ces échanges sont uni-directionnels (src->dst) et ordonnées par un numéro de séquence commençant à 0
 * Certains de mes messages peuvent arriver dans le désordre ce qui peut faire bugguer mes applications.
 * Il faut donc faire un service capable de remettre les messages dans l'ordre
 * Exemple pour une conversation unique :
 *  1) Je reçois le message 0, je le transmets (c'était le message attendu)
 *  2) Je reçois le message 2 alors que j'attends le message 1, je le stocke mais ne transmet rien
 *  3) Je reçois le message 1, je transmets les messages 1 et 2 dans l'ordre
"""

messages = []
expected_msg = 0

def reorder_msg(msg):
    global expected_msg
    j = 0
    messages.append(msg)
    ordered_messages = sorted(messages)
    if len(ordered_messages) == 1 and ordered_messages[0] == expected_msg:
        print(ordered_messages)
        messages.remove(expected_msg)
        ordered_messages.remove(expected_msg)
        expected_msg += 1
    elif msg == expected_msg:
        for i in range(len(ordered_messages)):
            if i >= 1 :
                if ordered_messages[i] == ordered_messages[i - 1] + 1 :
                    j+=1
                else:
                    print(ordered_messages[:i])
                    expected_msg = ordered_messages[i -1] + 1
                    for _ in range(i):
                        messages.remove(ordered_messages[0])
                        ordered_messages.remove(ordered_messages[0])
                    break
                if j == len(ordered_messages) - 1:
                    expected_msg = ordered_messages[-1] + 1
                    print(ordered_messages)
                    messages.clear()
reorder_msg(1)
reorder_msg(0)
reorder_msg(2)
reorder_msg(4)
reorder_msg(3)
