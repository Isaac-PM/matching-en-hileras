"""
Title  : Own interpretation of the Knuth-Morris-Pratt string matching algorithm & INSTRUMENTED
Author : Isaac Fabián Palma Medina @ isaac.palma.medina@est.una.ac.cr
Type   : Own interpretation & INSTRUMENTED
"""

import random
import sys
sys.path.insert(0, '../matching-en-hileras/Utilities')
from generateString import generate_text_and_pattern
from generateString import generate_equal_text

def get_lps(p:str): # Construcción de la LPS.
    m:int = len(p)
    lps = [0] * m
    index_behind, i = 0, 1
    while i < m:
        if p[i] == p[index_behind]:
            lps[i] = index_behind + 1
            index_behind += 1
            i += 1
        elif index_behind == 0:
            lps[i] = 0
            i += 1
        else:
            index_behind = lps[index_behind - 1]
    return lps

def knuth_morris_pratt_instrumentado(t:str, p:str):
    contador:int = 0
    m:int = len(p)
    n:int = len(t)
    lps:list = get_lps(p) # Obtiene la LPS correspondiente al patrón.
    i:int = 0
    j:int = 0
    while i < n: # Saltos entre los índices según la LPS.
        if t[i] == p[j]:
            i, j = i + 1, j + 1
        contador += 2 # Counts t[i] and p[j].
        if j == m :
            j = lps[j - 1]
            contador += 1 # Counts lps[j - 1].
        elif i < n and p[j] != t[i]:
            if j != 0 :
                j = lps[j - 1]
                contador += 1 # Counts lps[j - 1].
            else :
                i += 1
        contador += 2 # Counts p[j] and t[i].
    return contador

def test_knuth_morris_pratt_instrumentado(maxi:int):
    file = open("../matching-en-hileras/Knuth-Morris-Pratt/test_knuth_morris_pratt_instrumentado.csv", 'w')
    file.write('n;time\n')
    for n in range(3, maxi):
        text_and_pattern = generate_text_and_pattern(n, 0)
        if text_and_pattern != None:
            print(text_and_pattern)
            print(f"{len(text_and_pattern[0])};{knuth_morris_pratt_instrumentado(text_and_pattern[0], '$')}")
            file.write(f"{len(text_and_pattern[0])};{knuth_morris_pratt_instrumentado(text_and_pattern[0], '$')}\n")
    file.close()

test_knuth_morris_pratt_instrumentado(40)