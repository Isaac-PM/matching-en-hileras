"""
Title  : Own interpretation of the Boyer-Moore string matching algorithm & INSTRUMENTED
Author : Isaac Fabián Palma Medina @ isaac.palma.medina@est.una.ac.cr
Type   : Own authorship & INSTRUMENTED
"""
import random
import sys
sys.path.insert(0, '../matching-en-hileras/Utilities')
from generateString import generate_text_and_pattern
from generateString import generate_equal_text

def boyer_moore_instrumentado(t:str, p:str):
    contador:int = 0
    m:int = len(p)
    n:int = len(t)
    bad_char:str = [-1] * (256) 
    for i in range(m):
        bad_char[ord(p[i])] = i
    j:int = m - 1
    c:int = 0
    while c <= (n - m):
        while j >= 0 and p[j] == t[c + j]:
            j -= 1
            contador += 2
        if j < 0:
            if c + m < n:
                c += m - bad_char[ord(t[c + m])]
                contador += 1
            else:
                c += 1
        else:
            c += max(1, j - bad_char[ord(t[c + j])])
            contador += 1
        j = m - 1
    return contador

def test_boyer_moore_instrumentado(maxi:int):
    file = open("../matching-en-hileras/Boyer-Moore/test_boyer_moore_instrumentado.csv", 'w')
    file.write('n;time\n')
    for n in range(maxi):
        text_and_pattern = generate_equal_text(n)
        if text_and_pattern != None:
            print(text_and_pattern)
            print(f"{len(text_and_pattern[0])};{boyer_moore_instrumentado(text_and_pattern[0], text_and_pattern[1])}")
            file.write(f"{len(text_and_pattern[0])};{boyer_moore_instrumentado(text_and_pattern[0], text_and_pattern[1])}\n")
    file.close()

test_boyer_moore_instrumentado(30)