import streamlit as st
from pages import comptes, page_d_evolution, classes, presence_journaliere
from pages import evolution_sequentielle, performance_sequentielle, evolution_trimestrielle
from pages import performance_trimestrielle, performance_annuelle
from pages import performance_sequentielle_enseignant, performance_trimestrielle_enseignant
from pages import performance_annuelle_enseignant
import mysql.connector


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
        st.write("Voici les informations sur l'application...")

if __name__ == "__main__":
    main()