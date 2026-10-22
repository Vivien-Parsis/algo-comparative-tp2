import time
import random
from colis import Colis
from gestionnaire import GestionnaireColis
from tri import tri_fusion
from camion import chargement_glouton

def generer_colis(taille):
    destinations = ["Paris", "Lyon", "Marseille", "Lille", "Bordeaux", "Nantes"]
    colis_liste = []
    for i in range(taille):
        c = Colis(id_colis=i, poids=random.uniform(1.0, 30.0), valeur=random.uniform(10.0, 200.0), priorite=random.randint(1, 5), destination=random.choice(destinations))
        colis_liste.append(c)
    return colis_liste

def recherche_lineaire(liste, cible_id):
    for c in liste:
        if c.id == cible_id:
            return c
    return None

def lancer_benchmark():
    tailles = [100, 1000, 10000, 100000]
    resultats = []

    print("=")
    print("BENCHMARK DE PERFORMANCE ET PASSAGE A L'ECHELLE")
    print("=")

    for n in tailles:
        print(f"\nGeneration de {n} colis...")
        donnees = generer_colis(n)
        gestionnaire = GestionnaireColis()
        for c in donnees:
            gestionnaire.ajouter(c)

        id_cible = n - 1

        t0 = time.perf_counter()
        gestionnaire.trouver_par_id(id_cible)
        t_hash = time.perf_counter() - t0

        t0 = time.perf_counter()
        recherche_lineaire(gestionnaire.colis_liste, id_cible)
        t_lineaire = time.perf_counter() - t0

        t0 = time.perf_counter()
        tri_fusion(gestionnaire.colis_liste, key=lambda c: c.poids)
        t_tri = time.perf_counter() - t0

        t0 = time.perf_counter()
        chargement_glouton(gestionnaire.colis_liste, capacite_max=500.0, avec_priorite=True)
        t_camion = time.perf_counter() - t0

        resultats.append({"n": n, "t_hash": t_hash, "t_lineaire": t_lineaire, "t_tri": t_tri, "t_camion": t_camion})

        print(f"Taille n = {n}:")
        print(f"Recherche Hash : {t_hash:.8f} s")
        print(f"Recherche Lineaire : {t_lineaire:.8f} s")
        print(f"Tri Fusion : {t_tri:.6f} s")
        print(f"Chargement Camion : {t_camion:.6f} s")

    return resultats

if __name__ == "__main__":
    lancer_benchmark()
