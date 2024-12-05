import streamlit as st
from pages import classes, evolution_sequentielle, evolution_trimestrielle

def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def page_d_evolution():
    load_css("static/styles/styles.css")
    col1, col2, col3 = st.columns([1.5, 2, 0.5])
    with col2:
        st.image("static/images/logo.png", use_container_width=True)

    st.title("Page d'Évolution")
    st.session_state['page'] = "Page d'évolution"

    if st.session_state['role'] in ['admin', 'admin_principal', 'parent']:  # Ajoutez le parent
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            if st.button("Présence Journalière"):
                # Vérification du rôle et activation du mode visualisation
                if st.session_state['role'] == 'admin': 
                    st.session_state['evolution_type'] = None
                    st.session_state['page'] = "Page des Classes"
                elif st.session_state['role'] == 'admin_principal': 
                    st.session_state['evolution_type'] = None
                    st.session_state['page'] = "Page des Classes"
                elif st.session_state['role'] == 'parent':
                    st.session_state['evolution_type'] = None
                    st.session_state['page'] = "Présence Journalière"
                st.rerun()
        with col2:
            if st.button("Évolution Séquentielle"):
                st.session_state['evolution_type'] = "séquentielle"
                # Dirigez le parent vers la page de choix de la séquence
                if st.session_state['role'] == 'parent':
                    st.session_state['page'] = "Évolution Séquentielle"
                    st.rerun()
                else:
                    st.session_state['mode'] = "Visualisation"
                    st.session_state['page'] = "Évolution Séquentielle"
                    st.rerun()
        with col3:
            if st.button("Évolution Trimestrielle"):
                st.session_state['evolution_type'] = "trimestrielle"
                # Dirigez le parent vers la page de choix du trimestre
                if st.session_state['role'] == 'parent':
                    st.session_state['page'] = "Évolution Trimestrielle"
                    st.rerun()
                else:
                    st.session_state['mode'] = "Visualisation"  
                    st.session_state['page'] = "Évolution Trimestrielle"
                    st.rerun()
        with col4:
            if st.button("Évolution Annuelle"):
                st.session_state['evolution_type'] = "annuelle"
                # Dirigez le parent vers la visualisation annuelle
                if st.session_state['role'] == 'parent':
                    st.session_state['page'] = "Performance Annuelle"
                    st.rerun()
                else:
                    st.session_state['mode'] = "Visualisation"  
                    st.session_state['page'] = "Page des Classes"
                    st.rerun()

    elif st.session_state['role'] == 'teacher':
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            if st.button("Présence Journalière"):
                st.warning("Veuillez vous connecter en tant qu'administrateur")
        with col2:
            if st.button("Évolution Séquentielle"):
                st.session_state['evolution_type'] = "séquentielle"
                st.session_state['page'] = "Évolution Séquentielle"
                st.rerun()
        with col3:
            if st.button("Évolution Trimestrielle"):
                st.session_state['evolution_type'] = "trimestrielle"
                st.session_state['page'] = "Évolution Trimestrielle"
                st.rerun()
        with col4:
            if st.button("Évolution Annuelle"):
                st.session_state['evolution_type'] = "annuelle"
                st.session_state['page'] = "Page des Classes"
                st.rerun()

    if st.button("Retour", key="comptes"):
        st.session_state['page'] = "Page des Comptes"
        st.rerun()

if __name__ == "__main__":
    page_d_evolution()