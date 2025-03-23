# 📦 Importation des bibliothèques nécessaires
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')  # Style des graphiques
import seaborn as sns
from wordcloud import WordCloud

# 🔗 Liens vers les fichiers CSV hébergés en ligne (GitHub)
url1 = "https://raw.githubusercontent.com/JhpAb/data354_Hiring_Challenge/main/DATABASE/cyber_security_ai_tools.csv"
url2 = "https://raw.githubusercontent.com/JhpAb/data354_Hiring_Challenge/main/DATABASE/top_10_authors_df_sorted.csv"

# 📥 Chargement du 1er fichier CSV : Données de publications
try:
    df = pd.read_csv(url1)
except Exception as e:
    st.error(f"Erreur lors du chargement du fichier CSV principal: {e}")
    df = pd.DataFrame()

# 📥 Chargement du 2e fichier CSV : Données des auteurs
try:
    top_10_authors_df_sorted = pd.read_csv(url2)
except Exception as e:
    st.error(f"Erreur lors du chargement du fichier des auteurs: {e}")
    top_10_authors_df_sorted = pd.DataFrame(columns=['Author', 'Likes', 'Shares', 'Keywords', 'Content'])

# 🏷️ Titre principal du dashboard
st.title("📊 LinkedIn Post Analysis Dashboard")

# 📚 Menu de navigation dans la barre latérale
st.sidebar.title("Navigation")
page = st.sidebar.radio("Aller à", [
    "📈 Statistiques générales", 
    "🏆 Analyse des auteurs", 
    "🔍 Analyse des mots-clés",
    "📋 Analyse du contenu de publications"
])

# ================================
# 1️⃣ Page : Statistiques générales
# ================================
if page == "📈 Statistiques générales":
    st.header("📊 Statistiques générales")
    
    # 🔍 Affichage du DataFrame principal
    st.subheader("Tableau des données : LinkedIn_Post_Analysis.csv")
    st.dataframe(df)

    # 🧮 Affichage des métriques clés sur la même ligne dans des cases
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(label="Total des publications", value=len(df))

with col2:
    st.metric(label="Nombre d'auteurs uniques", value=df['Author'].nunique())

with col3:
    # Top 10 des auteurs
    top_10_authors_count = df['Author'].value_counts().head(10).count()
    st.metric(label="Top 10 des auteurs", value=top_10_authors_count)

with col4:
    # Nombre de mots-clés uniques
    unique_keywords_count = df['Keywords'].nunique()
    st.metric(label="Nombre de mots-clés uniques", value=unique_keywords_count)


    # 📊 Top 30 auteurs avec le plus de publications
    st.subheader("Nombre de publications par auteur")
    author_counts = df['Author'].value_counts().head(30)
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(x=author_counts.index, y=author_counts.values, palette="coolwarm", ax=ax)
    plt.xticks(rotation=90)
    plt.xlabel("Auteurs")
    plt.ylabel("Nombre de publications")
    plt.title("Top 30 des auteurs par nombre de publications")
    st.pyplot(fig)

# ============================
# 2️⃣ Page : Analyse des auteurs
# ============================
elif page == "🏆 Analyse des auteurs":
    st.header("🏆 Top 10 Auteurs")

    # 🧾 Affichage des données des auteurs
    st.subheader("Tableau des données : Top_10_authors.csv")
    st.dataframe(top_10_authors_df_sorted)

    # 📊 Auteurs avec le plus de publications
    st.subheader("Auteurs avec le plus de publications")
    author_counts = top_10_authors_df_sorted['Author'].value_counts().head(10)
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(x=author_counts.values, y=author_counts.index, color="red", ax=ax)
    plt.xlabel("Nombre de publications")
    plt.ylabel("Auteurs")
    plt.title("Top 10 des auteurs avec le plus de publications")
    st.pyplot(fig)

    # 📊 Likes et Shares des Top 10 Auteurs (2 colonnes côte à côte)
    st.subheader("Likes et Shares des Top 10 Auteurs")
    col1, col2 = st.columns(2)

    with col1:
        fig, ax = plt.subplots(figsize=(12, 6))
        sns.barplot(x='Likes', y='Author', data=top_10_authors_df_sorted, palette='viridis', ax=ax)
        plt.xlabel("Likes")
        plt.ylabel("Auteurs")
        plt.title("Likes des Top 10 Auteurs")
        st.pyplot(fig)

    with col2:
        fig, ax = plt.subplots(figsize=(12, 6))
        sns.barplot(x='Shares', y='Author', data=top_10_authors_df_sorted, palette='magma', ax=ax)
        plt.xlabel("Shares")
        plt.ylabel("Auteurs")
        plt.title("Shares des Top 10 Auteurs")
        st.pyplot(fig)

    # 🔗 Corrélation entre Likes et Shares
    st.subheader("📊 Corrélation entre Likes et Shares")
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.scatterplot(x='Likes', y='Shares', data=top_10_authors_df_sorted, color='purple', ax=ax)
    plt.xlabel("Likes")
    plt.ylabel("Shares")
    plt.title("Corrélation entre Likes et Shares")
    st.pyplot(fig)
    correlation = top_10_authors_df_sorted['Likes'].corr(top_10_authors_df_sorted['Shares'])
    st.write(f"Coefficient de corrélation : **{correlation:.2f}**")

# ============================
# 3️⃣ Page : Analyse des mots-clés
# ============================
elif page == "🔍 Analyse des mots-clés":
    st.header("🔍 Analyse des mots-clés")

    st.subheader("Tableau des données : Top_10_authors.csv")
    st.dataframe(top_10_authors_df_sorted)

    # 🔍 Analyse croisée Auteurs x Mots-clés (graphique empilé)
    st.subheader("📚 Top 10 des auteurs par mots-clés")
    author_keyword_counts = df.groupby(['Author', 'Keywords'])['Author'].count().unstack().fillna(0)
    top_10_authors = author_keyword_counts.sum(axis=1).sort_values(ascending=False).head(10).index
    top_author_keyword_counts = author_keyword_counts.loc[top_10_authors]

    fig, ax = plt.subplots(figsize=(15, 8))
    top_author_keyword_counts.plot(kind='bar', stacked=True, ax=ax)
    plt.title('Top 10 des Auteurs Uniques par Mot-clés')
    plt.xlabel('Auteurs')
    plt.ylabel('Nombre de Publications')
    plt.xticks(rotation=45, ha='right')
    plt.legend(title='Mots-clés', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    st.pyplot(fig)

    # ☁️ WordCloud des mots-clés
    st.subheader("WordCloud des mots-clés")
    text = " ".join(top_10_authors_df_sorted['Keywords'].dropna().astype(str))
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis("off")
    plt.title("Nuage de mots des mots-clés")
    st.pyplot(fig)

# ===============================
# 4️⃣ Page : Analyse du contenu texte
# ===============================
elif page == "📋 Analyse du contenu de publications":
    st.header("📋 Analyse du contenu de publications")

    st.subheader("Tableau des données : Top_10_authors.csv")
    st.dataframe(top_10_authors_df_sorted)

    # ☁️ WordCloud du contenu des publications
    st.subheader("WordCloud du contenu des publications")
    text_content = " ".join(top_10_authors_df_sorted['Content'].dropna().astype(str))
    wordcloud_content = WordCloud(width=800, height=400, background_color='white').generate(text_content)
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wordcloud_content, interpolation='bilinear')
    ax.axis("off")
    plt.title("Nuage de mots du contenu des publications")
    st.pyplot(fig)

# ========================
# 👤 Pied de page - Auteurs
# ========================
st.sidebar.markdown("---")
st.sidebar.markdown("📌 **Auteur : ABBE Jean Pierre, Data Analyst | CEM Engineer**")
st.sidebar.markdown("📞 **Téléphone :** +225 0749499034")
st.sidebar.markdown("📧 **Email :** abbejeanpierre0808@gmail.com")
st.sidebar.info("👈 Sélectionnez une section pour explorer les données !")
