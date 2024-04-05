#import des fichier ainsi que des bibliothec utile
from bitarray import bitarray



def lectureFichierBinaire(nomfichier):
    """fonction qui permet de lire et recupérer les donnée du fichier biaire 
    entré: nom du fichier binaire str
    sortie: le fichier 
    """
    res=""
    with open(nomfichier, 'rb') as f:
        data = f.read()
        binary_string = ''.join(format(byte, '08b') for byte in data)
        f.close()
    return(binary_string)

fichier_binaire =(lectureFichierBinaire('exemple_comp.bin'))
tabCharactereDutexte=[]
tabIterationTexte=[]
dicoalphabets={}
def lectureFichierTexte(nomfichier):
    """fonction qui permet de lire et recuprée les information du fichier alphabets 
    entré: nom du fichier alphabets str
    sortie: str
    """
    with open(nomfichier,'r') as f:
        data=f.readline()
        data=f.readline()
        data=f.readline()
        data=f.readline()
        data=f.readline()
        data=f.readline()
        data=f.readline()
        data=f.readline()
        
        
        tabCharactereDutexte.append(data)
        f.close()
    return

lectureFichierTexte('exemple_freq.txt')
print(tabCharactereDutexte)