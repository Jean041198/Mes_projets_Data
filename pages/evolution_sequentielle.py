import streamlit as st
from pages.classes import classes_page
import sqlite3
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)




# Fonction pour établir la connexion à la base de données
DB_PATH = "utils/collegefoganggenies_db.sqlite"      

# Fonction pour établir la connexion à la base de données SQLite
def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    return conn


def evolution_sequentielle_page():
    load_css("static/styles/styles.css")
    col1, col2, col3 = st.columns([1.5, 2, 0.5])
    with col2:
        st.image("static/images/logo.png", use_container_width=True)
    st.title("Veuillez choisir la séquence")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Séquence 1"):
            st.session_state['sequence'] = 1
            # Dirigez vers la page de performance 
            if st.session_state['role'] == 'parent':
                st.session_state['page'] = "Performance Séquentielle"  
                st.rerun()
            else:
                st.session_state['page'] = "Page des Classes" 
                st.rerun()
        if st.button("Séquence 4"):
            st.session_state['sequence'] = 4
            # Dirigez vers la page de performance 
            if st.session_state['role'] == 'parent':
                st.session_state['page'] = "Performance Séquentielle"  
                st.rerun()
            else:
                st.session_state['page'] = "Page des Classes" 
                st.rerun()
    with col2:
        if st.button("Séquence 2"):
            st.session_state['sequence'] = 2
            # Dirigez vers la page de performance 
            if st.session_state['role'] == 'parent':
                st.session_state['page'] = "Performance Séquentielle"  
                st.rerun()
            else:
                st.session_state['page'] = "Page des Classes" 
                st.rerun()
        if st.button("Séquence 5"):
            st.session_state['sequence'] = 5
            # Dirigez vers la page de performance 
            if st.session_state['role'] == 'parent':
                st.session_state['page'] = "Performance Séquentielle"  
                st.rerun()
            else:
                st.session_state['page'] = "Page des Classes" 
                st.rerun()
    with col3:
        if st.button("Séquence 3"):
            st.session_state['sequence'] = 3
            # Dirigez vers la page de performance 
            if st.session_state['role'] == 'parent':
                st.session_state['page'] = "Performance Séquentielle"  
                st.rerun()
            else:
                st.session_state['page'] = "Page des Classes" 
                st.rerun()
        if st.button("Séquence 6"):
            st.session_state['sequence'] = 6
            # Dirigez vers la page de performance 
            if st.session_state['role'] == 'parent':
                st.session_state['page'] = "Performance Séquentielle"  
                st.rerun()
            else:
                st.session_state['page'] = "Page des Classes" 
                st.rerun()

    if st.session_state.get('page') == "Page des Classes":
        st.session_state['page'] = None  # Reset pour la prochaine utilisation
        classes_page()

if __name__ == "__main__":
    evolution_sequentielle_page()