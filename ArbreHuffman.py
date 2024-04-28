from ArbreBinaire import *

class ArbreHuffman:
    """
    classe qui crée un arbre de huffman permettant le decodage des fréquence

    """
    # Constructeur
    def __init__(self, dicolettre, poidMax,textbinaire):
        self.listefeuille = self.crealistefeuille(dicolettre)
        self.poidMax = poidMax
        self.listetempo = self.crealistefeuille(dicolettre)
        self.texteF = ""
        self.textBinaire=textbinaire

    #getteur et setteur 
    def gettextbin(self):
        return self.textBinaire 
    
    def gettextF(self):
        return self.texteF
    # Methode 
    # Creation de toutes les feuilles 
    def crealistefeuille(self, dicolettre):
        """
        methode qui créé l'entierter des feuilles 
        entré dictionnaire de l'alphabete et des fréquence 
        sortie liste d'arbre binaire correspondant au feuille 
        """
        listefeuille = []
        listecle = dicolettre.keys()
        for cle in listecle:
            listefeuille.append(ArbreBinaire(dicolettre[cle], cle))
        

        return listefeuille

    #creation de l'arbre
        #trie des liste 
    def tripoid(self,liste):
        """
        methode qui trie une liste en fonction du poid de son element et met ses valeur dans listetempo
        entré liste a trié
        sortie rien 

        j'ai créé cette fonction pour triée la liste en fonction du poid je voulait en faire une autre pour trié en fonction du code ascci
        cependant je me suis rendu compte que cela faisais planté la creation de l'arbre et donnais n'importe quoi apres le parcours de l'arbre
        """
        listetrie=[liste[0]]
        for i in range(1,len(liste)):
            
            for j in range(len(listetrie)):
                
                if(liste[i].getpoid()<listetrie[j].getpoid()):
                    listetrie.insert(j,liste[i])
                    break
                elif(j==len(listetrie)-1):
                    
                    listetrie.append(liste[i])
                    break

        self.listetempo=listetrie
    
    

                


    def constructionARB(self):
        """
        Méthode récursive pour construire l'arbre de Huffman en combinant les arbres de poids les plus faibles.

        Entrée: rien
        Sortie: rien
        """
        # Vérifie s'il y a au moins deux éléments dans 'listetempo' et si le poids du premier élément est inférieur ou égal à 'poidMax'
        if len(self.listetempo) > 1 and self.listetempo[0].getpoid() <= self.poidMax:
            # Récupère les deux arbres avec les poids les plus faibles
            arbreG = self.listetempo[0]
            arbreD = self.listetempo[1]

            # Calcule le nouveau poids en combinant les poids des sous-arbres
            nouvpoid = arbreG.getpoid() + arbreD.getpoid()

            # Crée un nouvel arbre avec le nouveau poids et les sous-arbres
            nouvelarbre = ArbreBinaire(nouvpoid, None)
            nouvelarbre.setfgauche(arbreG)
            nouvelarbre.setfdroit(arbreD)

            # Supprime les deux premiers éléments de 'listetempo'
            del self.listetempo[0]
            del self.listetempo[0]

            # Ajoute le nouvel arbre à 'listetempo'
            self.listetempo.insert(0,nouvelarbre)
            #au cour du projet j'ai eu beaucoup de mal a se que l'arbre se construise correctement, pour que cela marche j'ai ete oblige a ajoute les nouveau noeud au debut de la liste 
            #je ne sais pas pourquoi et cela peut peut etre etre un probleme pour d'autre fichier c'est quelque chose qu'il faudra ameliorer
            # Trie 'listetempo' à nouveau
            self.tripoid(self.listetempo)

            # Appelle récursivement la méthode pour continuer la construction de l'arbre
            self.constructionARB()

        

    #parcourt de l'arbre
    def decodage(self, strbin): 
        """
        Méthode qui parcourt l'arbre pour retrouver l'encodage de chaque caractère
        et l'ajoute dans une chaîne de caractères pour décoder le texte.

        entré : Chaîne de caractères de 0 et 1
        sortie: Texte décodé
        """
        # Initialisez la chaîne pour stocker le texte décodé
        texte_decode = ""
        current_node = self.listetempo[0]  # Démarre à partir de la racine

        for bit in strbin:
            if bit == '0':
                current_node = current_node.getFilsG()  # Déplacez-vous vers le fils gauche
            elif bit == '1':
                current_node = current_node.getFilsD()  # Déplacez-vous vers le fils droit

            if current_node.estfeuille():
                lettre = current_node.getlettre()
                texte_decode += lettre
                current_node = self.listetempo[0]  # Réinitialise le nœud à la racine
                
                # Vérifie si la longueur du texte décodé atteint le poids maximum
                if len(texte_decode) == self.poidMax:
                    break
        self.texteF=texte_decode
        print(self.texteF)
        return texte_decode

    def calculegain(self):
        """methode qui calcule le gain de place que a été effectuer par la compresstion
         entre : rien 
          sortie :le gain  """
        volumeini=len(self.texteF)*8
        volumef=len(self.textBinaire)
        return("gain",1-(volumef/volumeini))


    def calculetaux(self):
        """methode qui calcule le nombre moyen de bit qui a été utiliser pour coder un caractere 
        entre : rien 
        sortie : le taux """
        return (len(self.textBinaire)/self.poidMax)

    
