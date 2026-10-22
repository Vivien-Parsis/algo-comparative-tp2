from tri import tri_fusion
from camion import chargement_glouton

class GestionnaireColis:
    def __init__(self):
        self.colis_par_id = {}
        self.colis_liste = []
        self.dernier_chargement = None

    def ajouter(self, colis):
        if colis.id in self.colis_par_id:
            return False
        self.colis_par_id[colis.id] = colis
        self.colis_liste.append(colis)
        return True

    def trouver_par_id(self, colis_id):
        return self.colis_par_id.get(colis_id)

    def tous_les_colis(self):
        return self.colis_liste

    def trier_par(self, critere="poids", decroissant=False, algorithme="fusion"):
        criteres = {"poids": lambda c: c.poids, "valeur": lambda c: c.valeur, "priorite": lambda c: c.priorite}
        cle = criteres.get(critere, lambda c: c.id)

        if algorithme == "fusion":
            return tri_fusion(self.colis_liste, key=cle, reverse=decroissant)
        return sorted(self.colis_liste, key=cle, reverse=decroissant)

    def afficher(self, liste=None, limite=20):
        items = self.colis_liste if liste is None else liste
        if not items:
            print("Aucun colis enregistre.")
            return
        total = len(items)
        affichees = items[:limite]
        print(f"{'ID':<8} {'Poids':<10} {'Valeur':<10} {'Priorite':<10} {'Destination':<15}")
        print("-" * 55)
        for c in affichees:
            print(f"{c.id:<8} {c.poids:<10.1f} {c.valeur:<10.1f} {c.priorite:<10} {c.destination:<15}")
        if total > limite:
            print(f"... ({total - limite} autres colis non affiches sur un total de {total})")

    def statistiques(self):
        n = len(self.colis_liste)
        p_tot = sum(c.poids for c in self.colis_liste)
        v_tot = sum(c.valeur for c in self.colis_liste)
        return {"total": n, "poids_total": p_tot, "valeur_totale": v_tot, "poids_moyen": (p_tot / n) if n else 0,"valeur_moyenne": (v_tot / n) if n else 0}

    def afficher_selon_poids(self, decroissant=False):
        print(f"\n--- Colis tries par poids ({'decroissant' if decroissant else 'croissant'}) ---")
        self.afficher(self.trier_par("poids", decroissant))

    def afficher_selon_valeur(self, decroissant=True):
        print(f"\n--- Colis tries par valeur ({'decroissant' if decroissant else 'croissant'}) ---")
        self.afficher(self.trier_par("valeur", decroissant))

    def afficher_selon_priorite(self, decroissant=True):
        print(f"\n--- Colis tries par priorite ({'decroissant' if decroissant else 'croissant'}) ---")
        self.afficher(self.trier_par("priorite", decroissant))

    def preparer_camion(self, capacite_max, avec_priorite=True):
        charges, p_tot, v_tot = chargement_glouton(self.colis_liste, capacite_max, avec_priorite)
        self.dernier_chargement = (charges, p_tot, v_tot, capacite_max)
        return self.dernier_chargement

    def afficher_chargement(self, chargement=None):
        donnees = chargement or self.dernier_chargement
        if not donnees:
            print("Aucun camion n'a ete prepare.")
            return

        charges, p_tot, v_tot, cap_max = donnees
        print(f"\n=== Chargement Camion (Capacite: {cap_max} kg) ===")
        self.afficher(charges)
        print("-" * 55)
        print(f"Total charges : {len(charges)} colis | Poids : {p_tot:.1f}/{cap_max} kg | Valeur : {v_tot:.1f}")
