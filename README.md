# DataVizApp_laghchim-ouahjoujou

Cette application de visualisation des données utilise plusieurs bibliothèques Python, notamment Bokeh, Pandas et Matplotlib, pour analyser et visualiser des informations extraites d'un dataset Marocain de voitures provenant d'Avito. Elle présente plusieurs graphiques interactifs et informatifs permettant de mieux comprendre divers aspects des données de voitures d'occasion, telles que les marques, les prix, les kilométrages, et d'autres caractéristiques. Voici un résumé des différentes visualisations et de leur contenu:


--> Kilométrage moyen par marque
    Description : Ce graphique à barres montre le kilométrage moyen des voitures pour chaque marque.
    Axes :
    X : Marque
    Y : Kilométrage moyen
    Interactivité : Un outil de survol (hover) affiche le détail du kilométrage moyen pour chaque marque.


--> Prix moyen par marque
    Description : Ce graphique à barres représente le prix moyen des voitures pour chaque marque.
    Axes :
    X : Marque
    Y : Prix moyen
    Interactivité : Un outil de survol (hover) affiche le détail du prix moyen pour chaque marque.


--> Nombre d'occurrences de la marque la plus fréquente par ville
    Description : Ce graphique à barres horizontales indique la marque de voiture la plus fréquente pour chaque ville et le nombre d'occurrences de cette marque.
    Axes :
    X : Nombre d'occurrences
    Y : Ville
    Interactivité : Un outil de survol (hover) montre les détails de la ville, de la marque et du nombre d'occurrences.


--> Répartition des États par Marque
    Description : Ce graphique à barres empilées montre la répartition des états des voitures (Bon, Très Bon, Excellent) pour chaque marque.
    Axes :
    X : Fréquence
    Y : Marque
    Interactivité : Un outil de survol (hover) affiche le détail de chaque état par marque.


--> Répartition des types de carburant par marque
    Description : Ce graphique à barres empilées illustre la répartition des différents types de carburant (Essence, Diesel, etc.) pour chaque marque.
    Axes :
    X : Marque
    Y : Nombre de voitures
    Interactivité : Un outil de survol (hover) montre les détails du type de carburant et du nombre de voitures par marque.


--> Heatmap de la boîte de vitesses par ville et prix (Top 20 villes)
    Description : Ce heatmap montre la distribution des prix moyens des voitures en fonction de la boîte de vitesses (Automatique, Manuelle) dans les 20 villes principales.
    Axes :
    X : Boîte de vitesses
    Y : Ville
    Interactivité : Un outil de survol (hover) affiche le prix moyen pour chaque combinaison ville/boîte de vitesses.

    
--> Heatmap des systèmes de sécurité par marque
    Description : Ce heatmap présente la répartition des systèmes de sécurité (ABS, ESP, Airbags) pour chaque marque.
    Axes :
    X : Système de sécurité
    Y : Marque
    Interactivité : Un outil de survol (hover) montre le nombre de chaque système de sécurité par marque.
    
--> Puissance fiscale par année modèle
    Description : Ce graphique de dispersion (scatter plot) visualise la puissance fiscale des voitures en fonction de l'année modèle.
    Axes :
    X : Année-Modèle
    Y : Puissance fiscale
    Interactivité : L'utilisateur peut zoomer et naviguer à travers
