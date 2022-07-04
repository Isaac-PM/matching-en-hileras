"""
Title  : Own interpretation of the Boyer-Moore string matching algorithm
Author : Isaac Fabián Palma Medina @ isaac.palma.medina@est.una.ac.cr
Type   : Own interpretation

Source authors:
Deshmukh, N. (2021, March 29). Boyer moore algorithm for pattern searching - Kalkicode. Recuperado de https://kalkicode.com/boyer-moore-algorithm-pattern-searching
Langmead, B. (2015, May 19). ADS1: Practical: Implementing Boyer-Moore. Youtube. Recuperado de https://www.youtube.com/watch?v=CT1lQN73UMs
"""

def boyer_moore(t:str, p:str):
    m:int = len(p)
    n:int = len(t)
    a:list = []
    bad_char:str = [-1] * (256) 
    # Se inicializa según la cantidad posbile de caracteres, en este caso 256 según ASCII.
    for i in range(m):
        bad_char[ord(p[i])] = i
        # En la lista de caracteres, para cada elemento del patrón, guarda su valor posicional en este (primera ocurrencia).
    j:int = m - 1
    c:int = 0
    while c <= (n - m): # Tomando en cuenta los largos de t y p.
        while j >= 0 and p[j] == t[c + j]:
            j -= 1
        if j < 0:
            a.append((c, c + m - 1)) # En caso de coincidencia lo guarda.
            if c + m < n:
                c += m - bad_char[ord(t[c + m])]
            else:
                c += 1
        else:
            c += max(1, j - bad_char[ord(t[c + j])])
        j = m - 1
    return a

print(boyer_moore("trusthardtoothbrushestoothbrushes", "tooth"))
print(boyer_moore("iscreamyouscreamweallscreamforicecream", "scream"))

"""
Output
[(9, 13), (21, 25)]
[(1, 6), (10, 15), (21, 26)]
"""