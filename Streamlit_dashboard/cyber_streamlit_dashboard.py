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

    # 🧮 Affichage des métriques clés dans des cases colorées
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(f"<div style='background-color:#dbe9d7; padding:10px; border-radius:10px; text-align:center;'><b>Total des publications</b><br><span style='font-size:20px; color:#1a8d5e;'>{len(df)}</span></div>", unsafe_allow_html=True)

    with col2:
        st.markdown(f"<div style='background-color:#d9f7be; padding:10px; border-radius:10px; text-align:center;'><b>Nombre d'auteurs uniques</b><br><span style='font-size:20px; color:#5cb85c;'>{df['Author'].nunique()}</span></div>", unsafe_allow_html=True)

    with col3:
        top_10_authors_count = len(top_10_authors_df_sorted)
        st.markdown(f"<div style='background-color:#f6d9d9; padding:10px; border-radius:10px; text-align:center;'><b>Nombres de publications du Top 10 des auteurs</b><br><span style='font-size:20px; color:#f0ad4e;'>{top_10_authors_count}</span></div>", unsafe_allow_html=True)

    with col4:
        unique_keywords_count = df['Keywords'].dropna().nunique()  # Assurez-vous d'ignorer les NaN
        st.markdown(f"<div style='background-color:#e9f7ff; padding:10px; border-radius:10px; text-align:center;'><b>Nombre de mots-clés uniques</b><br><span style='font-size:20px; color:#5bc0de;'>{unique_keywords_count}</span></div>", unsafe_allow_html=True)

    with col5:
        st.markdown(f"<div style='background-color:#f1e0ff; padding:10px; border-radius:10px; text-align:center;'><b>Total des Likes</b><br><span style='font-size:20px; color:#9b59b6;'>{total_likes}</span></div>", unsafe_allow_html=True)

    with col6:
        st.markdown(f"<div style='background-color:#e0f7fa; padding:10px; border-radius:10px; text-align:center;'><b>Total des Shares</b><br><span style='font-size:20px; color:#00bcd4;'>{total_shares}</span></div>", unsafe_allow_html=True)

        # Affichage du nombre total de Likes et Shares du Top 10 des auteurs
        st.markdown(f"<div style='background-color:#f9f8f8; padding:10px; border-radius:10px; text-align:center;'><b>Likes Totals des Top 10 Auteurs</b><br><span style='font-size:20px; color:#ff6347;'>{top_10_likes}</span></div>", unsafe_allow_html=True)
        st.markdown(f"<div style='background-color:#f9f8f8; padding:10px; border-radius:10px; text-align:center;'><b>Shares Totals des Top 10 Auteurs</b><br><span style='font-size:20px; color:#ff6347;'>{top_10_shares}</span></div>", unsafe_allow_html=True)

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
    plt.title("Top 10 des auteurs et/ou sources avec le plus de publications")
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
        # 📝 Explication sous le graphique
        st.write("Ce graphique montre le nombre de 'Likes' accumulés par chaque auteur parmi les 10 auteurs les plus actifs." 
        " Il permet de comparer l'engagement des utilisateurs vis-à-vis des publications de chaque auteur.")


    with col2:
        fig, ax = plt.subplots(figsize=(12, 6))
        sns.barplot(x='Shares', y='Author', data=top_10_authors_df_sorted, palette='magma', ax=ax)
        plt.xlabel("Shares")
        plt.ylabel("Auteurs")
        plt.title("Shares des Top 10 Auteurs")
        st.pyplot(fig)
        # 📝 Explication sous le graphique
        st.write("Ce graphique illustre le nombre de 'Shares' (partages) des publications des Top 10 Auteurs." 
        " Cela permet d'évaluer la viralité des publications et de voir comment elles sont partagées au sein du réseau LinkedIn.")

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

    
    
    
    st.write("N.B : Les donées de 'Likes' 'Shares' on été générées de manière arbitraires vu que nous ne pouvions les colleceter.")


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
    # 📝 Explication sous le graphique
    st.write("Ce graphique montre la distribution des publications par auteur en fonction des mots-clés." 
    " Il permet d'observer quelles sont les thématiques les plus abordées par les auteurs en fonction de leur domaine d'activité.")

# ================================
# 4️⃣ Page : Analyse du contenu texte
# ================================
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
    # 📝 Explication sous le graphique
    st.write("Le WordCloud ci-dessus présente visuellement les mots les plus fréquemment utilisés dans le contenu des publications des Top 10 Auteurs. "
    " Plus un mot est grand, plus il apparaît fréquemment dans les textes. ")

# ========================
# 👤 Pied de page - Auteurs
# ========================
st.sidebar.markdown("---")
st.sidebar.markdown("📌 **Auteur : ABBE Jean Pierre, Data Analyst | CEM Engineer**")
st.sidebar.markdown("📞 **Téléphone :** +225 0749499034")
st.sidebar.markdown("📧 **Email :** abbejeanpierre0808@gmail.com")
st.sidebar.info("👈 Sélectionnez une section pour explorer les données !")
