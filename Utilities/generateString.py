"""
Title  : Generate pattern and text
Author : Isaac Fabián Palma Medina @ isaac.palma.medina@est.una.ac.cr
Type   : Own authorship
"""

import random
import string

alphabet = string.ascii_lowercase

vocab_length_max = random.randint(0,26)
vocab_length_min = random.randint(0,vocab_length_max)
vocabulary = alphabet[vocab_length_min:vocab_length_max]

def generate_text_and_pattern(maxi:int, mode:int):
    if maxi == 0 or maxi < 3:
        return ""
    text:str = ""
    pattern:str = ""
    for i in range(3):
        pattern += vocabulary[random.randint(0,len(vocabulary) - 1)]
    for i in range(maxi):
        text += vocabulary[random.randint(0,len(vocabulary) - 1)]
    # print(text, pattern)
    if mode == 1:
        return(text, pattern)
    return(text, " ")