import streamlit as st
from pages.classes import classes_page
import mysql.connector
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)



# Fonction pour établir la connexion à la base de données
def get_db_connection():
    mydb = mysql.connector.connect(
        host="localhost",
        user="gelito01",
        password="admin@01",
        database="collegefoganggenies_db"
    )
    return mydb



def evolution_trimestrielle_page():
    load_css("static/styles/styles.css")
    col1, col2, col3 = st.columns([1.5, 2, 0.5])
    with col2:
        st.image("static/images/logo.png", width=150)
    st.title("Veuillez choisir le trimestre")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Trimestre 1"):
            st.session_state['trimestre'] = 1
            # Dirigez vers la page de performance 
            if st.session_state['role'] == 'parent':
                st.session_state['page'] = "Performance Trimestrielle"  
                st.rerun()
            else:
                st.session_state['page'] = "Page des Classes" 
                st.rerun()
    with col2:       
        if st.button("Trimestre 2"):
            st.session_state['trimestre'] = 2
            # Dirigez vers la page de performance 
            if st.session_state['role'] == 'parent':
                st.session_state['page'] = "Performance Trimestrielle"  
                st.rerun()
            else:
                st.session_state['page'] = "Page des Classes" 
                st.rerun()
    with col3:
        if st.button("Trimestre 3"):
            st.session_state['trimestre'] = 3
            # Dirigez vers la page de performance 
            if st.session_state['role'] == 'parent':
                st.session_state['page'] = "Performance Trimestrielle"  
                st.rerun()
            else:
                st.session_state['page'] = "Page des Classes" 
                st.rerun()
       

    if st.session_state.get('page') == "Page des Classes":
        st.session_state['page'] = None  # Reset pour la prochaine utilisation
        classes_page()

if __name__ == "__main__":
    evolution_trimestrielle_page()