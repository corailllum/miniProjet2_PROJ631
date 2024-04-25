from ArbreBinaire import *

class ArbreHuffman:
    """"""
    # Constructeur
    def __init__(self, dicolettre, poidMax):
        self.listefeuille = self.crealistefeuille(dicolettre)
        self.poidMax = poidMax
        self.listetempo = self.crealistefeuille(dicolettre)
        self.texteF = ""
        
    # Methode 
    # Creation de toutes les feuilles 
    def crealistefeuille(self, dicolettre):
        """"""
        listefeuille = []
        listecle = dicolettre.keys()
        for cle in listecle:
            listefeuille.append(ArbreBinaire(dicolettre[cle], cle))
        return listefeuille

    #creation de l'arbre
        #trie des liste 
    def tripoid(self,liste):
        """"""
        listetrie=[liste[0]]
        for i in range(1,len(liste)):
            for j in range(len(listetrie)):
                if(liste[i].getpoid()<listetrie[j].getpoid()):
                    listetrie.insert(j,liste[i])
                    break
                elif(j==len(liste)-1):
                    listetrie.append(liste[i])

        self.listetempo=listetrie
        

    def constructionARB(self):
        """"""
    # Vérifie s'il y a au moins deux éléments dans 'listetempo' et si le poids du premier élément est inférieur ou égal à 'poidMax'
        while len(self.listetempo) > 1 and self.listetempo[0].getpoid() <= self.poidMax:
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
            self.listetempo.append(nouvelarbre)
            # Trie 'listetempo' à nouveau
            self.tripoid(self.listetempo)
        # Affiche 'listetempo' après la construction de l'arbre
        print(self.listetempo)

    #parcourt de l'arbre

    def decodage (self):
        """"""
