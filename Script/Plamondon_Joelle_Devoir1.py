#workflow pour le sexing des plants de cannabis lorsqu'on a des donnees normalises d'expression
#utilise les genes REM16 et FT1 identifiés LOC115699937 et LOC115696989 respectivement
#Recquiert l'installation de pandas, matplotlib, numpy et seaborn

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


file_path = "Data/2_Data_RNASeq_Cannabis_Sex.csv" # définition du chemin du fichier .csv dans le clone git. Changer le chemin et/ou le nom du fichier ici au besoin
data = pd.read_csv(file_path) #variable data assignée au fichier .csv

# fonction pour filtrer les données
def filter_data():
    """Filtre les données pour ne garder que les lignes correspondant aux identifiants du sexing"""
    id = ['LOC115699937', 'LOC115696989']  # Liste des identifiants à filtrer. Si on veut analyser d'autres gènes, il faudrait changer les ID ici

    # Filtrer les lignes dont l'identifiant est dans la première colonne (index 0)
    data_filtered = data[data['Unnamed: 0'].isin(id)].copy()

    # Remplacer les identifiants par les nouveaux noms
    data_filtered['Unnamed: 0'] = data_filtered['Unnamed: 0'].replace({
        'LOC115699937': 'REM16',
        'LOC115696989': 'FT1'
        }) # si on veut analyser d'autres gènes, il faudrait changer l'ID et le nom commun auquel il est associé (= nom assigné)
    data_filtered = data_filtered.rename(columns={'Unnamed: 0': 'Gene'}) #modifie le nom de la colonne 1 pour gene
    data_filtered = data_filtered.melt(id_vars=['Gene'],
                                   var_name='ID',
                                   value_name='Expression') # pivote le tableau pour qu'il soit plus long que large
    data_filtered['Sexe'] = data_filtered['ID'].apply(
        lambda x: 'female' if 'XX' in x else ('male' if 'XY' in x else 'Other')) #Ajoute une colonne femelle/male si XX ou XY est present
    data_filtered['Gene_Sexe'] = data_filtered['Gene'] + '_' + data_filtered['Sexe'] #Ajoute une colonne pour associer l'expression du gene au sexe

    data_REM16 = data_filtered[data_filtered['Gene'] == 'REM16'] #si on analyse d'autres gènes, il faut changer les noms assignés ici
    data_FT1 = data_filtered[data_filtered['Gene'] == 'FT1'] # si on analyse d'autres gènes, il faut changer les noms  assignés ici
    return data_REM16, data_FT1, data_filtered

data_REM16, data_FT1, data_filtered = filter_data() # Appel de la fonction filter_data pour obtenir les données filtrées
print(data_REM16, data_FT1, data_filtered) #Affiche les dataFrames. Attention aux noms des dataframes.

def save_graph(fig, filename):
    plt.show()
    save = input(f"Voulez-vous enregistrer le graphique sous le nom '{filename}' ? (y/n): ")
    if save.lower() != 'y':
        print("Le téléchargement a été annulé.") #annule le telechargement si la reponse n'est pas y
        plt.close(fig)
        return
    if os.path.exists(filename): #verifie si le fichier existe deja
        overwrite = input(f"Le fichier '{filename}' existe déjà. Voulez-vous l'écraser ? (y/n): ") # ecrase un fichier qui porte meme nom si reponse = y
        if overwrite.lower() != 'y':
            print("Le téléchargement a été annulé.")
            plt.close(fig)
            return
    fig.savefig(filename) #sauvegarde le fichier avec le nom specifié pour filename
    file_path = os.path.abspath(filename)
    print(f"Le graphique a été enregistré sous le nom '{filename}'. Vous pouvez le trouver ici : {file_path}") #donne l'emplacement du telechargement
    plt.close(fig)

def figure(df_REM16, df_FT1, df_filtered):
    palette = {'FT1': 'blue', 'REM16': 'orange', 'REM16_female' : 'orange', 'REM16_male': 'orange', 'FT1_female': 'blue', 'FT1_male': 'blue'}
    # Graphique pour REM16
    fig1=plt.figure() #crée la nouvelle figure nommée fig1
    g1=sns.boxplot(data=data_REM16, x='Gene_Sexe', y='Expression', hue='Gene', # cree le box plot. Si on a changé les noms des gènes, il faut changer le nom du dataframe
                   width=0.3,  # Réduit la largeur du boxplot
                   showcaps=False,  # Supprime les caps aux extrémités des moustaches
                   whiskerprops={'linewidth': 1},
                   palette=palette)  # Ajuste l'épaisseur des moustaches
    g1.set_xlabel('Sexe des plants de cannabis') #nom de l'axe x. Changer le nom au besoin
    g1.set_ylabel('Niveaux d\'expression normalisé') # nom de l'axe y
    g1.set_title('Niveaux d\'expression de REM16 selon le sexe') # titre du graph. Changer le nom au besoin
    legend = g1.get_legend()
    if legend is not None:
        legend.remove()
    plt.show() #ouvre le graph pour le montrer
    save_graph(fig1, 'REM16_expression.png') #appel de la fonction pour sauvegarder le graph. Pour changer le nom du fichier, changer 'REM16_expression.png' pour 'nom_de_fichier.png'

    ''' Répétition du code pour la création des 3 graphiques. Les lignes de codes font la même chose pour les 3 graphiques. Seuls les data et les noms des axes changent '''

    # Graphique pour FT1
    fig2=plt.figure()
    g2=sns.boxplot(data=data_FT1, x='Gene_Sexe', y='Expression', hue='Gene', width = 0.3, showcaps = False, whiskerprops = {'linewidth': 1}, palette=palette) #attention au nom du dataframe
    g2.set_xlabel('Sexe des plants de cannabis')
    g2.set_ylabel('Niveaux d\'expression')
    g2.set_title('Niveaux d\'expression pour FT1 selon le sexe')
    legend = g2.get_legend()
    if legend is not None:
        legend.remove()
    plt.show()
    save_graph(fig2, 'FT1_expression.png') #Pour changer le nom du fichier, changer 'FT1_expression.png' pour 'nom_de_fichier.png'

    # Graphique des deux genes selon le sexe
    fig3=plt.figure()
    g3=sns.boxplot(data=data_filtered, x='Gene_Sexe', y='Expression', hue='Gene', width = 0.3, showcaps = False, whiskerprops = {'linewidth': 1}, palette=palette) #attention au nom du dataframe
    g3.set_xlabel('Gène et sexe des plants de cannabis')
    g3.set_ylabel('Niveaux d\'expression')
    g3.set_title('Niveaux d\'expression de REM16 et FT1 selon le sexe du plant')
    g3.legend(title='Gène', loc='upper right')
    plt.show()
    save_graph(fig3, 'FT1_REM16_expression.png') #Pour changer le nom du fichier, changer 'FT1_REM16_expression.png' pour 'nom_de_fichier.png'
    return g1, g2, g3

figure(data_REM16, data_FT1, data_filtered) # Appel de la fonction figure pour faire apparaître les graph. Si les

'''Fonctionne de la même manière que pour la sauvegarde des graphiques'''
def save_dataframe(df, csv_filename):
    save_csv = input(f"Voulez-vous enregistrer le DataFrame sous le nom '{csv_filename}' ? (y/n): ")
    if save_csv.lower() != 'y':
        print("Le téléchargement du DataFrame a été annulé.")
        return

    if os.path.exists(csv_filename):
        overwrite_csv = input(f"Le fichier '{csv_filename}' existe déjà. Voulez-vous l'écraser ? (y/n): ")
        if overwrite_csv.lower() != 'y':
            print("Le téléchargement du DataFrame a été annulé.")
            return

    df.to_csv(csv_filename, index=False, sep=';') #Permet d'avoir le fichier excel en sortie et de reconnaitre les colonne avec la séparation par ";". Au besoin, changer ";" par ","
    csv_file_path = os.path.abspath(csv_filename)
    print(f"Le DataFrame a été enregistré sous le nom '{csv_filename}'. Vous pouvez le trouver ici : {csv_file_path}") #Informe de l'emplacement du telechargement

'''Fonction pour sexer les plants a partir du fichier .csv brut'''
''' Le seuil d'expression de REM16 pour le sexing est déterminé a 9,6 en regardant les figures réalisés. En bas de 9,6 c'est un plant mâle et en haut, c'est un plant femelle'''
''' De la même manière, le seuil pour le controle FT1 est déterminé a 5 en regardant l'expression de FT1 dans les figures'''
def sexing(data):
    # Création d'un nouveau DataFrame pour stocker les résultats de sexing
    sexing_df = pd.DataFrame(columns=['ID', 'Sexe', 'Controle'])

    # Parcours des colonnes pour tester les valeurs
    for col in data.columns[1:]:
        # Recherche de l'ID "LOC115699937" de REM16 dans la première colonne
        value_sexe = data.loc[data['Unnamed: 0'] == 'LOC115699937', col].values[0]
        Sexe = 'F' if value_sexe >= 9.6 else 'M'

        # Recherche de l'ID "LOC115696989" de FT1 dans la première colonne
        value_control = data.loc[data['Unnamed: 0'] == 'LOC115696989', col].values[0]
        Controle = '+' if 5 <= value_control <= 8.5 else '-'

        # Ajoute les résultats au dataframe sexing_df
        sexing_df = pd.concat([sexing_df, pd.DataFrame({'ID': [col], 'Sexe': [Sexe], 'Controle': [Controle]})],
                              ignore_index=True)

    save_dataframe(sexing_df, "sexing_cannabis.csv") #sauve le data.frame
    return sexing_df

resultat = sexing(data) #Appel de la fonction sexing pour montrer le résultat du dataframe dans le terminal
print(resultat)

def sexing_results(df):
    # Compte le nombre de mâles et femelles où le contrôle est '+'
    males = resultat[(resultat['Sexe'] == 'M') & (resultat['Controle'] == '+')].shape[0]
    females = resultat[(resultat['Sexe'] == 'F') & (resultat['Controle'] == '+')].shape[0]

    # Compte le nombre d'échantillons non confirmés (contrôle '-')
    unconfirmed = resultat[resultat[('Controle')] == '-'].shape[0]

    # Imprime les résultats
    print(
        f"Sexing complete. {males} mâles ont été identifiés et {females} femelles ont été identifiées. {unconfirmed} échantillons n'ont pas été confirmés.")

sexing_results(resultat)
