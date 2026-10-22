# Projet : Gestion et Optimisation du Chargement de Camions

Ce projet propose un système de gestion de colis et d'optimisation de chargement de camions, conçu pour passer à l'échelle jusqu'à 100 000 colis.

## Structure du projet

```text
algo-comparative-tp2/
├── src/
│   ├── colis.py         # Modélisation de l'entité Colis
│   ├── gestionnaire.py  # Structure de données hybride (dict + list)
│   ├── tri.py           # Algorithme de tri fusion stable O(n log n)
│   ├── camion.py        # Algorithme glouton avec calcul de score
│   ├── benchmark.py     # Mesures de performances (100 à 100 000 colis)
│   └── main.py          # Interface interactive en ligne de commande (CLI)
├── rapport.md           # Rapport d'analyse et justifications algorithmiques
└── README.md            # Documentation et instructions d'exécution
```

## Exécution

Depuis la racine du projet (`algo-comparative-tp2/`) :

### Lancer l'application interactive

```bash
python src/main.py
```

### Lancer le benchmark de performance

```bash
python src/benchmark.py
```
