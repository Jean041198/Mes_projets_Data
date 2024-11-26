import streamlit as st
from pages import page_d_evolution
import mysql.connector
import os


ADMIN_ID = "admin123"
ADMIN_PASSWORD = "password123"
TEACHER_ID = "teacher123"
TEACHER_PASSWORD = "password456"
ADMIN_PRINCIPAL_ID = "adminprincipal123" 
ADMIN_PRINCIPAL_PASSWORD = "password789"  

def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Fonction pour établir la connexion à la base de données
def get_db_connection():
    # Détecter l'environnement (Cloud ou local)
    if "STREAMLIT_CLOUD" in os.environ:
        # Si l'application est déployée sur Streamlit Cloud, utilisez Ngrok
        host = st.secrets["mysql"]["host"]
        port = st.secrets["mysql"]["port"]
    else:
        # En local, localhost et le port par défaut
        host = "127.0.0.1"
        port = 3306

    # Connexion à MySQL
    mydb = mysql.connector.connect(
        host=host,
        port=port,
        user=st.secrets["mysql"]["user"],
        password=st.secrets["mysql"]["password"],
        database=st.secrets["mysql"]["database"]
    )
    return mydb

# Fonction d'authentification
def authenticate_user(username, password, role):
    db = get_db_connection()
    cursor = db.cursor()

    # Vérifiez si l'utilisateur existe et si le mot de passe est correct
    if role == 'admin':
        sql = "SELECT * FROM administration WHERE identifiant = %s AND mot_de_passe = %s"
        cursor.execute(sql, (username, password))  # Passez les deux paramètres
    elif role == 'teacher':
        sql = "SELECT * FROM enseignants WHERE identifiant = %s AND mot_de_passe = %s"
        cursor.execute(sql, (username, password))  # Passez les deux paramètres
    elif role == 'admin_principal':
        sql = "SELECT * FROM administrateur_principal WHERE identifiant = %s AND mot_de_passe = %s"
        cursor.execute(sql, (username, password))  # Passez les deux paramètres
    elif role == 'parent':
        # Pour les parents, le mot de passe est le matricule de l'élève
        sql = "SELECT * FROM eleves WHERE matricule_eleve = %s"  
        cursor.execute(sql, (username,))  # Pas besoin de passer le mot de passe pour le parent
    else:
        return False, "Rôle invalide."

    result = cursor.fetchone()
    cursor.close()
    db.close()

    if result:
        return True, None
    else:
        return False, "Nom d'utilisateur ou mot de passe incorrect."

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
    parent_id = st.text_input("Matricule de l'enfant")  # Saisir le matricule de l'enfant

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
        st.image("static/images/logo.png", width=150)

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