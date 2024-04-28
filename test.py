class MaClasse:
    def __init__(self):
        self.ma_variable = None

# Création d'une instance de la classe
objet = MaClasse()

# Vérification si l'attribut de la classe a la valeur None
if objet.ma_variable is None:
    print("L'attribut de la classe a la valeur None.")
else:
    print("L'attribut de la classe n'a pas la valeur None.")
print(objet.ma_variable)
