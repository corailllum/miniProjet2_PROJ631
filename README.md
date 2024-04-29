Le décodage du Huffman permet de décompresser des fichiers qui ont été codés par se même procéder, la compression de Huffman permet de compresser un fichier en fonction du nombre d'occurrences de chaque caractère. Pour cela, on construit un arbre binaire en fonction d nombre d'itération de chaque lettre et on le parcourt afin de trouver le nombre d'occurrences. 
Pour la décompression, nous construisons aussi l'arbre puis nous donnons la chaîne de caractère binaire codé en paramètre du parcours pour la décoder petit à petit.

Ce projet a été codé en python.

J'ai décidé de coder en programmation orientée objet.
J'ai créé 3 classes :
La classe main :
Permet de lire le fichier binaire faire les traitements puis d'écrire dans le fichier text.txt le fichier décompresser 

Le classe arbrebinaire : 
Permet la création d'objets arbre binaire qui est utilisé afin de créer l'arbre 

La classe arbreHuffman : 
Permet la création de l'arbre, le parcours de décodage du texte et le calcule de gain et de taux de compression des lettres.

Installation 
Pour l'installation du programme, il suffit de télécharger les fichiers du git et d'ouvrir dans un éditeur de code python la classe Main.

Utilisation 
Il faut dans un premier temps importer dans le dossier miniProjet2 les fichiers de décodage et d'alphabets que vous voulez décoder.
Pour utiliser le décodage, il faut dans la classe main a la ligne 18 entré le nom du fichier binaire contenant le texte a décoder. 
Il faut aussi à la ligne 45 du main donner le nom du fichier alphabets comportant les lettres utiliser et leur nombre d'occurrences. 
Le fichier décodé sera envoyé le fichier du nom texte_decoder

Crédit 
Pour comprendre la construction de l'arbre et le parcours, j'ai utilisé cette vidéo : https://www.youtube.com/watch?v=Wfdv6854QTw

Piste d'amélioration

Dans la classe arbrehuffman 
Il faut revoir les méthodes de parcours de l'arbre et de création de l'arbre, je pense qu'il y a un problème dans la gestion de la listetempo qu'il me sert à la création de l'arbre. 
En effet, pour que la méthode marche avec l'exemple qui nous a été donné, j'ai été obligé d'ajouter les nouveaux nœuds au début de la listetempo. 

