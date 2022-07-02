"""
Title  : Own interpretation of the naive string matching algorithm & INSTRUMENTED
Author : Isaac Fabián Palma Medina @ isaac.palma.medina@est.una.ac.cr
Type   : Own interpretation & INSTRUMENTED

Source authors:
Agrawal, M. (2020a). Search Algorithm [Software]. Retrieved from: https://www.youtube.com/watch?v=nK7SLhXcqRo
garg10may. (2018). Find Algorithm [Software]. Retrieved from: https://stackoverflow.com/questions/41199057/naive-string-search-algorithm-python
"""

import sys
sys.path.insert(0, '../matching-en-hileras/Utilities')
from generateString import generate_text_and_pattern

def naive_instrumentado(t:str, p:str):
    contador:int = 0
    m:int = len(p)
    n:int = len(t)
    a:list = []
    for i in range(n - m + 1):
        flag:bool = True
        for j in range(m) :
            if t[i + j] != p[j]:
                flag = False
                break
            contador += 3 # Counts != comparison plus t[i + j] and p[j] accesses to t.
        if j == m - 1 and flag:
            pass
            # a.append((i, i + m - 1))
        contador += 1 # Counts j == m comparison.
    # print(f"{a = }")
    return contador       

def test_naive_instrumentado(maxi:int):
    file = open("test_naive_instrumentado.csv", 'w')
    file.write('n;time\n')
    for n in range(3, maxi):
        text_and_pattern = generate_text_and_pattern(n, 0)
        if(text_and_pattern != ""):
            print(f"{n};{naive_instrumentado(text_and_pattern[0], text_and_pattern[1])}")
            file.write(f"{n};{naive_instrumentado(text_and_pattern[0], text_and_pattern[1])}\n")
    file.close()

test_naive_instrumentado(100)
