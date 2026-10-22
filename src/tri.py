def tri_fusion(elements, key=lambda x: x, reverse=False):
    if len(elements) <= 1:
        return list(elements)

    milieu = len(elements) // 2
    gauche = tri_fusion(elements[:milieu], key, reverse)
    droite = tri_fusion(elements[milieu:], key, reverse)

    return _fusionner(gauche, droite, key, reverse)

def _fusionner(gauche, droite, key, reverse):
    resultat = []
    i = j = 0
    n_g, n_d = len(gauche), len(droite)

    while i < n_g and j < n_d:
        cond = (key(gauche[i]) >= key(droite[j])) if reverse else (key(gauche[i]) <= key(droite[j]))
        if cond:
            resultat.append(gauche[i])
            i += 1
        else:
            resultat.append(droite[j])
            j += 1

    resultat.extend(gauche[i:])
    resultat.extend(droite[j:])
    return resultat
