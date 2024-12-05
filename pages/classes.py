import streamlit as st
from pages import presence_journaliere, performance_sequentielle, performance_trimestrielle, performance_annuelle
from pages import performance_sequentielle_enseignant, performance_trimestrielle_enseignant, performance_annuelle_enseignant

def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def navigate_to_page(page_name, mode=None):
    st.session_state['page'] = page_name
    if mode:
        st.session_state['mode'] = mode
    st.rerun()

def handle_class_selection(class_name):
    st.session_state['class'] = class_name
    role = st.session_state.get('role')
    evolution_type = st.session_state.get('evolution_type')

    if role == "admin":
        if evolution_type == "séquentielle":
            st.session_state['page'] = "Performance Séquentielle"
            st.session_state['mode'] = "Visualisation" 
        elif evolution_type == "trimestrielle":
            st.session_state['page'] = "Performance Trimestrielle"
            st.session_state['mode'] = "Visualisation" 
        elif evolution_type == "annuelle":
            st.session_state['page'] = "Performance Annuelle"
            st.session_state['mode'] = "Visualisation" 
        else:
            st.session_state['page'] = "Présence Journalière"
        st.rerun()
    elif role == "teacher":
        if evolution_type == "séquentielle":
            st.session_state['page'] = "Performance Séquentielle Enseignant"
        elif evolution_type == "trimestrielle":
            st.session_state['page'] = "Performance Trimestrielle Enseignant"
        elif evolution_type == "annuelle":
            st.session_state['page'] = "Performance Annuelle Enseignant"
        st.rerun()
    elif role == "admin_principal":
        if evolution_type == "séquentielle":
            st.session_state['page'] = "Performance Séquentielle"
            st.session_state['mode'] = "Visualisation"
        elif evolution_type == "trimestrielle":
            st.session_state['page'] = "Performance Trimestrielle"
            st.session_state['mode'] = "Visualisation"
        elif evolution_type == "annuelle":
            st.session_state['page'] = "Performance Annuelle"
            st.session_state['mode'] = "Visualisation"
        else:
            st.session_state['visualisation_mode'] = True  # Activer le mode visualisation ici
            st.session_state['page'] = "Présence Journalière"
        st.rerun()


def classes_page():
    load_css("static/styles/styles.css")
    col1, col2, col3 = st.columns([1.5, 2, 0.5])
    with col2:
        st.image("static/images/logo.png", use_container_width=True)
    st.title("Page des Classes")

    if 'francophone_clicked' not in st.session_state:
        st.session_state['francophone_clicked'] = False
    if 'anglophone_clicked' not in st.session_state:
        st.session_state['anglophone_clicked'] = False

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Section Francophone", key="francophone"):
            st.session_state['francophone_clicked'] = True
            st.session_state['anglophone_clicked'] = False
            st.rerun()
    with col2:
        if st.button("Section Anglophone", key="anglophone"):
            st.session_state['anglophone_clicked'] = True
            st.session_state['francophone_clicked'] = False
            st.rerun()

    if st.session_state['francophone_clicked']:
        st.subheader("Section Francophone")
        col1, col2, col3= st.columns(3)

        with col1:
            if st.button("6ème", key="6ème"):
                handle_class_selection("6ème")
      

        with col2:
            if st.button("5ème", key="5ème"):
                handle_class_selection("5ème")
        
        with col3:
             if st.button("4ème", key="4ème"):
                handle_class_selection("4ème")
  
        if st.button("Retour Francophone", key="Retour_F"):
            st.session_state['francophone_clicked'] = False
            st.rerun()

    elif st.session_state['anglophone_clicked']:
        st.subheader("Section Anglophone")
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            if st.button("Form1", key="Form1"):
                handle_class_selection("Form1")
           

        with col2:
            if st.button("Form2", key="Form2"):
                handle_class_selection("Form2")
           

        with col3:
            if st.button("Form3", key="Form3"):
                handle_class_selection("Form3")
         
        
        if st.button("Retour Anglophone", key="Retour_A"):
            st.session_state['anglophone_clicked'] = False
            st.rerun()

    # Bouton Retour Général
    if not st.session_state['francophone_clicked'] and not st.session_state['anglophone_clicked']:
        if st.button("Retour", key="general_return"):
            st.session_state['page'] = "Page d'évolution"
            st.rerun()

    # Navigation vers les pages respectives en mode visualisation ou saisie
    if 'page' in st.session_state:
        if st.session_state['page'] == "Performance Séquentielle":
            if st.session_state.get('mode') == "Visualisation":
                # Masque les éléments de saisie et affiche uniquement ceux de visualisation
                performance_sequentielle.visualisation_performance()
            else:
                # Affiche les éléments de saisie uniquement pour les enseignants
                performance_sequentielle.performance_sequentielle_page()
        elif st.session_state['page'] == "Performance Trimestrielle":
            if st.session_state.get('mode') == "Visualisation":
                performance_trimestrielle.visualisation_performance()
            else:
                performance_trimestrielle.performance_trimestrielle_page()
        elif st.session_state['page'] == "Performance Annuelle":
            if st.session_state.get('mode') == "Visualisation":
                performance_annuelle.visualisation_performance()
            else:
                performance_annuelle.performance_annuelle_page()
        elif st.session_state['page'] == "Présence Journalière":
            # Afficher la page de présence journalière en mode visualisation
            if st.session_state.get('visualisation_mode'):
                presence_journaliere.visualisation_presence_journaliere()
            else:
                # Décommenter la ligne ci-dessous si l'Admin Principal doit saisir les présences
                # presence_journaliere.presence_journaliere_page()
                st.warning("L'Administrateur Principal n'a pas accès à la saisie des présences journalières. ")
if __name__ == "__main__":
    classes_page()