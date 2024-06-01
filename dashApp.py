import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.express as px
import seaborn as sns
from bokeh.core.properties import value
from bokeh.io import curdoc
from bokeh.layouts import column, row
from bokeh.models import (
    BasicTicker,
    ColorBar,
    ColumnDataSource,
    HoverTool,
    LabelSet,
    LinearColorMapper,
    Panel,
    Select,
)
from bokeh.palettes import Spectral6, Spectral11, Viridis256
from bokeh.plotting import figure, output_file, output_notebook, show
from bokeh.transform import factor_cmap, transform

df = pd.read_csv("AvitoCarDataset_ready2Viz.csv")

def km_moy(df):
    #kilométrage moyen par marque
    kilometrage_moyen_par_marque = df.groupby('Marque')['Kilometrage'].mean().reset_index()
    source = ColumnDataSource(data=dict(Marque=kilometrage_moyen_par_marque['Marque'],Kilometrage=kilometrage_moyen_par_marque['Kilometrage']))
    p1 = figure(x_range=kilometrage_moyen_par_marque['Marque'], height=400, width=600, title="Kilométrage Moyen par Marque", toolbar_location=None, tools="")
    p1.vbar(x='Marque', top='Kilometrage', width=0.9, source=source, color='skyblue')
    #étiquettes des axes
    p1.xaxis.axis_label = "Marque"
    p1.yaxis.axis_label = "Kilométrage moyen"
    p1.xaxis.major_label_orientation = 1.0
    p1.xaxis.major_label_text_font_size = "10pt"
    #curseur interacgtif
    hover = HoverTool()
    hover.tooltips = [("Marque", "@Marque"), ("Kilométrage moyen", "@Kilometrage{0.0}")]
    p1.add_tools(hover)
    return p1

def prix_moy(df):
    # Calculer le prix moyen par marque
    prix_moyen_par_marque = df.groupby('Marque')['Prix'].mean().reset_index()
    # Créer une source de données ColumnDataSource
    source = ColumnDataSource(data=dict(Marque=prix_moyen_par_marque['Marque'], Prix=prix_moyen_par_marque['Prix']))
    # Créer la figure
    p2 = figure(x_range=prix_moyen_par_marque['Marque'], height=350, width=600, title="Chiffres de ventes moyen par Marque", toolbar_location=None, tools="")
    # Ajouter les barres verticales pour représenter le prix moyen par marque
    p2.vbar(x='Marque', top='Prix', width=0.9, source=source, color='orange')
    # Ajouter les étiquettes des axes
    p2.xaxis.axis_label = "Marque"
    p2.yaxis.axis_label = "Prix moyen"
    p2.xaxis.major_label_orientation = 1.0
    p2.xaxis.major_label_text_font_size = "10pt"
    # Ajouter des outils de survol interactifs pour afficher les détails
    hover = HoverTool()
    hover.tooltips = [("Marque", "@Marque"), ("Prix moyen", "@Prix{0.0}")]
    p2.add_tools(hover)
    # Afficher le graphique
    return p2


def marque_freq_ville(df):
    # Liste des villes principales
    villes_principales = ["Casablanca","Rabat","Marrakech","Fès","Tanger","Agadir","Salé","Meknès","Kénitra","Tétouan","Safi","Mohammedia","Khouribga","Béni Mellal","Nador"]
    # Filtrer le DataFrame pour inclure uniquement les villes principales
    df = df[df['Ville'].isin(villes_principales)]
    # Obtenir la marque la plus fréquente et son nombre d'occurrences pour chaque ville
    marque_plus_frequente_par_ville = df.groupby('Ville')['Marque'].agg(lambda x: x.value_counts().idxmax()).reset_index()
    occurrences_marque_plus_frequente = df.groupby('Ville')['Marque'].agg(lambda x: x.value_counts().max()).reset_index()
    # Créer la source de données ColumnDataSource
    source = ColumnDataSource(data=dict(Ville=marque_plus_frequente_par_ville['Ville'], Marque=marque_plus_frequente_par_ville['Marque'],Occurrences=occurrences_marque_plus_frequente['Marque']))
    # Créer la figure
    p3 = figure(y_range=villes_principales, height=350, width=650, title="Nombre d'occurrences de la marque la plus fréquente par ville", toolbar_location=None, tools="")
    # Créer les barres horizontales
    p3.hbar(y='Ville', right='Occurrences', height=0.9, source=source, color='skyblue')
    # Étiquettes des axes
    p3.xaxis.axis_label = "Nombre d'occurrences"
    p3.yaxis.axis_label = "Ville"
    # Outil de survol pour afficher les informations
    hover = HoverTool()
    hover.tooltips = [("Ville", "@Ville"), ("Marque", "@Marque"), ("Occurrences", "@Occurrences")]
    p3.add_tools(hover)
    # Afficher le graphique
    return p3

def occ_etats(df):
    # Calculer le nombre d'occurrences de chaque état groupé par la marque
    occurrence_etats = df.groupby(['Marque', 'État']).size().unstack(fill_value=0)
    # Créer une source de données ColumnDataSource
    source = ColumnDataSource(occurrence_etats)
    marques = occurrence_etats.index.tolist()
    # Créer la figure avec la liste des marques comme plage sur l'axe y
    p4 = figure(y_range=marques, height=400, width=750, title="Répartition des États par Marque",toolbar_location=None, tools="")
    # Ajouter les barres empilées pour chaque état
    p4.hbar_stack(stackers=['Bon', 'Très Bon', 'Excellent'], y='Marque', height=0.9, color=['lightblue', 'deepskyblue', 'dodgerblue'],source=source, legend_label=['Bon', 'Très Bon', 'Excellent'])
    # Ajouter les étiquettes des axes
    p4.yaxis.axis_label = "Marque"
    p4.xaxis.axis_label = "Fréquence"
    p4.yaxis.major_label_orientation = 0.0
    p4.yaxis.major_label_text_font_size = "10pt"
    # Ajouter des outils de survol interactifs pour afficher les détails
    hover = HoverTool()
    hover.tooltips = [("Marque", "@Marque"), ("Bon", "@Bon"), ("Très Bon", "@{Très Bon}"), ("Excellent", "@Excellent")]
    p4.add_tools(hover)
    # Afficher le graphique
    return p4


def carburant_by_marque(df):
    output_file("carburant_counts.html")
    # Préparation des données
    carburant_counts = df.groupby(['Marque', 'Type de carburant']).size().unstack().fillna(0)
    # Création du graphique
    brands = list(carburant_counts.index)
    carburants = list(carburant_counts.columns)
    data = { 'Marque': brands }
    data.update({ carburant: list(carburant_counts[carburant]) for carburant in carburants })
    source = ColumnDataSource(data=data)
    p5 = figure(x_range=brands, height=350, width=700, title="Répartition des types de carburant par marque", toolbar_location=None, tools="")
    renderers = p5.vbar_stack(carburants, x='Marque', width=0.9, color=Spectral6[:len(carburants)], source=source,legend_label=[str(x) for x in carburants])
    p5.y_range.start = 0
    p5.xgrid.grid_line_color = None
    p5.axis.minor_tick_line_color = None
    p5.outline_line_color = None
    p5.legend.location = "top_left"
    p5.legend.orientation = "horizontal"
    # Rotation et ajustement de la taille des étiquettes de l'axe des abscisses
    p5.xaxis.major_label_orientation = 1  # Rotation à 45 degrés
    p5.xaxis.major_label_text_font_size = "10pt"  # Taille de police des étiquettes
    hover = HoverTool(tooltips=[("Marque", "@Marque"),("Type de carburant", "$name"),("Valeur", "@$name")])
    p5.add_tools(hover)
    return p5



def heatmap_bv(df):
    output_file("heatmap_boite_vitess.html")
    top_cities = df['Ville'].value_counts().index[:20]  # Par exemple, les 20 villes avec le plus d'entrées
    filtered_data = df[df['Ville'].isin(top_cities)]
    # Préparation des données filtrées
    pivot = filtered_data.pivot_table(index='Ville', columns='Boite de vitesses', values='Prix', aggfunc='mean').fillna(0)
    pivot = pivot[['Automatique', 'Manuelle']]  # Inclure uniquement les colonnes valides
    pivot = pivot.stack().rename("Prix").reset_index()
    # Création du heatmap
    mapper = LinearColorMapper(palette=Viridis256, low=pivot['Prix'].min(), high=pivot['Prix'].max())
    p6 = figure(title="Heatmap de la boîte de vitesses par ville et prix (Top 20 villes)", x_range=['Automatique', 'Manuelle'], y_range=list(pivot['Ville'].unique()), x_axis_location="above", width = 600, height = 500, tools="hover,save,pan,box_zoom,reset")
    p6.rect(x="Boite de vitesses", y="Ville", width=1, height=1, source=ColumnDataSource(pivot), line_color=None, fill_color=transform('Prix', mapper))
    color_bar = ColorBar(color_mapper=mapper, location=(0, 0), ticker=BasicTicker())
    p6.add_layout(color_bar, 'right')
    # Améliorer la lisibilité des étiquettes
    p6.xaxis.major_label_orientation = 0  # Rotation des étiquettes de l'axe des x
    p6.yaxis.major_label_text_font_size = "10pt"  # Taille de police des étiquettes de l'axe y
    # Ajouter des info-bulles
    hover = HoverTool(tooltips=[("Ville", "@Ville"),("Boîte de vitesses", "@{Boite de vitesses}"),("Prix moyen", "@Prix{0,0}")])
    p6.add_tools(hover)
    return p6

def security_heatmap(df):
    # Préparation des données
    securite_columns = ['ABS', 'ESP', 'Airbags']
    securite_counts = df.groupby(['Marque'])[securite_columns].sum()
    # Transformation des données pour Bokeh
    securite_counts = securite_counts.stack().rename("count").reset_index()
    securite_counts.columns = ['Marque', 'Système de sécurité', 'count']
    # Création du heatmap
    mapper = LinearColorMapper(palette=Viridis256, low=securite_counts['count'].min(), high=securite_counts['count'].max())
    p7 = figure(title="Heatmap des systèmes de sécurité par marque", x_range=securite_columns, y_range=list(securite_counts['Marque'].unique()), x_axis_location="above", width = 600, height = 500, tools="hover,save,pan,box_zoom,reset")
    p7.rect(x="Système de sécurité", y="Marque", width=1, height=1, source=ColumnDataSource(securite_counts),line_color=None, fill_color=transform('count', mapper))
    color_bar = ColorBar(color_mapper=mapper, location=(0, 0), ticker=BasicTicker())
    p7.add_layout(color_bar, 'right')
    # Ajouter des info-bulles
    hover = HoverTool(tooltips=[("Marque", "@Marque"),("Système de sécurité", "@{Système de sécurité}"),("Count", "@count")])
    p7.add_tools(hover)
    return p7

def scatter_plot(df):
    source = ColumnDataSource(df)
    p8 = figure(title="Puissance fiscale par année modèle", width=600, height=400, x_axis_label='Année-Modèle', y_axis_label='Puissance fiscale', tools="pan,wheel_zoom,box_zoom,reset")
    p8.scatter(x='Année-Modèle', y='Puissance fiscale', source=source, size=7, color="navy", alpha=0.5)
    return p8




kilom_Moy = km_moy(df)
car_mean_price = prix_moy(df)
villeMarque_freq = marque_freq_ville(df)
car_etats_occ = occ_etats(df)
carb_marque = carburant_by_marque(df)
bv_heatmap = heatmap_bv(df)
sec_heatmap = security_heatmap(df)
scatter_plot_p= scatter_plot(df)

# Combiner les visualisations dans une seule mise en page
layout1=row(kilom_Moy,car_etats_occ) 
layout2=row(car_mean_price, villeMarque_freq) 
layout3=row(carb_marque, scatter_plot_p) 
layout4=row(bv_heatmap, sec_heatmap)

layout5 = column(layout1,layout2)
layout6 = column(layout3,layout4)
final_layout=column(layout5, layout6)
# Afficher l'application dans le notebook
show(final_layout)
