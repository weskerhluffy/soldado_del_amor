'''
Created on 26/10/2017

@author: ernesto
'''

# XXX: http://codeforces.com/blog/entry/18034
"""
It's easy to count who wins and after how many "fights", but it's harder to say, that game won't end. How to do it?
Firstly let's count a number of different states that we can have in the game. Cards can be arranged in any one of n! ways. In every of this combination, we must separate first soldier's cards from the second one's. We can separate it in n + 1 places (because we can count the before and after deck case too).
So war has (n + 1)! states. If we'd do (n + 1)! "fights" and we have not finished the game yes, then we'll be sure that there is a state, that we passed at least twice. That means that we have a cycle, and game won't end.
After checking this game more accurately I can say that the longest path in the state-graph for n = 10 has length 106, so it is enough to do 106 fights, but solutions that did about 40 millions also passed.
Alternative solution is to map states that we already passed. If we know, that we longest time needed to return to state is about 100, then we know that this solution is correct and fast.
"""

import logging
import sys
from collections import deque

logger_cagada = None

nivel_log = logging.ERROR
#nivel_log = logging.DEBUG

def queue_a_tupla(q):
    tupla = tuple(list(q))
    logger_cagada.debug("la tupla de {} es {}".format(q, tupla))
    return tupla

def soldado_del_amor_barajea(pila1, pila2, comps_ya_vistas):
    if((queue_a_tupla(pila1), queue_a_tupla(pila2)) in comps_ya_vistas):
        return False
    comps_ya_vistas.add((queue_a_tupla(pila1), queue_a_tupla(pila2)))
    elem1 = pila1.popleft()
    elem2 = pila2.popleft()
    logger_cagada.debug("comparando {} con {}".format(elem1, elem2))
    if(elem1 > elem2):
        pila1.append(elem2)
        pila1.append(elem1)
    else:
        pila2.append(elem1)
        pila2.append(elem2)
    return True
        
def soldado_del_amor_core(nums1, nums2):
    q1 = deque(nums1)
    q2 = deque(nums2)
    num_vueltas = 0
    comps_ya_vistas = set()
    conti = True
    
    while conti and q1 and q2:
        logger_cagada.debug("la q1 {} la q2 {}".format(q1, q2))
        conti = soldado_del_amor_barajea(q1, q2, comps_ya_vistas)
        num_vueltas += 1
    
    if not conti:
        return None, None
    
    if not q1:
        return num_vueltas, 2
    else:
        return num_vueltas, 1
    
    
def soldado_del_amor_main():    
    lineas = list(sys.stdin)
    nums1 = [int(x) for x in lineas[1].strip().split(" ")]
    nums2 = [int(x) for x in lineas[2].strip().split(" ")]
    n_v, g = soldado_del_amor_core(nums1[1:], nums2[1:])
    if n_v:
        print("{} {}".format(n_v, g))
    else:
        print("-1")
    

if __name__ == '__main__':
    FORMAT = "[%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"
    logging.basicConfig(level=nivel_log, format=FORMAT)
    logger_cagada = logging.getLogger("asa")
    logger_cagada.setLevel(nivel_log)
    soldado_del_amor_main()
