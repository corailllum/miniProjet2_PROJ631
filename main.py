
from bitarray import bitarray
import os

def inverstion_fichier(nomfichier):
    res=""
    with open(nomfichier, 'rb') as f:
    # Lire le contenu du fichier en tant que séquence d'octets
        data = f.read()

# Convertir chaque octet en sa représentation binaire
        binary_string = ''.join(format(byte, '08b') for byte in data)

# Afficher la chaîne de caractères de 0 et de 1
    return(binary_string)


print(inverstion_fichier('exemple_comp.bin'))