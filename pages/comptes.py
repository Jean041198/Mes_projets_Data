import streamlit as st
from pages import page_d_evolution

import os
import sqlite3
ADMIN_ID = "admin123"
ADMIN_PASSWORD = "password123"
TEACHER_ID = "teacher123"
TEACHER_PASSWORD = "password456"
ADMIN_PRINCIPAL_ID = "adminprincipal123" 
ADMIN_PRINCIPAL_PASSWORD = "password789"  

def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

DB_PATH = "utils/collegefoganggenies_db.sqlite"      

# Fonction pour établir la connexion à la base de données SQLite
def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    return conn

# Fonction d'authentification (modifiée pour SQLite)
def authenticate_user(username, password, role):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        if role == 'admin':
            sql = "SELECT * FROM administration WHERE identifiant = ? AND mot_de_passe = ?"
            cursor.execute(sql, (username, password))
        elif role == 'teacher':
            sql = "SELECT * FROM enseignants WHERE identifiant = ? AND mot_de_passe = ?"
            cursor.execute(sql, (username, password))
        elif role == 'admin_principal':
            sql = "SELECT * FROM administrateur_principal WHERE identifiant = ? AND mot_de_passe = ?"
            cursor.execute(sql, (username, password))
        elif role == 'parent':
            sql = "SELECT * FROM eleves WHERE matricule_eleve = ?"
            cursor.execute(sql, (username,))
        else:
            conn.close()
            return False, "Rôle invalide."

        result = cursor.fetchone()
        if result:
            conn.close()
            return True, None
        else:
            conn.close()
            return False, "Nom d'utilisateur ou mot de passe incorrect."
    except sqlite3.Error as e:
        conn.close()
        return False, f"Erreur de base de données : {e}"

def show_admin_login():
    st.subheader("Connexion Administration")
    admin_id = st.text_input("ID Administrateur")
    admin_password = st.text_input("Mot de passe", type="password")

    if st.button("Se connecter"):
        success, message = authenticate_user(admin_id, admin_password, 'admin')
        if success:
            st.success("Connexion réussie !")
            st.session_state['role'] = 'admin'
            st.session_state['page'] = "Page d'évolution"  
            st.rerun()
        else:
            st.error(message)

def show_teacher_login():
    st.subheader("Connexion Enseignant")
    teacher_id = st.text_input("ID Enseignant")
    teacher_password = st.text_input("Mot de passe", type="password")

    if st.button("Se connecter"):
        success, message = authenticate_user(teacher_id, TEACHER_PASSWORD, 'teacher')  
        if success:
            st.success("Connexion réussie !")
            st.session_state['role'] = 'teacher'
            st.session_state['page'] = "Page d'évolution"  
            st.rerun()
        else:
            st.error(message)

def show_admin_principal_login():
    st.subheader("Connexion Administrateur Principal")
    admin_principal_id = st.text_input("ID Administrateur Principal")
    admin_principal_password = st.text_input("Mot de passe", type="password")

    if st.button("Se connecter"):
        success, message = authenticate_user(admin_principal_id, admin_principal_password, 'admin_principal')
        if success:
            st.success("Connexion réussie !")
            st.session_state['role'] = 'admin_principal'
            st.session_state['page'] = "Page d'évolution"
            st.rerun()
        else:
            st.error(message)

def show_parent_login():
    st.subheader("Connexion Parent")
    parent_id = st.text_input("Entrer le Matricule de l'élève")  # Saisir le matricule de l'enfant

    if st.button("Se connecter"):
        # On utilise le même matricule comme identifiant et mot de passe
        success, message = authenticate_user(parent_id, parent_id, 'parent')  
        if success:
            st.success("Connexion réussie !")
            st.session_state['role'] = 'parent'
            st.session_state['page'] = "Page d'évolution"
            st.session_state['matricule_eleve'] = parent_id  # Enregistrer le matricule de l'élève
            st.rerun()
        else:
            st.error(message)

def comptes_page():
    load_css("static/styles/styles.css")

    col1, col2, col3 = st.columns([1.5, 2, 0.5])
    with col2:
        st.image("static/images/logo.png", use_container_width=True)

    if st.session_state['page'] == "Page des Comptes":
        st.title("Page des Comptes")

    if 'admin_clicked' not in st.session_state:
        st.session_state['admin_clicked'] = False
    if 'teacher_clicked' not in st.session_state:
        st.session_state['teacher_clicked'] = False
    if 'admin_principal_clicked' not in st.session_state:
        st.session_state['admin_principal_clicked'] = False
    if 'parent_clicked' not in st.session_state:  
        st.session_state['parent_clicked'] = False

    if not st.session_state['admin_clicked'] and not st.session_state['teacher_clicked'] and not st.session_state['admin_principal_clicked'] and not st.session_state['parent_clicked']:  # Ajoutez pour le parent
        col1, col2, col3, col4 = st.columns([3.5, 3, 5, 3])
        with col1:
            if st.button("Administration"):
                st.session_state['admin_clicked'] = True
                st.rerun()
        with col2:
            if st.button("Enseignant"):
                st.session_state['teacher_clicked'] = True
                st.rerun()
        with col3:
            if st.button("Administrateur Principal"):
                st.session_state['admin_principal_clicked'] = True
                st.rerun()
        with col4:  
            if st.button("Parent"):
                st.session_state['parent_clicked'] = True
                st.rerun()

    if st.session_state['admin_clicked']:
        show_admin_login()
    elif st.session_state['teacher_clicked']:
        show_teacher_login()
    elif st.session_state['admin_principal_clicked']:
        show_admin_principal_login()
    elif st.session_state['parent_clicked']:  
        show_parent_login()

    if st.session_state['admin_clicked'] or st.session_state['teacher_clicked'] or st.session_state['admin_principal_clicked'] or st.session_state['parent_clicked']:  # Ajoutez pour le parent
        if st.button("Retour"):
            st.session_state['admin_clicked'] = False
            st.session_state['teacher_clicked'] = False
            st.session_state['admin_principal_clicked'] = False
            st.session_state['parent_clicked'] = False  
            st.session_state['page'] = "Page des Comptes"  
            st.rerun()

if __name__ == "__main__":
    comptes_page()