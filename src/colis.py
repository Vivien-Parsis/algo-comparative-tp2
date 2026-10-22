class Colis:
    def __init__(self, id_colis, poids, valeur, priorite, destination):
        self.id = id_colis
        self.poids = float(poids)
        self.valeur = float(valeur)
        self.priorite = int(priorite)
        self.destination = str(destination)

    def __repr__(self):
        return f"Colis(id={self.id}, poids={self.poids}, valeur={self.valeur}, priorite={self.priorite}, dest='{self.destination}')"
