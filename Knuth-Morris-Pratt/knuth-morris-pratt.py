"""
Title  : Own interpretation of the Knuth-Morris-Pratt string matching algorithm
Author : Isaac Fabián Palma Medina @ isaac.palma.medina@est.una.ac.cr
Type   : Own interpretation

Source authors:
Knuth, D. E., Morris, Jr., J. H., & Pratt, V. R. (1977). Fast Pattern Matching in Strings. SIAM Journal on Computing, 6(2), 323–350. Retrieved from: https://sci-hub.se/https://doi.org/10.1137/0206024
NeetCode. (2021, 14 noviembre). Knuth–Morris–Pratt KMP - Implement strStr() - Leetcode 28 - Python. YouTube. Retrieved from:  https://www.youtube.com/watch?v=JoF0Z7nVSrA
m00nlight. (2016). Python KMP algorithm. GitHub Gist. Retrieved from: https://gist.github.com/m00nlight/daa6786cc503fde12a77
"""

def get_lps(p:str): # Cosntrucción de la LPS.
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

def knuth_morris_pratt(t:str, p:str):
    m:int = len(p)
    n:int = len(t)
    lps:list = get_lps(p) # Obtiene la LPS correspondiente al patrón.
    i:int = 0
    j:int = 0
    a:list = []
    while i < n: # Saltos entre los índices según la LPS.
        if t[i] == p[j]:
            i, j = i + 1, j + 1
        if j == m :
            a.append((i - m, i - 1))
            j = lps[j - 1]
        elif i < n and p[j] != t[i]:
            if j != 0 :
                j = lps[j - 1]
            else :
                i += 1
    return a

print(knuth_morris_pratt("aadcabababd", "ababd"))

"""
Output
[(6, 10)]
"""