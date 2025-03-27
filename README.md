# data354_Hiring_Challenge

LinkedIn Post Analysis
--

Description
--

Ce projet crée un tableau de bord interactif pour l'analyse des publications LinkedIn en utilisant des données sur les auteurs, les likes, les partages, et les mots-clés. Le tableau de bord est développé avec Streamlit, une bibliothèque Python permettant de créer des applications web interactives. Ce tableau de bord permet de :

Visualiser des statistiques générales sur les publications.

Analyser les performances des auteurs en termes de likes, partages, et nombre de publications.

Explorer la répartition des mots-clés utilisés dans les publications et leur fréquence.


Le projet se compose de plusieurs sections permettant une exploration dynamique des données, à savoir :

Statistiques générales : Affichage des données de base, du nombre de publications et des auteurs uniques.

Analyse des auteurs : Détail sur les auteurs, y compris le nombre de publications, les likes, les partages, et la corrélation entre ces deux derniers.

Analyse des mots-clés : Nuages de mots montrant les termes les plus utilisés dans les publications et leur contenu.


Technologies utilisées

Python : Langage de programmation principal.

Streamlit : Outil pour créer des applications web interactives.

Pandas : Pour la manipulation et l'analyse des données.

Matplotlib et Seaborn : Pour la visualisation des données sous forme de graphiques.

WordCloud : Pour générer des nuages de mots à partir des mots-clés et du contenu des publications.

--
Prérequis
--

Avant d'exécuter ce projet, vous devez avoir installé les bibliothèques suivantes :

pip install streamlit pandas matplotlib seaborn wordcloud

Fichiers utilisés

Le projet utilise deux fichiers CSV qui contiennent les données des publications et des auteurs :

1. cyber_security_ai_tools.csv : Ce fichier contient des informations sur les publications, y compris l'auteur, les likes, les partages et les mots-clés.


2. top_10_authors_df_sorted.csv : Ce fichier contient des informations supplémentaires sur les 10 auteurs ayant le plus de publications, y compris les likes, les partages, les mots-clés et le contenu des publications.


--
Les données de ces fichiers sont chargées depuis des URL publiques.
--
Fonctionnalités

1. 📈 Statistiques générales

Affichage du tableau des publications.

Nombre total de publications et nombre d'auteurs uniques.

Graphique des 30 auteurs ayant publié le plus grand nombre de posts.


2. 🏆 Analyse des auteurs

Affichage des top 10 auteurs par nombre de publications.

Graphiques montrant les likes et les partages des top 10 auteurs.

Analyse de la corrélation entre le nombre de likes et de partages.

Visualisation des publications des auteurs en fonction des mots-clés.


3. 🔍 Analyse des mots-clés

Nuage de mots des mots-clés les plus utilisés dans les publications des top 10 auteurs.

Nuage de mots des contenus des publications des top 10 auteurs.

--
Utilisation
--
1. Clonez ce dépôt ou téléchargez les fichiers sources sur votre machine.


2. Exécutez le fichier Streamlit pour lancer l'application dans votre navigateur :



streamlit run app.py

3. Une fois l'application lancée, vous pouvez naviguer entre les sections du tableau de bord via la barre latérale :

📈 Statistiques générales : Affiche des métriques de base et un graphique des auteurs les plus actifs.

🏆 Analyse des auteurs : Explorez les performances des auteurs et analysez la corrélation entre likes et partages.

🔍 Analyse des mots-clés : Visualisez les mots-clés populaires et le contenu des publications sous forme de nuages de mots.




Exemple de sortie

L'application fournit différents types de visualisations comme :

Barres de distribution des publications par auteur.

Graphiques de likes et de partages pour chaque auteur.

Nuages de mots représentant les mots-clés et le contenu des publications.


Ces visualisations permettent une analyse approfondie de la performance des publications sur LinkedIn.

Contact
--

Auteur : ABBE Jean Pierre, Data Analyst | CEM Engineer

Téléphone : +225 0749499034

Email : abbejeanpierre0808@gmail.com

--
Contributions
--

Les contributions sont les bienvenues ! Si vous avez des idées pour améliorer ce projet, n'hésitez pas à ouvrir une issue ou à soumettre une pull request.
