#Compter les voyelles

def comter_voyelles(chaine):
    voyelles = 'aeiouAEIOU'
    compteur = 0
    for caractere in chaine:


        if caractere in voyelles:
            compteur += 1
    return compteur

texte = input("Entrez une chaîne de caractères: ")
nombre_voyelles = comter_voyelles(texte)        
print(f"Le nombre de voyelles dans la chaîne est: {nombre_voyelles}")
