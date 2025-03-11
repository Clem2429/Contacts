import pickle
liste_contacts = []
def ajouter_contact(nom, tel):
    contacts = lire_contacts()
    contacts.append([nom, tel])
    enregistrer_contacts(contacts)
    print("Contacts", nom, " ajouté avec succés")

async def lire_contact():
    liste_contacts = input("Quel contact voulez-vous lire ? ")
    with open(liste_contacts, 'rb') as fichier:
        contenu = pickle.load(fichier)
    return contenu

async def menu():

    print("1 : Ajouter un Contact /n 2 : Rechercher un contact /n 3 : Modifier un Contact /n 4 : Supprimer un contact")
    choix_fonctionnalite = int(input("Quelle fonctionnalité souhaitez-vous utiliser ?"))
    if choix_fonctionnalite == 1:
        nom = input("Veuillez entrer le nom du contact : ")
        tel = input("Veuillez entrer le numéro de téléphone du contact : ")
        ajouter_contact(nom, tel)
    elif choix_fonctionnalite == 2:
        contact_recherche = input("Veuillez entrer le contact recherché : ")
        recherche_num = rechercher_contact(contact_recherche)
        print(recherche_num)
    elif choix_fonctionnalite == 3:
        print("Service temporairement indisponible.")
    elif choix_fonctionnalite == 4:
        contact_supp = input("Veuillez entrer le nom du contact que vous souhaitez suppprimer : ")
        liste_contacts.remove(contact_supp)
    else:
        print("Choix invalide, veuillez retenter.")