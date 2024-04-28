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
        """
        """
        print("entré liste ")
        for z in range (len(liste)):
            print(liste[z].getpoid())
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
        print("sorite liste ")
        """for o in range (len(listetrie)):
            print(listetrie[o].getpoid())
            print(listetrie[o].getlettre())"""
        self.listetempo=listetrie
    
    

    """def triecarc(self,liste):
        listetrie=[liste[0]]
        for i in range(1,len(liste)):
            
            for j in range(len(listetrie)):"""
                


    def constructionARB(self):
        print("on reste zen")
        for z in range (len(self.listetempo)):
            print(self.listetempo[z].getpoid())
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

            # Trie 'listetempo' à nouveau
            self.tripoid(self.listetempo)

            # Appelle récursivement la méthode pour continuer la construction de l'arbre
            self.constructionARB()

        

    #parcourt de l'arbre
    def decodage(self, strbin):
       
            
        """
        Méthode qui parcourt l'arbre pour retrouver l'encodage de chaque caractère
        et l'ajoute dans une chaîne de caractères pour décoder le texte.

        Args:
        - strbin: Chaîne de caractères de 0 et 1 (binaire)

        Returns:
        - str: Texte décodé
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
        print(texte_decode)
        print(self.poidMax)
        print(len(texte_decode))
        return texte_decode


        """
        Méthode qui parcourt l'arbre pour retrouver l'encodage de chaque caractère
        et l'ajoute dans une chaîne de caractères pour décoder le texte.

        Args:
        - strbin: Chaîne de caractères de 0 et 1 (binaire)

        Returns:
        - str: Texte décodé
        
        if self.poidMax==len(self.texteF):
             # Initialisez la chaîne pour stocker le texte décodé
            current_node = self.listetempo[0]  # Démarre à partir de la racine

            for bit in strbin:
                if bit == '0':
                    current_node = current_node.getFilsG()  # Déplacez-vous vers le fils gauche
                elif bit == '1':
                    current_node = current_node.getFilsD()  # Déplacez-vous vers le fils droit

                if current_node.estfeuille():
                    lettre = current_node.getlettre()
                    self.texteF += lettre
                    current_node = self.listetempo[0]  # Réinitialise le nœud à la racine
            print(self.texteF)
        print(self.texteF)
        return "texte_decode"""

