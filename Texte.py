class Texte:
    """"""
    def __init__(self,texteBinaire,dicoAlphabet):
        self.texte=texteBinaire
        self.dicoAlphabet=dicoAlphabet
        print("object créé")



    def getdicoAlphabet(self):
        return self.dicoAlphabet
    
    def gettexteBinaire(self):
        return self.texteBinaire
    
    