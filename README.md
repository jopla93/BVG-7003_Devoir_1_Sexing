###Note: Je n'avais jamais utilisé python de ma vie et je voulais essayer quelque chose de différent de R. J'ai donc refait l'analyse qu'on avait fait en classe, mais avec python. C'est pourquoi mon code est probablement structuré étrangement.


Cas d'utilisation :
Le script contient différentes fonctions. Celles-ci permettent de :
 
1. Importer des données à partir d'un fichier .csv qui contient des données d'expression de gènes normalisés de plantes
	
2. Filtrer les données afin de produire des tableaux selon les gènes sélectionnés. Dans le script, les tableaux réalisés permettent de filtrer les gènes REM16 et FT1 selon leur numéro d'identifiant en fonction de leur sexe. 1 tableau est produit avec le gène REM16 filtré, 1 autre avec le gène FT1 filtré et un troisième tableau qui contient les données pour les 2 gènes.

3. Faire les figures de l'expression des gènes d'intérêt en fonction du sexe des plants. Trois boxplots sont produit: un pour l'expression du gène REM16 en fonction du sexe, un pour l'expression du gène FT1 en fonction du sexe et un dernier qui donne l'expression des gènes REM16 et FT1 en fonction du sexe des plants.

4. Sauvegarder les figures dans le répertoire courant selon la décision de l'utilisateur

5. Faire le sexing à partir de données d'expression normalisées brutes. La fonction produit un fichier excel qui permet directement de sexer les plants en utilisant l'expression du gène REM16. Le gène FT1 est utilisé comme gène de référence pour le contrôle de qualité de l'expérience.

6. Sauvegarder le fichier excel dans le répertoire courant selon la décision de l'utilisateur

7. Indiquer le nombre de plants mâles et le nombre de plants femelles où le contrôle est positif et indiquer combien de cas où le contrôle est négatif.

Données d'entrée : 

Le fichier d'entrée est un fichier excel de données transcriptomiques normalisées avec des "," comme séparateur entre les colonnes. La première colonne du tableau contient les identifiants (ID) des gènes. La première ligne du tableau contient les identifiants (num) des plantes suivi de leur sexe (XX ou XY) dans le format suivant: num_XX pour un plant femelle ou num_XY pour un plant mâle. Chaque colonne correspond donc à l plant et ses données transcriptomiques pour chacun des gènes. Pour les fonctions qui permettent de faire le sexing (5 et 6), le fichier d'entrée n'a pas besoin d'avoir des plantes dont le sexe est déjà déterminé. Seul un identifiant de plante (num) doit être présent dans la première ligne du fichier.


Résultats : 

###Note: Tous les résultats décrits sont générés avec le fichier nommé "2_Data_RNASeq_Cannabis_Sex" présent dans le répertoire data/ du GitHub###

(2.1) Les données filtrées avec le gène REM16 donnent un tableau de 138 lignes x 5 colonnes, qui donnent le gène (REM16), l'ID, l'expression, le sexe et la combinaison du gène et du sexe pour tous les plants. Le tableau est nommé data_REM16 dans le script.

(2.2) Les données filtrées avec le gène FT1 donnent un tableau de 138 lignes x 5 colonnes, qui donnent le gène (FT1), l'ID, l'expression, le sexe et la combinaison du gène et du sexe pour tous les plants. Le tableau est nommé data_FT1 dans le script.

(2.3) Les données filtrées avec les gènes FT1 et REM16 donnent un tableau de 276 lignes x 5 colonnes, qui donnent le gène (FT1 ou REM16), l'ID, l'expression, le sexe et la combinaison du gène et du sexe pour tous les plants. Le tableau est nommé data_filtered dans le script.

(3.1) fig1 : Les résultats du graphique de l'expression de REM16 en fonction du sexe montre une différence de l'expression du gène entre les plants mâles et les plants  femelles. Au delà d'une expression normalisée de 9,6 pour ce gène, il apparaît sur le graphique généré que les plants sont femelle et en bas du seuil, les plants sont mâles.

(3.2) fig2 : La figure du graphique de l'expression de FT1 en fonction du sexe montre que son expression est stable entre les plants indépendamment du sexe. Les niveaux d'expression normalisés sont plus grands que 5 dans tous les cas et ne varient pas différemment en fonction du sexe des plants.

(3.3) fig3 : La figure du graphique de l'expression de FT1 et REM16 en fonction du sexe montre que les niveaux d'expression de FT1 ne diffèrent pas entre le sexe des plants. De plus, les niveaux d'expression de REM16 sont plus élevés que ceux de FT1 pour les plants mâles et les plants femelles. Enfin, les niveaux d'expression de REM16 sont plus élevés dans les plants femelles que les plants mâles.

(5) Le dataframe nommé sexing_df donne un tableau de 138 lignes x 3 colonnes, qui donnent l'identifiant du plant, le sexe et le contrôle. Les résultats montrent que le gène de référence utilisé démontre qu'il n'y a pas de problème majeur avec l'expérience, car un + est présent dans toutes les cases du tableau. Pour la colonne sexe, on peut voir qu'il correspond avec le sexe identifié pour tous les plants, ce qui démontre que la fonction de sexing fonctionne pour ce jeu de donnée.

(6) Le résultat du sexing est affiché dans le terminal, indiquant qu'il y a 69 mâles, 69 femelles et 0 échantillons non confirmés.


Instructions pour l'utilisation du script avec le fichier "2_Data_RNASeq_Cannabis_Sex" :
	
Ce projet contient un script Python qui utilise les dépendances pandas, os, matplotlib, et seaborn.
Prérequis: Python 3.6 ou plus récent
Les répertoires du projet sont trouvés à cette adresse: 
	
	https://github.com/jopla93/BVG_7003_Devoir_1_Sexing.git


0.  ###Cette étape est utile si vous devez installer les dépendances###
Copier ces commandes dans le terminal pour créer un environnement dans lequel les dépendances peuvent être installées : 

		python3 -m venv requirements_sexing
		source requirements_sexing/bin/activate
		pip install pandas matplotlib seaborn numpy


1. Faire un clone du git avec la commande :  git clone https://github.com/jopla93/BVG-7003_Devoir_1_Sexing.git
		

2. Déplacez vous dans le répertoire où vous avez cloné le github: 
		
	cd /chemin/du/github/BVG-7003_Devoir_1_Sexing    #(Changer le chemin pour celui de votre choix si vous changez de fichié analysé)

###Noter que la commande de l'étape suivante téléchargera automatiquement les figures et les résultats du sexing directement dans le répertoire désigné###

3. Exécuter le script Plamondon_Joelle_Devoir1.py présent dans le dossier Script/ avec la commande :

		python3 Script/Plamondon_Joelle_Devoir1.py # La commande doit être effectuée à partir du répertoire du clone github : BVG-7003_Devoir_1_Sexing.git/

Le script demande pour chaque figure et tableau si vous voulez le télécharger. Si oui, les fichiers seront téléchargés dans le répertoire courant et son chemin d'accès vous sera indiqué. Sinon, le téléchargement de la figure sera annulé. La question est demandée pour tous les fichiers (4).

En répondant "yes" pour tout, vous obtiendrez dans le répertoire courant: 
# 3 images .png qui correspondent aux figures d'expression des gènes REM16 et FT1 en fonction du sexe

# 1 fichier .csv qui contient les résultats du sexing

Dans le terminal s'affichent les 5 premières lignes et les 5 dernières lignes des dataframes utilisés pour les figures et le sexing

4. Vous pouvez changer les fichiers d'emplacement si vous le désirez avec le code suivant en spécifiant le chemin que vous voulez.
   
		mv FT1_expression.png FT1_REM16_expression.png REM16_expression.png sexing_cannabis.csv /chemin/que/vous/voulez

Pour les résultats du sexing à partir des données brutes, voici comment les interpréter: 
Le dataframe nommé sexing_df donne un tableau qui donne l'identifiant du plant, le sexe et le contrôle. Le sexe est déterminé en fonction du seuil de 9,6 pour l'expression de REM16. La colonne "Sexe" indique "F" si les résultats de l'expression de REM16 correspondent à ceux d'un plant femelle et "M" si les résultats de l'expression de REM15 correspondent à ceux d'un plant mâle.
Le contrôle est déterminé par l'expression de FT1, qui est le gène de référence pour le contrôle de qualité de l'expérience. Lorsque son expression est plus grande ou égale à 5 et plus petite ou égale à 8,5 il est indiqué "+" dans la colonne contrôle, ce qui veut dire que le gène de référence s'est exprimé normalement dans l'expérience. Si le gène FT1 a une expression en bas de 5 ou plus grande que 8,5, la colonne contrôle indique "-", ce qui signifie qu'il y a potentiellement un problème au niveau de l'expérience pour les niveaux d'expression du plant donné.
Le résultat de la fonction du sexing affiche dans le terminal le nombre de plants qui ont été identifiés soit femelles ou males lorsque le contrôle est positif. Les résultats d'expression où le contrôle est négatif sont comptabilisés et est indiqué dans le terminal en tant qu'échantillons non confirmés.
