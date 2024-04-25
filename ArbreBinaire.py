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
    
    def setfgauche(self,arbg):
        self.filsG=arbg

    def setfdroit(self,arbd):
        self.filsD=arbd