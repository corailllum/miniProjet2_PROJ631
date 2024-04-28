le decodage du Huffman pemet de decompresser de fichier qui on été code par se meme procéder, la compression de huffman permet de compresser un fichier en 
fonction du nombre d'occurence de chaque caractere. Pour cela on construie un arbre binaire en fonction d nombre d'iteration de chaque lettre et on le parcour afin de trouver le nombre d'occurence 
pour la decompresstion nous construison aussi l'arbre puis nous donnons la fais de caratere binaire coder en paramettre du parcour pour la decoder petit a petit

ce proget a été coder en python

j'ai decider de coder en programation orientée object
j'ai créé 3 classe :
la classe main 
permet de lire le fichier binaire faire les traitement puis d'ecrire dans le fichier text.txt le fichie decompresser 

la classe arbre binaire 
permet la creation d'obect arbre binaire qui sont utiliser afin de cree l'arbre 

la classe arbre huffman 
permet la creation de l'arbre , le parcours de decodage du text et la calucle de gain et de taux de compression des lettre 

Installtion 
pour l'instalation du programme il suffit de telecharger les fichier du git 

Utilisation 
il faut dans un premeir temps importé dans le dosier miniProjet2 les fichier de decodage et d'alphabets
pour utiliser le decodage il faut dans la class main a la ligne 18 entré le nom du fichier binaire contenant le texte a decoder 
il faut aussi a la ligne 45 du main donner le nom du fichier alphabets comportant les lettre utiliser et leur nombre d'ocurence 
le fichier decoder sera dans le fichier du nom texte_decoder

crédit 
pour comprendre le decodage j'ai utilisée cette video : https://www.youtube.com/watch?v=Wfdv6854QTw

piste d'ameloriation 

dans le class arbrehuffman 
il faut revoir les methode de parcours de l'arbre et de creation de l'arbre je pense qu'il y a un probeleme dans la gestion de la liste temporaraie qu'il me sert a la creation de l'arbre 
en effet pour que la methode marche avec l'exemple qui nous a été donner j'ai ete obliger d'ajouter les nouc=veau noeud au debut de la liste 

