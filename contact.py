import pickle

fichier_contact = "contact.pkl"
liste_contact = []

def enregistrer_contact(liste_contact):
    with open(fichier_contact, "wb") as fichier:
        pickle.dump(liste_contact, fichier)

def lire_contact():
    try:
        with open(fichier_contact, "rb") as fichier:
            return pickle.load(fichier)
    except (FileNotFoundError, EOFError):
        return []
    
def ajouter_contact(nom, tel):
    contact = lire_contact()
    contact.append([nom, tel])
    enregistrer_contact(contact)
    print(nom, 'ajouté avec succès !')

def rechercher_contact(nom):
    contact = lire_contact()
    for contact in contact:
        if contact[0].lower() == nom.lower():
            return "Nom:", contact[0]," Téléphone:", contact[1]
    print("Contact non trouvé.") 

def modifier_contact(nom, newtel):
    liste_contact = lire_contact()
    for k in range(len(liste_contact)):
         if liste_contact[k][0].lower() == nom.lower():
            liste_contact[k][1] = newtel
    enregistrer_contact(liste_contact)

def supprimer_contact(nom):
    liste_contact = lire_contact()
    for k in range(len(liste_contact)):
        if liste_contact[k][0].lower() == nom.lower():  
            del liste_contact[k] 
            enregistrer_contact(liste_contact)  
            print("Le contact", nom, "a été supprimé avec succès.")
            return 
    print("Le contact", nom, "n'a pas été trouvé.")

async def menu():
    while True:
        print("\n0 : Afficher les contacts\n1 : Ajouter un Contact\n2 : Rechercher un contact\n3 : Modifier un Contact\n4 : Supprimer un contact\n5 : Quitter")
        choix = input("Quelle fonctionnalité souhaitez-vous utiliser ? ")

        if choix == "0":
            contacts = lire_contact()
            if contacts:
                print("\nListe des contacts :")
                for contact in contacts:
                    print("Nom : ", contact[0], "Téléphone : ", contact[1])
            else:
                print("Aucun contact enregistré.")

        elif choix == "1":
            nom = input("Veuillez entrer le nom du contact : ")
            tel = input("Veuillez entrer le numéro de téléphone du contact : ")
            while len(tel) != 10:
                print("Le numéro de téléphone n'est pas au bon format !")
                tel = input("Veuillez entrer le numéro de téléphone du contact : ")
            ajouter_contact(nom, tel)

        elif choix == "2":
            nom = input("Veuillez entrer le nom du contact recherché : ")
            print(rechercher_contact(nom))

        elif choix == "3":
            nom = input("Veuillez entrer le nom du contact à modifier : ")
            newtel = input("Veuillez entrer le nouveau numéro de téléphone : ")
            modifier_contact(nom, newtel)

        elif choix == "4":
            nom = input("Veuillez entrer le nom du contact à supprimer : ")
            supprimer_contact(nom)

        elif choix == "5":
            print("Fermeture du programme.")
            break

        else:
            print("Choix invalide, veuillez réessayer.")

await menu()