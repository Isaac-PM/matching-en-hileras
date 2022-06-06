"""
Title  : Own interpretation of the naive string matching algorithm
Author : Isaac Fabián Palma Medina @ isaac.palma.medina@est.una.ac.cr
Type   : Own interpretation

Source authors:
Agrawal, M. (2020a). Search Algorithm [Software]. Retrieved from: https://www.youtube.com/watch?v=nK7SLhXcqRo
garg10may. (2018). Find Algorithm [Software]. Retrieved from: https://stackoverflow.com/questions/41199057/naive-string-search-algorithm-python
"""

def sm_naive(t:str, p:str):
    m:int = len(p)
    n:int = len(t)
    a:list = []
    for i in range(n - m + 1) :
        flag:bool = True
        for j in range(m) :
            if t[i + j] != p[j] :
                flag = False
                break
        if j == m - 1 and flag:
            a.append((i, i + m - 1))
    return a       

print(sm_naive("AGCATGCTGCAGTCATGCTTAGGCTA", "GCT"))

"""
Output
[(5, 7), (16, 18), (22, 24)]
"""
