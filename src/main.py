from colis import Colis
from gestionnaire import GestionnaireColis
from src.benchmark import lancer_benchmark

def charger_donnees_initiales(gestionnaire):
    exemples = [
        Colis(101, 8.0, 20.0, 2, "Paris"),
        Colis(102, 3.0, 10.0, 5, "Lille"),
        Colis(103, 12.0, 40.0, 1, "Lyon"),
        Colis(104, 5.0, 25.0, 4, "Paris"),
        Colis(105, 2.0, 15.0, 3, "Lille"),
    ]
    for c in exemples:
        gestionnaire.ajouter(c)

def afficher_menu():
    print("\n===== GESTION DES LIVRAISONS =====")
    print("1. Afficher les colis")
    print("2. Ajouter un colis")
    print("3. Rechercher un colis")
    print("4. Organiser les colis")
    print("5. Préparer un camion")
    print("6. Afficher le chargement")
    print("7. Afficher les statistiques")
    print("0. Quitter")

def action_afficher(gestionnaire):
    print("\n--- Liste des colis ---")
    gestionnaire.afficher()

def action_ajouter(gestionnaire):
    try:
        id_c = int(input("Identifiant (ex: 106) : "))
        poids = float(input("Poids en kg (ex: 4.5) : "))
        valeur = float(input("Valeur (ex: 30) : "))
        prio = int(input("Priorite (1 a 5) : "))
        dest = input("Destination (ex: Marseille) : ").strip()
        if gestionnaire.ajouter(Colis(id_c, poids, valeur, prio, dest)):
            print("Colis ajoute avec succes.")
        else:
            print("Erreur : Un colis avec cet identifiant existe deja.")
    except ValueError:
        print("Erreur de saisie : Veuillez entrer des nombres valides.")

def action_rechercher(gestionnaire):
    try:
        id_c = int(input("Identifiant du colis a rechercher : "))
        colis = gestionnaire.trouver_par_id(id_c)
        if colis:
            print(f"Colis trouve : ID={colis.id}, Poids={colis.poids} kg, Valeur={colis.valeur}, Priorite={colis.priorite}, Destination={colis.destination}")
        else:
            print("Colis introuvable.")
    except ValueError:
        print("Identifiant invalide.")

def action_organiser(gestionnaire):
    print("\nCritere de tri :")
    print("1. Par poids (croissant)")
    print("2. Par valeur (decroissant)")
    print("3. Par priorite (decroissant)")
    s_choix = input("Votre choix : ").strip()
    if s_choix == "1":
        gestionnaire.afficher_selon_poids(decroissant=False)
    elif s_choix == "2":
        gestionnaire.afficher_selon_valeur(decroissant=True)
    elif s_choix == "3":
        gestionnaire.afficher_selon_priorite(decroissant=True)
    else:
        print("Choix invalide.")

def action_preparer_camion(gestionnaire):
    try:
        cap = float(input("Capacite maximale du camion en kg (ex: 50) : "))
        gestionnaire.preparer_camion(cap, avec_priorite=True)
        gestionnaire.afficher_chargement()
    except ValueError:
        print("Capacite invalide.")

def action_afficher_chargement(gestionnaire):
    gestionnaire.afficher_chargement()

def action_statistiques(gestionnaire):
    stats = gestionnaire.statistiques()
    print("\n=== Statistiques des colis ===")
    print(f"Nombre total de colis : {stats['total']}")
    print(f"Poids total : {stats['poids_total']:.1f} kg")
    print(f"Valeur totale : {stats['valeur_totale']:.1f}")
    print(f"Poids moyen : {stats['poids_moyen']:.1f} kg")
    print(f"Valeur moyenne : {stats['valeur_moyenne']:.1f}")

    rep = input("\nSouhaitez-vous lancer le benchmark de passage a l'echelle ? (o/n) : ").strip().lower()
    if rep == "o":
        lancer_benchmark()

def menu():
    gestionnaire = GestionnaireColis()
    charger_donnees_initiales(gestionnaire)

    while True:
        afficher_menu()
        choix = input("Choix : ").strip()

        if choix == "0":
            print("Au revoir.")
            break
        elif choix == "1":
            action_afficher(gestionnaire)
        elif choix == "2":
            action_ajouter(gestionnaire)
        elif choix == "3":
            action_rechercher(gestionnaire)
        elif choix == "4":
            action_organiser(gestionnaire)
        elif choix == "5":
            action_preparer_camion(gestionnaire)
        elif choix == "6":
            action_afficher_chargement(gestionnaire)
        elif choix == "7":
            action_statistiques(gestionnaire)
        else:
            print("Option non reconnue. Veuillez choisir entre 0 et 7.")

if __name__ == "__main__":
    menu()
