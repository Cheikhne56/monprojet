print("Voici le contenu du fichier :")
file= open("file.txt","r")
fichier =file.readlines()
for i in fichier :
    print (i)
listes=open("listes.txt","w")
for i in fichier[:2] :
    listes.write(i)
matrice=open("matrice.txt","w")     
for i in fichier[3:]:
    matrice.write(i)
matrice.close()
listes.close()
file.close()
print("\n")
print("Voici les deux listes :")
l= open("listes.txt","r")
fichier =l.readlines()
for i in fichier :
    print (i)
print("\n")
print("Voici la matrice :")
m=open("matrice.txt","r")
mat=m.readlines()
for i in mat:
    print(i)
m.close()
l.close()
 