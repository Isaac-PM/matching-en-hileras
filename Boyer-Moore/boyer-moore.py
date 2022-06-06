"""
Autor / Author : Isaac Fabián Palma Medina @ isaac.palma.medina@est.una.ac.cr

Tipo  / Type   : Elaboración propia
"""

def get_value(length:int, index:int):
    return length - index - 1

def generate_bad_match_table(pattern:str): # Construcción de la Bad Match Table.
        if " " in pattern : return -1
        bmt:list = []
        for i in range(len(pattern) - 1):
            if not pattern[i] in bmt :
                bmt.append(pattern[i])
                bmt.append(get_value(len(pattern), i))
            else :
                bmt[bmt.index(pattern[i]) + 1] = get_value(len(pattern), i)
        bmt.extend([pattern[len(pattern) - 1], len(pattern), " ", len(pattern)])
        it = iter(bmt)
        pattern = dict(zip(it, it))
        return pattern

def boyer_moore(t:str, p:str):
    if len(t) < len(p): # Verificación inicial.
        return -1
    bmt:dict = generate_bad_match_table(p) # Obtiene la BMT correspondiente al patrón.
    
    coincidence_list:list = []
    aux_list:list = []
    p_length:int = len(p)
    current_index:int = p_length
    carriage:int = p_length
    finished:bool = False
    
    while not finished:
        if carriage + p_length > len(t): # Verifica si es posible "encajar" p en lo que resta de t.
            finished = True   
        if current_index == p_length:
            coincidence_list = [] 
        if t[carriage] != p[current_index - 1]: # Movimiento inicial de la "ventana" o "carro".
            if not t[carriage] in p:
                carriage += bmt.get(" ")
            else:
                carriage += bmt.get(t[carriage])
            current_index = len(p)
        else:
            coincidence_list.append(carriage) # Añade donde existe una coincidencia de el carácter.
            if len(coincidence_list) == p_length:
                aux_list.append((coincidence_list[len(coincidence_list) - 1], coincidence_list[0]))
                coincidence_list = []
                carriage += p_length
                current_index = p_length
            else:
                carriage -= 1
                current_index -= 1
    return aux_list

print(boyer_moore("trusthardtoothbrushestoothbrushes", "tooth"))

print(boyer_moore("iscreamyouscreamweallscreamforicecream", "scream"))

"""
Output
[(9, 13), (21, 25)]
[(1, 6), (10, 15), (21, 26)]
"""