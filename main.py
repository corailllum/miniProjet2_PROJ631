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
            dicoalphabets[data[0]]=int(data[2])
            data=f.readline()
        f.close()    
    return nbCaractere




nbCaractere = lectureFichierTexte('exemple_freq.txt')
print("je ne suis pas un hero ")
print(nbCaractere)
print(dicoalphabets)

print(fichier_binaire)

ABR= ArbreHuffman(dicoalphabets,int(nbCaractere),fichier_binaire)
ABR.constructionARB()
ABR.decodage(ABR.gettextbin())
ABR.calculegain()
ABR.calculetaux()

def ecriturefichiertxt(gain,taux,text):
    """fonction qui permet de crée un fichier contenant le fichier decoder avec le calcule de gain et de taux """
    with open("texte_decoder.txt", 'w') as fichier:
            # Écrit le contenu dans le fichier
            fichier.write("le gain de place etais de ")
            fichier.write(str(gain))
            fichier.write("\n")
            fichier.write("le de taux de compression de chaque lettre etais de  ")
            fichier.write(str(taux))
            fichier.write("\n")
            fichier.write(text)
            fichier.close()

ecriturefichiertxt(ABR.calculegain(),ABR.calculetaux(),ABR.gettextF())
