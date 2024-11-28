import streamlit as st
from pages import comptes, page_d_evolution, classes, presence_journaliere
from pages import evolution_sequentielle, performance_sequentielle, evolution_trimestrielle
from pages import performance_trimestrielle, performance_annuelle
from pages import performance_sequentielle_enseignant, performance_trimestrielle_enseignant
from pages import performance_annuelle_enseignant
import mysql.connector
import os


# Fonction pour établir la connexion à la base de données
def get_db_connection():
    # Remplacez les informations par vos propres valeurs
    mydb = mysql.connector.connect(
        host="localhost",
        user="gelito01",
        password="admin@01",
        database="collegefoganggenies_db"
    )
    return mydb


def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def main():
    # Charger le CSS
    load_css("static/styles/styles.css")
    
    # Définir la page par défaut si elle n'existe pas encore dans l'état de la session
    if 'page' not in st.session_state:
        st.session_state['page'] = 'Application'
    
    # Définir le mode de visualisation par défaut si nécessaire
    if 'visualisation_mode' not in st.session_state:
        st.session_state['visualisation_mode'] = False
    
    # Sidebar - Main Menu avec le titre "Collège bilingue Fogang et les Génies" au-dessus de "app"
    st.sidebar.markdown(
        """
        <div style='display: flex; align-items: center; background-color: #87CEEB; color: #000000; padding: 10px;'>
            <h1 style='font-size: 28px; color:  #001f3f; margin: 0;'>Collège bilingue Fogang et les Génies</h1>
        </div>
        """, unsafe_allow_html=True)
    
    # Section 'Menu'
    st.sidebar.markdown("<h2 style='color: #000000;'>Menu</h2>", unsafe_allow_html=True)
    options = ["Application", "Page des Comptes", "Page d'évolution", "Page des Classes", 
               "Présence Journalière", "Évolution Séquentielle", "Évolution Trimestrielle", 
               "Performance Séquentielle", "Performance Trimestrielle", "Performance Annuelle", 
               "Performance Séquentielle Enseignant","Performance Trimestrielle Enseignant",
               "Performance Annuelle Enseignant"]
    selected_page = st.sidebar.selectbox(
        "Choisissez une page",  # Pas besoin de <div> ici
        options, 
        index=options.index(st.session_state['page'])
    )

    # Mettre à jour l'état de la session avec la page sélectionnée
    if st.session_state['page'] != selected_page:
        st.session_state['page'] = selected_page
        st.session_state['visualisation_mode'] = False  # Réinitialiser le mode de visualisation
        st.rerun()
    
    # Afficher les pages en fonction de la sélection
    if st.session_state['page'] == "Page des Comptes":
        comptes.comptes_page()
    elif st.session_state['page'] == "Page d'évolution":
        page_d_evolution.page_d_evolution()
    elif st.session_state['page'] == "Page des Classes":
        classes.classes_page()
    elif st.session_state['page'] == "Présence Journalière":
        presence_journaliere.presence_journaliere_page()
    elif st.session_state['page'] == "Évolution Séquentielle":
        evolution_sequentielle.evolution_sequentielle_page()
    elif st.session_state['page'] == "Performance Séquentielle":
        if st.session_state.get('visualisation_mode', False):
            performance_sequentielle.visualisation_performance()
        else:
            performance_sequentielle.performance_sequentielle_page()
    elif st.session_state['page'] == "Évolution Trimestrielle":
        evolution_trimestrielle.evolution_trimestrielle_page()
    elif st.session_state['page'] == "Performance Trimestrielle":
        if st.session_state.get('visualisation_mode', False):
            performance_trimestrielle.visualisation_performance()
        else:
            performance_trimestrielle.performance_trimestrielle_page()
    elif st.session_state['page'] == "Performance Annuelle":
        if st.session_state.get('visualisation_mode', False):
            performance_annuelle.visualisation_performance()
        else:
            performance_annuelle.performance_annuelle_page()
    elif st.session_state['page'] == "Performance Séquentielle Enseignant":
         performance_sequentielle_enseignant.performance_sequentielle_enseignant_page()
    elif st.session_state['page'] == "Performance Trimestrielle Enseignant":
         performance_trimestrielle_enseignant.performance_trimestrielle_enseignant_page()
    elif st.session_state['page'] == "Performance Annuelle Enseignant":
         performance_annuelle_enseignant.performance_annuelle_enseignant_page()
    elif st.session_state['page'] == "Application":
        st.title("À propos de l'application")
        st.write("## Guide d' utilisation")
        st.markdown("""

        Ce guide décrit les fonctionnalités de l'application pour chaque type d'utilisateur.
         **Tous les utilisateurs utilisent la barre latérale pour naviguer entre les pages de l'application.** 

        **I. Accès à l'application**

        Pour accéder à l'application, rendez-vous sur l'URL fournie. Vous aurez besoin de vous connecter en utilisant votre identifiant et votre mot de passe.

        **II. Types d'utilisateurs et fonctionnalités**

        L'application propose différents niveaux d'accès pour garantir la sécurité et la confidentialité des données.

        **A. Administration**

        Les administrateurs ont accès aux fonctionnalités suivantes :

        *   **Page des Comptes :** Se coonecter via ses identifiants.
        *   **Page d'évolution :** Consulter et suivre l'évolution des performances des élèves au niveau séquentiel, trimestriel et annuel. Générer des rapports et analyses.
        *   **Page des classes :** Afficher et gérer les informations sur les classes.
        *   **Présence Journalière :** Consulter la présence des élèves. 
        *   **Pages de Performance (Visualisation) :** Visualiser les performances des élèves de manière globale avec des analyses et des graphiques détaillés.


        **B. Administrateur Principal**

        L'administrateur principal possède les mêmes fonctionnalités que l'administrateur et peut :

        *   **Surveiller l'activité de tous les utilisateurs.**
        *   **Gérer les paramètres généraux de l'application.**
        *   **Visualiser des rapports plus détaillés.**


        **C. Enseignant**

        Les enseignants ont un accès limité à l'application, axé sur la gestion des notes et le suivi de la progression de leurs élèves :

        *   **Page des Comptes :** Se connecter à l'application.
        *   **Page d'évolution :** Consulter et suivre l'évolution des performances des élèves au niveau séquentiel, trimestriel et annuel.
        *   **Page des Classes:** Sélectionner la classe.
        *   **Pages de Performance (Saisie) :** Saisir et enregistrer les notes de leurs élèves pour chaque séquence, chaque trimestre et en fin d'année.
        *   **Pages de Performance (Visualisation) :** Visualiser les performances de leurs élèves.


        **D. Parent**

        Les parents ont accès aux informations concernant leurs enfants :

        *   **Page de connexion des parents :** Se connecter avec un identifiant et un mot de passe.
        *   **Tableau de bord des parents :** Visualiser les notes, les présences et les rapports de progression de leurs enfants.


        **III. Instructions pour l'utilisation de chaque page**

        Les descriptions suivantes détaillent l'utilisation de chaque page de l'application :

        *   **Page des Comptes :** Cette page permet à chaque
        *   **Page d'évolution:** Cette page permet de suivre l'évolution des performances des élèves. Sélectionnez le type d'évolution (séquentiel, trimestriel, annuel), la classe et visualisez les rapports.
        *   **Page des Classes :** Cette page liste les différentes classes. Sélectionnez la classe pour accéder à la saisie ou la visualisation des notes. 
        *   **Présence Journalière :** Cette page permet de saisir et de visualiser la présence des élèves.
        *   **Pages de Performance (Saisie/Visualisation) :** Ces pages permettent aux enseignants de saisir et enregistrer les notes. L'administrateur et l'administrateur principal peuvent visualiser les notes et les graphiques d'évolution.
        *   **Tableau de bord des parents :** Cette page affiche un résumé des notes, des présences et des rapports de progression des enfants du parent connecté.


        **IV. Assistance**

        Pour toute question ou problème technique, veuillez contacter l'équipe d'assistance à l'adresse email suivante : angelnyoungou@gmail.com


        **V. Avertissement**

        Toutes les données saisies dans l'application sont **confidentielles** et doivent être utilisées à des fins scolaires uniquement.

        Ce guide est conçu pour vous aider à utiliser l'application de manière efficace. N'hésitez pas à nous contacter pour toute question.
    """, unsafe_allow_html=True)

# Injecter le JavaScript
polyfill_script = """
<script>
if (!String.prototype.replaceAll) {
    String.prototype.replaceAll = function(search, replacement) {
        const target = this;
        return target.split(search).join(replacement);
    };
}
</script>
"""
st.components.v1.html(polyfill_script, height=0)




if __name__ == "__main__":
    main()