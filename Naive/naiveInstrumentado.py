"""
Title  : Own interpretation of the naive string matching algorithm & INSTRUMENTED
Author : Isaac Fabián Palma Medina @ isaac.palma.medina@est.una.ac.cr
Type   : Own interpretation & INSTRUMENTED
"""

import random
import sys
sys.path.insert(0, '../matching-en-hileras/Utilities')
from generateString import generate_text_and_pattern
from generateString import generate_equal_text

def naive_instrumentado(t:str, p:str):
    contador:int = 0
    m:int = len(p)
    n:int = len(t)
    for i in range(n - m + 1):
        flag:bool = True
        for j in range(m):
            if t[i + j] != p[j]:
                break
            contador += 2 # Counts t[i + j] and p[j].
        if j == m - 1 and flag:
            pass
    return contador

def test_naive_instrumentado(maxi:int):
    file = open("../matching-en-hileras/Naive/test_naive_instrumentado.csv", 'w')
    file.write('n;time\n')
    for n in range(maxi):
        text_and_pattern = generate_equal_text(n, 2)
        if text_and_pattern != None:
            print(text_and_pattern)
            print(f"{len(text_and_pattern[0])};{naive_instrumentado(text_and_pattern[0], text_and_pattern[1])}")
            file.write(f"{len(text_and_pattern[0])};{naive_instrumentado(text_and_pattern[0], text_and_pattern[1])}\n")
    file.close()

test_naive_instrumentado(20)
