import streamlit as st
import sqlite3
import seaborn as sns
import matplotlib.pyplot as plt
from statistics import mean, median, stdev

def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

DB_PATH = "utils/collegefoganggenies_db.sqlite"      

# Fonction pour établir la connexion à la base de données SQLite
def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    return conn

# Dictionnaire des coefficients par matière et classe
coefficients = {
    '6ème': {
        'Economie Social et Familiale(ESF)': 2,
        'Anglais': 3,
        'Latin': 2,
        'Sciences': 2,
        'Informatique': 2,
        'Mathématiques': 4,
        'Histoire': 2,
        'Expression ecrite/orale':2,
        'Correction orthographique':1,
        'Etude de texte': 1,
        'Espagnol': 2,
        'Sport': 2,
        'Langue et Culture Nationale': 1,
        'Éducation Civique et Morale (ECM)':2,
        'Géographie':2,
        'Travail manuel':1
    },
    '5ème': {
        'Economie Social et Familiale(ESF)': 2,
        'Anglais': 3,
        'Latin': 2,
        'Sciences': 2,
        'Informatique': 2,
        'Mathématiques': 4,
        'Histoire': 2,
        'Expression ecrite/orale':2,
        'Correction orthographique':1,
        'Etude de texte': 1,
        'Espagnol': 2,
        'Sport': 2,
        'Langue et Culture Nationale': 1,
        'Éducation Civique et Morale (ECM)':2,
        'Géographie':2,
        'Travail manuel':1
    },
    '4ème': {
        'Economie Social et Familiale(ESF)': 2,
        'Anglais': 3,
        'Latin': 1,
        'Sciences': 2,
        'Informatique': 2,
        'Mathématiques': 4,
        'Histoire': 2,
        'Expression ecrite/orale':2,
        'Correction orthographique':1,
        'Etude de texte': 1,
        'Espagnol': 2,
        'Sport': 2,
        'Langue et Culture Nationale': 1,
        'Physique Chimie Technologie': 2,
        'Éducation Civique et Morale (ECM)':2,
        'Géographie':2,
        'Travail manuel':1
    },
    'Form1': {
        'English Language': 4,
        'Food and Nutrition': 2,
        'literature': 2,
        'French': 4,
        'History': 2,
        'Geography': 2,
        'Citizenship': 2,
        'Mathematics': 4,
        'Chemistry': 2,
        'Biology': 2,
        'Computer Sciences': 2,
        'Sport': 2,
        'Physics': 2,
        'Manual labour':1
    },
    'Form2': {
        'English Language': 4,
        'Food and Nutrition': 2,
        'literature': 2,
        'French': 4,
        'History': 2,
        'Geography': 2,
        'Citizenship': 2,
        'Mathematics': 4,
        'Chemistry': 2,
        'Biology': 2,
        'Computer Sciences': 2,
        'Sport': 2,
        'Physics': 2,
        'Manual labour':1
    },
    'Form3': {
        'English Language': 4,
        'Food and Nutrition': 2,
        'literature': 2,
        'French': 4,
        'History': 2,
        'Geography': 2,
        'Citizenship': 2,
        'Mathematics': 4,
        'Chemistry': 2,
        'Biology': 2,
        'Computer Sciences': 2,
        'Sport': 2,
        'Physics': 2,
        'Economics': 2,
        'Commerce': 2,
        'Manual labour':1
    }
}

def performance_sequentielle_page():
    if 'class' not in st.session_state:
        st.session_state['class'] = None

    load_css("static/styles/styles.css")

    # Logo en haut de la page
    col1, col2, col3 = st.columns([1.5, 2, 0.5])
    with col2:
        st.image("static/images/logo.png", use_container_width=True)

    # Mode Visualisation des Performances (pas de saisie)
    st.title("Visualisation des performances et prise de décisions")

    # Vérifiez le rôle de l'utilisateur
    role = st.session_state.get('role')
    
    if role == 'parent':
        # Récupérez le matricule de l'élève depuis la session
        matricule_eleve = st.session_state['matricule_eleve'] 

        # Afficher les informations de l'élève
        eleve_info = get_eleve_info(matricule_eleve)
        if eleve_info:
            st.subheader(f"Notes de l'élève : {eleve_info['nom']} {eleve_info['prenom']}")
            
            # Afficher les notes de l'élève
            notes_eleve = get_notes_eleve_sequentielles(matricule_eleve=matricule_eleve) 
            if notes_eleve:
                matieres = list(notes_eleve.keys())
                notes = list(notes_eleve.values())

                # Statistiques descriptives
                st.subheader("Statistiques descriptives")
            
                mediane = round(median(notes), 2)
               

                
                st.write(f"Médiane : {mediane}/20")
               

                # Interprétation statistique
                st.subheader("Interprétation statistique")
                st.write(f"La médiane des notes de l'élève est de {mediane}/20. Cela signifie que la moitié des notes de l'élève sont supérieures à "
                         f"{mediane} et l'autre moitié sont inférieures.")
                
                # Graphique avec Seaborn
                st.subheader("Graphiques d'évolution des notes de l'élève ")
                sns.set_theme(style="whitegrid")
                fig, ax = plt.subplots(figsize=(10, 6))
                sns.barplot(x=matieres, y=notes, ax=ax, color='orange')
                ax.set_title(f"Évolution des notes de {eleve_info['nom']} {eleve_info['prenom']}")
                ax.set_ylabel("Note /20")

                 # Définir les ticks et les labels
                ax.set_xticks(range(len(matieres)))  # Définit les ticks
                ax.set_xticklabels(matieres, rotation=45, ha='right')  # Définit les labels

                # Ajouter une courbe d'évolution des notes
                sns.lineplot(x=matieres, y=notes, ax=ax, color='black', marker='o')

                # Rotation des labels pour les matières pour éviter le chevauchement
                ax.set_xticklabels(matieres, rotation=45, ha='right')
                st.pyplot(fig)
                

                # Calcul de la moyenne pondérée
                st.subheader("MOYENNE GENERALE DE L'ELEVE")
                moyenne_ponderee = calculer_moyenne_ponderee(st.session_state['class'], notes_eleve)
                
                st.write(f"Moyenne de l'élève : {moyenne_ponderee}/20")

               # Interprétation de la moyenne pondérée
                if moyenne_ponderee != "Non applicable":
                    if moyenne_ponderee >= 15:
                        st.write(f"La moyenne  de l'élève est de {moyenne_ponderee}/20, ce qui correspond à une excellente performance. "
                            f"L'élève excelle dans ses études et maîtrise bien les différentes matières.")
                    elif 10 <= moyenne_ponderee < 15:
                        st.write(f"La moyenne  de l'élève est de {moyenne_ponderee}/20, ce qui correspond à une performance satisfaisante. "
                            f"L'élève a un bon niveau général, mais il (elle) peut encore progresser dans certaines matières.")
                    else:
                        st.write(f"La moyenne  de l'élève est de {moyenne_ponderee}/20, ce qui correspond à une performance insuffisante. "
                        f"L'élève a des difficultés dans certaines matières et nécessite un suivi plus approfondi.")
                else:
                     st.write("La moyenne  n'est pas disponible pour cet élève.")

                # Prise de décision automatique
                st.subheader("Prise de décision sur chaque matière")
                for matiere, note in notes_eleve.items():
                    enseignant_nom = get_enseignant_nom(matiere)  # Obtenir le nom de l'enseignant
                    if note >= 15:
                        st.write(f"{matiere} : Excellente performance, continuez comme ça ! Félicitations prof {enseignant_nom} pour votre travail!")
                    elif 10 <= note < 15:
                        st.write(f"{matiere} : Performance satisfaisante, mais peut être améliorée. Prof {enseignant_nom}, encouragez l'élève à poursuivre ses efforts.")
                    else:
                        st.write(f"{matiere} : Note insuffisante, un suivi rigoureux est nécessaire. Prof {enseignant_nom}, un suivi personnalisé pourrait être bénéfique.")
                    
                    # Comparer aux notes précédentes
                    if st.session_state['sequence'] > 1:
                        notes_precedentes = get_notes_eleve_precedentes(matricule_eleve=matricule_eleve, matiere=matiere, sequence_precedente=st.session_state['sequence'] - 1)
                        if notes_precedentes:
                            note_precedente = notes_precedentes[0][0] if notes_precedentes else None
                            if note_precedente is not None:
                                if note > note_precedente:
                                    st.write(f"**{matiere} : L'élève a progressé par rapport à la séquence précédente.**")
                                elif note == note_precedente:
                                    st.write(f"**{matiere} : L'élève a maintenu un niveau stable par rapport à la séquence précédente.**")
                                else:
                                    st.write(f"**{matiere} : L'élève a régressé par rapport à la séquence précédente.**")

            else:
                st.warning(f"Aucune note pour l'élève {eleve_info['nom']} {eleve_info['prenom']}")

    elif role in ['admin', 'admin_principal']:
        # Récupérer les élèves de la classe sélectionnée
        eleves = get_eleves_from_class(st.session_state['class'])
        if eleves:
            st.subheader("Sélectionnez les élèves")
            eleve_selectionne = st.selectbox("Élève", eleves, key="select_eleve", index=None)  

            # Afficher les éléments si un élève est sélectionné
            if eleve_selectionne:  
                st.subheader(f"Notes de l'élève : {eleve_selectionne}")
                
                # Afficher les notes de l'élève
                notes_eleve = get_notes_eleve_sequentielles(eleve_name=eleve_selectionne) 
                if notes_eleve:
                    matieres = list(notes_eleve.keys())
                    notes = list(notes_eleve.values())

                    # Statistiques descriptives
                    st.subheader("Statistiques descriptives")
                    
                    mediane = round(median(notes), 2)
                    

                    
                    st.write(f"Médiane : {mediane}/20")
                 


                   # Interprétation statistique
                    st.subheader("Interprétation statistique")
                    st.write(f"La médiane des notes de l'élève est de {mediane}/20. Cela signifie que la moitié des notes de l'élève sont supérieures à "
                         f"{mediane} et l'autre moitié sont inférieures.")
                    
                    # Graphique avec Seaborn
                    st.subheader("Graphiques d'évolution")
                    sns.set_theme(style="whitegrid")
                    fig, ax = plt.subplots(figsize=(10, 6))
                    sns.barplot(x=matieres, y=notes, ax=ax, color='orange')
                    ax.set_title(f"Évolution des notes de {eleve_selectionne}")
                    ax.set_ylabel("Note /20")

                    # Ajouter une courbe d'évolution des notes
                    sns.lineplot(x=matieres, y=notes, ax=ax, color='black', marker='o')

                    # Rotation des labels pour les matières pour éviter le chevauchement
                    ax.set_xticklabels(matieres, rotation=45, ha='right')
                    st.pyplot(fig)

                     # Calcul de la moyenne pondérée
                    st.subheader("MOYENNE GENERALE DE L'ELEVE")
                    moyenne_ponderee = calculer_moyenne_ponderee(st.session_state['class'], notes_eleve)
                    st.write(f"Moyenne de l'élève : {moyenne_ponderee}/20")

                     # Interprétation de la moyenne pondérée
                    if moyenne_ponderee != "Non applicable":
                        if moyenne_ponderee >= 14:
                            st.write(f"La moyenne  de l'élève est de {moyenne_ponderee}/20, ce qui correspond à une excellente performance. "
                            f"L'élève excelle dans ses études et maîtrise bien les différentes matières.")
                        elif 10 <= moyenne_ponderee < 14:
                            st.write(f"La moyenne de l'élève est de {moyenne_ponderee}/20, ce qui correspond à une performance satisfaisante. "
                            f"L'élève a un bon niveau général, mais il (elle) peut encore progresser dans certaines matières.")
                        else:
                            st.write(f"La moyenne de l'élève est de {moyenne_ponderee}/20, ce qui correspond à une performance insuffisante. "
                            f"L'élève a des difficultés dans certaines matières et nécessite un suivi plus approfondi.")
                    else:
                        st.write("La moyenne n'est pas disponible pour cet élève.")


                    # Prise de décision automatique
                    st.subheader("Prise de décision sur chaque matière")
                    for matiere, note in notes_eleve.items():
                        enseignant_nom = get_enseignant_nom(matiere)  # Obtenir le nom de l'enseignant
                        if note >= 14:
                            st.write(f"{matiere} : Excellente performance, continuez comme ça ! Félicitations prof {enseignant_nom} pour votre travail!")
                        elif 10 <= note < 14:
                            st.write(f"{matiere} : Performance satisfaisante, mais peut être améliorée. Prof {enseignant_nom}, encouragez l'élève à poursuivre ses efforts.")
                        else:
                            st.write(f"{matiere} : Note insuffisante, un suivi rigoureux est nécessaire. Prof {enseignant_nom}, un suivi personnalisé pourrait être bénéfique.")
                    
                        # Comparer aux notes précédentes
                        if st.session_state['sequence'] > 1:
                            notes_precedentes = get_notes_eleve_precedentes(matricule_eleve=matricule_eleve, matiere=matiere, sequence_precedente=st.session_state['sequence'] - 1)
                            if notes_precedentes:
                                note_precedente = notes_precedentes[0][0] if notes_precedentes else None
                                if note_precedente is not None:
                                    if note > note_precedente:
                                        st.write(f"**{matiere} : L'élève a progressé par rapport à la séquence précédente.**")
                                    elif note == note_precedente:
                                        st.write(f"**{matiere} : L'élève a maintenu un niveau stable par rapport à la séquence précédente.**")
                                    else:
                                        st.write(f"**{matiere} : L'élève a régressé par rapport à la séquence précédente.**")

                else:
                    st.warning(f"Aucune note pour l'élève {eleve_selectionne}")

        else:
            st.warning("Aucun élève dans cette classe.")

    if st.button("Retour", key="retour_visualisation"):  
        if role == 'parent':
            st.session_state['page'] = "Page d'évolution"  # Retourne vers la page d'évolution
            st.rerun()
        else:
            st.session_state['page'] = "Page des Classes"  
            st.rerun()
    
    # Appliquer la classe CSS au bouton "Retour"
    role = st.session_state.get('role')
    if role == 'admin_principal':
        st.markdown(f'<style>.stButton > div > button {{background-color: green !important; color: white !important; border: none !important; padding: 10px 20px !important; text-align: center !important; text-decoration: none !important; display: inline-block !important; font-size: 16px !important; margin: 4px 2px !important; cursor: pointer !important;}}</style>', unsafe_allow_html=True)
    elif role == 'admin':
        st.markdown(f'<style>.stButton > div > button {{background-color: blue !important; color: white !important; border: none !important; padding: 10px 20px !important; text-align: center !important; text-decoration: none !important; display: inline-block !important; font-size: 16px !important; margin: 4px 2px !important; cursor: pointer !important;}}</style>', unsafe_allow_html=True)

# Fonction pour obtenir les élèves d'une classe
def get_eleves_from_class(class_name):
    conn = get_db_connection()
    cursor = conn.cursor()
    sql = "SELECT matricule_eleve, nom, prenom FROM eleves WHERE classe = ?"
    cursor.execute(sql, (class_name,))
    eleves = cursor.fetchall()
    conn.close()
    return [f"{row[1]} {row[2]}" for row in eleves]  # Retourne une liste de noms complets




# Fonction pour obtenir le nom de l'enseignant à partir d'une matière
def get_enseignant_nom(matiere):
    conn = get_db_connection()
    cursor = conn.cursor()
    sql = """
        SELECT e.nom
        FROM enseignants e
        JOIN matieres_des_enseignants me ON e.identifiant = me.identifiant_enseignant
        WHERE me.matiere_enseignee = ?
    """
    cursor.execute(sql, (matiere,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else "N/A"


def get_eleve_info(matricule_eleve):
    conn = get_db_connection()
    cursor = conn.cursor()
    sql = "SELECT nom, prenom FROM eleves WHERE matricule_eleve = ?"
    cursor.execute(sql, (matricule_eleve,))
    result = cursor.fetchone()
    conn.close()
    if result:
        return {"nom": result[0], "prenom": result[1]}
    else:
        return None

def get_matieres_for_class(class_name):
    conn = get_db_connection()
    cursor = conn.cursor()
    sql = """
        SELECT me.matiere_enseignee, IFNULL(e.nom, 'N/A') AS nom_enseignant
        FROM matieres_des_enseignants me
        LEFT JOIN enseignants e ON me.identifiant_enseignant = e.identifiant
        LEFT JOIN enseignants_classes ec ON me.identifiant_enseignant = ec.identifiant_enseignant
        WHERE ec.nom_de_la_classe = ? AND (me.classe_specifique IS NULL OR me.classe_specifique = ?)
    """
    cursor.execute(sql, (class_name, class_name))
    matieres = cursor.fetchall()
    conn.close()
    matieres_list = [{"matiere": row[0], "nom": row[1]} for row in matieres]
    if class_name in ['6ème', '5ème', '4ème']:
        matieres_list.append({"matiere": "Travail manuel", "nom": "N/A"})
    elif class_name in ['Form1', 'Form2', 'Form3']:
        matieres_list.append({"matiere": "Manual labour", "nom": "N/A"})
    return matieres_list

def get_notes_eleve_sequentielles(eleve_name=None, matricule_eleve=None):
    conn = get_db_connection()
    cursor = conn.cursor()
    if matricule_eleve is not None:
        sql = """
            SELECT n.matiere, n.note
            FROM notes n
            JOIN eleves e ON n.matricule_eleve = e.matricule_eleve
            WHERE n.matricule_eleve = ?
        """
        cursor.execute(sql, (matricule_eleve,))
    else:
        sql = """
            SELECT n.matiere, n.note
            FROM notes n
            JOIN eleves e ON n.matricule_eleve = e.matricule_eleve
            WHERE e.nom || ' ' || e.prenom = ?
        """
        cursor.execute(sql, (eleve_name,))
    notes = cursor.fetchall()
    conn.close()
    return {row[0]: row[1] for row in notes}

def get_notes_eleve_precedentes(matricule_eleve, matiere, sequence_precedente):
    conn = get_db_connection()
    cursor = conn.cursor()
    sql = """
        SELECT n.note
        FROM notes n
        JOIN notes_sequentielles ns ON n.id = ns.note_id
        WHERE n.matricule_eleve = ? AND n.matiere = ? AND ns.sequence = ?
    """
    cursor.execute(sql, (matricule_eleve, matiere, sequence_precedente))
    result = cursor.fetchall()
    conn.close()
    return result

def calculer_moyenne_ponderee(class_name, notes):
    somme_ponderee = 0
    somme_coefficients = 0
    for matiere, note in notes.items():
        coefficient = coefficients.get(class_name, {}).get(matiere, 1)
        somme_ponderee += note * coefficient
        somme_coefficients += coefficient
    moyenne_ponderee = round(somme_ponderee / somme_coefficients, 2) if somme_coefficients > 0 else "Non applicable"
    return moyenne_ponderee




if __name__ == "__main__":
    performance_sequentielle_page()