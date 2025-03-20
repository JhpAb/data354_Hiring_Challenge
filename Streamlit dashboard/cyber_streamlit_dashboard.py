import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')
import seaborn as sns
from wordcloud import WordCloud

# Charger les fichiers CSV
df = pd.read_csv('D:/cyber_security_ai_tools.csv')  # Tableau des publications
top_10_authors_df_sorted = pd.read_csv('D:/top_10_authors_df_sorted.csv')  # Tableau des auteurs

# Titre du dashboard
st.title("📊 LinkedIn Post Analysis Dashboard")

# Sidebar de navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Aller à", ["📈 Statistiques générales", "🏆 Analyse des auteurs", "🔍 Analyse des mots-clés"])

if page == "📈 Statistiques générales":
    st.header("📊 Statistiques générales")

    # Affichage du tableau cyber_security_ai_tools.csv
    st.subheader("Tableau des données : cyber_security_ai_tools.csv")
    st.dataframe(df)

    # Nombre total de publications
    st.metric(label="Total des publications", value=len(df))

    # Nombre d'auteurs uniques
    st.metric(label="Nombre d'auteurs uniques", value=df['Author'].nunique())

    # Graphique des auteurs uniques
    st.subheader("Nombre de publications par auteur")
    author_counts = df['Author'].value_counts().head(30)  # Limiter à 30 pour lisibilité
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(x=author_counts.index, y=author_counts.values, palette="coolwarm", ax=ax)
    plt.xticks(rotation=90)
    plt.xlabel("Auteurs")
    plt.ylabel("Nombre de publications")
    plt.title("Top 30 des auteurs par nombre de publications")
    st.pyplot(fig)

elif page == "🏆 Analyse des auteurs":
    st.header("🏆 Top 10 Auteurs")

    # Affichage du tableau top_10_authors_df_sorted.csv
    st.subheader("Tableau des données : top_10_authors_df_sorted.csv")
    st.dataframe(top_10_authors_df_sorted)

    # Top 10 auteurs
    st.subheader("Auteurs avec le plus de publications")
    author_counts = top_10_authors_df_sorted['Author'].value_counts().head(10)

    # Créer le graphique avec une taille ajustée
    fig, ax = plt.subplots(figsize=(12, 6))  # Augmenter la taille du graphique
    sns.barplot(x=author_counts.values, y=author_counts.index, palette="Blues_r", ax=ax)  # Inverser x et y

    # Redresser les étiquettes
    plt.xticks(rotation=0)  # Garder les étiquettes horizontales
    plt.xlabel("Nombre de publications")
    plt.ylabel("Auteurs")
    plt.title("Top 10 des auteurs avec le plus de publications")

    # Afficher le graphique
    st.pyplot(fig)

    # Analyse des Likes et Shares
    st.subheader("Likes et Shares des Top 10 Auteurs")
    col1, col2 = st.columns(2)
    
    # Graphique Likes
    with col1:
        fig, ax = plt.subplots(figsize=(12, 6))
        sns.barplot(x='Likes', y='Author', data=top_10_authors_df_sorted, palette='viridis', ax=ax)
        plt.xticks(rotation=0)
        plt.xlabel("Likes")
        plt.ylabel("Auteurs")
        plt.title("Likes des Top 10 Auteurs")
        st.pyplot(fig)

    # Graphique Shares
    with col2:
        fig, ax = plt.subplots(figsize=(12, 6))
        sns.barplot(x='Shares', y='Author', data=top_10_authors_df_sorted, palette='magma', ax=ax)
        plt.xticks(rotation=45)
        plt.xlabel("Shares")
        plt.ylabel("Auteurs")
        plt.title("Shares des Top 10 Auteurs")
        st.pyplot(fig)

    # Corrélation entre Likes et Shares
    st.subheader("📊 Corrélation entre Likes et Shares")
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.scatterplot(x='Likes', y='Shares', data=top_10_authors_df_sorted, color='purple', ax=ax)
    plt.xlabel("Likes")
    plt.ylabel("Shares")
    plt.title("Corrélation entre Likes et Shares")
    st.pyplot(fig)
    correlation = top_10_authors_df_sorted['Likes'].corr(top_10_authors_df_sorted['Shares'])
    st.write(f"Coefficient de corrélation : **{correlation:.2f}**")

    # Nouveau graphique : Top 10 des auteurs uniques par mot-clé
    st.subheader("📚 Top 10 des auteurs par mots-clés")

    # Groupement par Auteur et Mots-clés, puis comptage du nombre de publications
    author_keyword_counts = df.groupby(['Author', 'Keywords'])['Author'].count().unstack().fillna(0)

    # Récupérer les 10 auteurs les plus actifs en fonction du nombre total de publications
    top_10_authors = author_keyword_counts.sum(axis=1).sort_values(ascending=False).head(10).index

    # Filtrer le DataFrame pour ne garder que les 10 auteurs
    top_author_keyword_counts = author_keyword_counts.loc[top_10_authors]

    # Créer le graphique en barre
    fig, ax = plt.subplots(figsize=(15, 8))
    top_author_keyword_counts.plot(kind='bar', stacked=True, ax=ax)
    plt.title('Top 10 des Auteurs Uniques par Mot-clés')
    plt.xlabel('Auteurs')
    plt.ylabel('Nombre de Publications')
    plt.xticks(rotation=45, ha='right')
    plt.legend(title='Mots-clés', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()

    # Afficher le graphique
    st.pyplot(fig)


elif page == "🔍 Analyse des mots-clés":
    st.header("🔍 Analyse des mots-clés")

    # Affichage du tableau top_10_authors_df_sorted.csv (car il contient les mots-clés)
    st.subheader("Tableau des données : top_10_authors_df_sorted.csv")
    st.dataframe(top_10_authors_df_sorted)

    # Nuage de mots des mots-clés
    st.subheader("WordCloud des mots-clés")
    text = " ".join(top_10_authors_df_sorted['Keywords'].dropna().astype(str))
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis("off")
    plt.title("Nuage de mots des mots-clés")
    st.pyplot(fig)

    # Nuage de mots du contenu des posts
    st.subheader("WordCloud du contenu des publications")
    text_content = " ".join(top_10_authors_df_sorted['Content'].dropna().astype(str))
    wordcloud_content = WordCloud(width=800, height=400, background_color='white').generate(text_content)
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wordcloud_content, interpolation='bilinear')
    ax.axis("off")
    plt.title("Nuage de mots du contenu des publications")
    st.pyplot(fig)


st.sidebar.info("👈 Sélectionnez une section pour explorer les données !")
