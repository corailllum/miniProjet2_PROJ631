class ArbreBinaire:
    """classe qui permet de créé des arbre binaire 
    
    """

    def __init__(self,poid,lettreassocier):
        self.lettreassocier=lettreassocier if lettreassocier is not None else None
        self.filsG=None
        self.filsD=None
        self.poid=poid
    
    #getteur et des setteur 
    def getpoid(self):
        return self.poid
    
    def getFilsG(self):
        return self.filsG
    
    def getFilsD(self):
        return self.filsD
    
    def getlettre(self):
        return self.lettreassocier
    
    def setfgauche(self,arbg):
        self.filsG=arbg

    def setfdroit(self,arbd):
        self.filsD=arbd

    def estfeuille (self):
        return self.filsG is None and self.filsD is None