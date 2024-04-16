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
nbCaractere=0
dicoalphabets={}
def lectureFichierTexte(nomfichier):
    """fonction qui permet de lire et recuprée les information du fichier alphabets 
    entré: nom du fichier alphabets str
    sortie: str dictionnaire/listes de l'alphabets 
    """
    with open(nomfichier,'r') as f:
        #lecture et recuperation du nombre total de caractere
        data=f.readline()
        nbCaractere=data[0]
        data=f.readline()
        print(data)
        while(data!=""):
            print(42)
            print(data)
            tabCharactereDutexte.append(data[0])
            tabIterationTexte.append(data[2])
            dicoalphabets[data[0]]=data[2]
            #tabIterationTexte.append(data[2])
            data=f.readline()
        f.close()    
        """
        data=f.readline()
        data=f.readline()
        tabCharactereDutexte.append(data[0])
        data=f.readline()
        tabCharactereDutexte.append(data[0])
        data=f.readline()
        tabCharactereDutexte.append(data[0])
        data=f.readline()
        tabCharactereDutexte.append(data[0])
        data=f.readline()
        tabCharactereDutexte.append(data[0])
        data=f.readline()
        tabCharactereDutexte.append(data[0])
        data=f.readline()
        tabCharactereDutexte.append(data[0])
        
        print(tabCharactereDutexte)
        f.close()"""
    return

lectureFichierTexte('exemple_freq.txt')
print(dicoalphabets)
print(tabCharactereDutexte)
print(tabIterationTexte)
print(fichier_binaire)