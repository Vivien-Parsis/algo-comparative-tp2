from tri import tri_fusion

def calcul_score(colis, avec_priorite=True):
    if colis.poids <= 0:
        return 0
    if avec_priorite:
        return (colis.valeur * colis.priorite) / colis.poids
    return colis.valeur / colis.poids

def chargement_glouton(colis_liste, capacite_max, avec_priorite=True):
    tries = tri_fusion(colis_liste, key=lambda c: calcul_score(c, avec_priorite), reverse=True)
    charges = []
    poids_total = 0.0
    valeur_totale = 0.0

    for c in tries:
        if poids_total + c.poids <= capacite_max:
            charges.append(c)
            poids_total += c.poids
            valeur_totale += c.valeur

    return charges, poids_total, valeur_totale
