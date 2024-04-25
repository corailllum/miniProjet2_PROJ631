#import des fichier ainsi que des bibliothec utile
from bitarray import bitarray
from Texte import *
from ArbreHuffman import *
from ArbreBinaire import *
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
        #lecture et recuperation des lettres et de leur iteration 
        while(data!=""):
            tabCharactereDutexte.append(data[0])
            tabIterationTexte.append(int(data[2]))
            dicoalphabets[data[0]]=int(data[2])
            data=f.readline()
        f.close()    
    return

lectureFichierTexte('exemple_freq.txt')
print(dicoalphabets)
#print(tabCharactereDutexte)
#print(tabIterationTexte)
print(fichier_binaire)
#texte=Texte(fichier_binaire,dicoalphabets)
ABR= ArbreHuffman(dicoalphabets,5)
ABR.constructionARB()

#creation des feuille contenant les lettres 
