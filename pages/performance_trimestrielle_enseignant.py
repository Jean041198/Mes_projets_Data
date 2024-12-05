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
        'Langue et culture nationale': 1,
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
        'Langue et culture nationale': 1,
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
        'Langue et culture nationale': 1,
        'Physique chimie technologie': 2,
        'Éducation Civique et Morale (ECM)':2,
        'Géographie':2,
        'Travail manuel':1
    },
    'Form 1': {
        'English Language': 4,
        'Food and Nutrition': 2,
        'Literature': 2,
        'French': 4,
        'History': 2,
        'Geography': 2,
        'Citizenship': 2,
        'Mathematics': 2,
        'Chemistry': 2,
        'Biology': 2,
        'Computer Sciences': 2,
        'Sport': 2,
        'Physics': 2,
        'Manual labour':1
    },
    'Form 2': {
        'English Language': 4,
        'Food and Nutrition': 2,
        'Literature': 2,
        'French': 4,
        'History': 2,
        'Geography': 2,
        'Citizenship': 2,
        'Mathematics': 2,
        'Chemistry': 2,
        'Biology': 2,
        'Computer Sciences': 2,
        'Sport': 2,
        'Physics': 2,
        'Manual labour':1
    },
    'Form 3': {
        'English Language': 4,
        'Food and Nutrition': 2,
        'Literature': 2,
        'French': 4,
        'History': 2,
        'Geography': 2,
        'Citizenship': 2,
        'Mathematics': 2,
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


def performance_trimestrielle_enseignant_page():
    if 'class' not in st.session_state:
        st.session_state['class'] = None

    load_css("static/styles/styles.css")

    # Logo en haut de la page
    col1, col2, col3 = st.columns([1.5, 2, 0.5])
    with col2:
        st.image("static/images/logo.png", width=150)

    # Mode Saisie des Notes
    if not st.session_state.get('visualisation_mode', False):
        st.title("Performance Trimestrielle")

        # Récupérer les élèves de la classe sélectionnée
        eleves = get_eleves_from_class(st.session_state['class'])
        if eleves:
            st.subheader("Sélectionnez les élèves")
            eleves_selectionnes = st.multiselect("Sélectionnez les élèves", eleves, key="multiselect_eleves")

            if eleves_selectionnes:
                st.subheader("Matières")

                # Afficher les champs de saisie et les enseignants
                matieres = get_matieres_for_class(st.session_state['class'])
                afficher_champs_et_enseignants(matieres)

                # Enregistrer les notes dans la base de données
                if st.button("Enregistrer"):
                    enregistrer_notes_trimestrielles(st.session_state['class'], eleves_selectionnes)
                    st.success("Les informations ont été enregistrées.")

        else:
            st.warning("Aucun élève dans cette classe.")

        col1, col2 = st.columns([1, 1])
        with col1:
            if st.button("Retour", key="retour_saisie"):
                st.session_state['page'] = "Page des Classes"
                st.rerun()
        with col2:
            if st.button("Visualisation des performances", key="visualisation"):
                # Vérifier si toutes les notes ont été saisies et enregistrées dans la BD
                if notes_enregistrees(st.session_state['class'], eleves_selectionnes):
                    st.session_state['visualisation_mode'] = True
                    st.rerun()
                else:
                    st.warning("Veuillez remplir toutes les notes avant d'accéder à la visualisation des performances.")

    # Mode Visualisation des Performances
    else:
        visualisation_performance()


def visualisation_performance():
    st.title("Visualisation des performances et prise de décisions")

    # Récupérer les élèves de la classe sélectionnée
    eleves = get_eleves_from_class(st.session_state['class'])
    if eleves:
        st.subheader("Sélectionnez les élèves")
        eleve_selectionne = st.selectbox("Élève", eleves, key="select_eleve", index=None)  

        if eleve_selectionne:
            st.subheader(f"Notes de l'élève : {eleve_selectionne}")

            # Afficher les notes de l'élève
            notes_eleve = get_notes_eleve_trimestrielles(eleve_selectionne)
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
                ax.set_title(f"Évolution des notes de {eleve_selectionne}")
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
                     st.write("La moyenne de l'élève n'est pas disponible pour cet élève.")

                # Prise de décision automatique
                st.subheader("Prise de décision sur chaque matière")
                for matiere, note in notes_eleve.items():
                    enseignant_nom = get_enseignant_nom(matiere)    
                    if note >= 14:
                        st.write(f"{matiere} : Excellente performance, continuez comme ça ! Félicitations prof {enseignant_nom} pour votre travail!")
                    elif 10 <= note < 14:
                        st.write(f"{matiere} : Performance satisfaisante, mais peut être améliorée. Prof {enseignant_nom}, encouragez l'élève à poursuivre ses efforts.")
                    else:
                        st.write(f"{matiere} : Note insuffisante, un suivi rigoureux est nécessaire.Prof {enseignant_nom}, un suivi personnalisé pourrait être bénéfique.")

                    # Comparer aux notes des trimestres précédents (si disponibles)
                    if st.session_state['trimestre'] > 1:
                        notes_precedentes = get_notes_eleve_precedentes_trimestre(eleve_selectionne, matiere, st.session_state['trimestre'] - 1)
                        if notes_precedentes:
                            note_precedente = notes_precedentes[0][0] if notes_precedentes else None
                            if note_precedente is not None:
                                if note > note_precedente:
                                    st.write(f"**{matiere} : L'élève a progressé par rapport au trimestre précédent.**")
                                elif note == note_precedente:
                                    st.write(f"**{matiere} : L'élève a maintenu un niveau stable par rapport au trimestre précédent.**")
                                else:
                                    st.write(f"**{matiere} : L'élève a régressé par rapport au trimestre précédent.**")

            else:
                st.warning(f"Aucune note pour l'élève {eleve_selectionne}")

    else:
        st.warning("Aucun élève dans cette classe.")

    if st.button("Retour", key="retour_visualisation"):
        st.session_state['visualisation_mode'] = False
        st.session_state['page'] = "Performance Trimestrielle Enseignant"
        st.rerun()

# Fonction pour afficher les champs de saisie et les enseignants
def afficher_champs_et_enseignants(matieres):
    matieres_ajoutees = []  # Créez une liste pour suivre les matières déjà ajoutées
    for matiere_data in matieres:
        matiere = matiere_data['matiere']
        
        # Vérifiez si la matière est déjà dans la liste avant de l'ajouter
        if matiere not in matieres_ajoutees: 
            matieres_ajoutees.append(matiere)  # Ajoutez la matière à la liste
            # Champ de saisie avec validation de la note
            note = st.number_input(f"{matiere} /20", min_value=0, max_value=20, key=f"note_{matiere}") 

            # Afficher le nom de l'enseignant avec un expandeur pour les détails
            enseignant_nom = matiere_data.get('nom')
            infos_suppl = get_enseignant_infos(matiere)
            with st.expander(f"Enseignant : {enseignant_nom}"):
                st.write(f"**Nom** : {enseignant_nom}")
               

# Fonction pour obtenir les élèves d'une classe
def get_eleves_from_class(class_name):
    conn = get_db_connection()
    cursor = conn.cursor()
    sql = "SELECT matricule_eleve, nom, prenom FROM eleves WHERE classe = ?"
    cursor.execute(sql, (class_name,))
    eleves = cursor.fetchall()
    conn.close()
    return [f"{row[1]} {row[2]}" for row in eleves]  # Retourne une liste de noms complets


# Fonction pour obtenir les matières enseignées dans une classe
def get_matieres_for_class(class_name):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        sql = """
            SELECT me.matiere_enseignee, IFNULL(e.nom, 'N/A') AS nom_enseignant
            FROM matieres_des_enseignants me
            LEFT JOIN enseignants e ON me.identifiant_enseignant = e.identifiant
            LEFT JOIN enseignants_classes ec ON me.identifiant_enseignant = ec.identifiant_enseignant
            WHERE ec.nom_de_la_classe = ? AND (me.classe_specifique IS NULL OR me.classe_specifique = ?)
        """
        cursor.execute(sql, (class_name, class_name))
        matieres = cursor.fetchall()
        matieres_list = [{"matiere": row[0], "nom": row[1]} for row in matieres]
        if class_name in ['6ème', '5ème', '4ème']:
            matieres_list.append({"matiere": "Travail manuel", "nom": "N/A"})
        elif class_name in ['Form1', 'Form2', 'Form3']:
            matieres_list.append({"matiere": "Manual labour", "nom": "N/A"})
        return matieres_list
    except sqlite3.Error as e:
        st.error(f"Erreur lors de la récupération des matières : {e}")
        return []
    finally:
        cursor.close()
        conn.close()

# Fonction pour enregistrer les notes dans la base de données
def enregistrer_notes_trimestrielles(class_name, eleves_selectionnes):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        for eleve_name in eleves_selectionnes:
            for matiere_data in get_matieres_for_class(class_name):
                matiere = matiere_data['matiere']
                note = st.session_state.get(f"note_{matiere}") # Correction ici
                if note is not None: # Vérification supplémentaire pour la note
                    matricule_eleve = get_matricule_by_nom_prenom(eleve_name)
                    if matricule_eleve:
                        sql = "INSERT INTO notes (matricule_eleve, matiere, note) VALUES (?, ?, ?)"
                        cursor.execute(sql, (matricule_eleve, matiere, note))
                        note_id = cursor.lastrowid
                        sql = "INSERT INTO notes_trimestrielles (note_id, trimestre) VALUES (?, ?)"
                        cursor.execute(sql, (note_id, st.session_state['trimestre']))
                        conn.commit()
    except sqlite3.Error as e:
        st.error(f"Erreur lors de l'enregistrement des notes : {e}")
    finally:
        cursor.close()
        conn.close()

# Fonction pour trouver le matricule d'un élève par son nom et prénom
def get_matricule_by_nom_prenom(eleve_name):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        sql = "SELECT matricule_eleve FROM eleves WHERE nom || ' ' || prenom = ?"
        cursor.execute(sql, (eleve_name,))
        result = cursor.fetchone()
        return result[0] if result else None
    except sqlite3.Error as e:
        st.error(f"Erreur lors de la récupération du matricule : {e}")
        return None
    finally:
        cursor.close()
        conn.close()


# Fonction pour obtenir les notes d'un élève
def get_notes_eleve_trimestrielles(eleve_name):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        sql = """
            SELECT n.matiere, n.note
            FROM notes n
            JOIN eleves e ON n.matricule_eleve = e.matricule_eleve
            JOIN notes_trimestrielles nt ON n.id = nt.note_id
            WHERE e.nom || ' ' || e.prenom = ? AND nt.trimestre = ?
        """
        cursor.execute(sql, (eleve_name, st.session_state['trimestre']))
        notes = cursor.fetchall()
        return {row[0]: row[1] for row in notes}
    except sqlite3.Error as e:
        st.error(f"Erreur lors de la récupération des notes : {e}")
        return {}
    finally:
        cursor.close()
        conn.close()

# Fonction pour obtenir les informations de l'enseignant pour une matière donnée
def get_enseignant_infos(matiere):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        sql = """
            SELECT e.nom
            FROM enseignants e
            JOIN matieres_des_enseignants me ON e.identifiant = me.identifiant_enseignant
            WHERE me.matiere_enseignee = ?
               AND (me.classe_specifique IS NULL OR me.classe_specifique = ?)
        """
        cursor.execute(sql, (matiere, st.session_state['class']))
        result = cursor.fetchone()
        return result[0] if result else "N/A"
    except sqlite3.Error as e:
        st.error(f"Erreur lors de la récupération des infos de l'enseignant : {e}")
        return "N/A"
    finally:
        cursor.close()
        conn.close()

# Fonction pour obtenir le nom de l'enseignant à partir d'une matière
def get_enseignant_nom(matiere):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        sql = """
            SELECT e.nom
            FROM enseignants e
            JOIN matieres_des_enseignants me ON e.identifiant = me.identifiant_enseignant
            WHERE me.matiere_enseignee = ?
        """
        cursor.execute(sql, (matiere,))
        result = cursor.fetchone()
        return result[0] if result else "N/A"
    except sqlite3.Error as e:
        st.error(f"Erreur lors de la récupération du nom de l'enseignant : {e}")
        return "N/A"
    finally:
        cursor.close()
        conn.close()

# Fonction pour vérifier si les notes ont été enregistrées
def notes_enregistrees(class_name, eleves_selectionnes):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        for eleve_name in eleves_selectionnes:
            matricule_eleve = get_matricule_by_nom_prenom(eleve_name)
            if matricule_eleve:
                sql = """
                    SELECT COUNT(*) 
                    FROM notes n
                    JOIN notes_trimestrielles nt ON n.id = nt.note_id
                    WHERE n.matricule_eleve = ? AND nt.trimestre = ?
                """
                cursor.execute(sql, (matricule_eleve, st.session_state['trimestre']))
                count = cursor.fetchone()[0]
                if count == 0:
                    return False
        return True
    except sqlite3.Error as e:
        st.error(f"Erreur lors de la vérification des notes : {e}")
        return False
    finally:
        cursor.close()
        conn.close()

# Fonction pour obtenir les notes précédentes d'un élève pour une matière dans un trimestre
def get_notes_eleve_precedentes_trimestre(eleve_name, matiere, trimestre_precedent):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        sql = """
            SELECT n.note
            FROM notes n
            JOIN eleves e ON n.matricule_eleve = e.matricule_eleve
            JOIN notes_trimestrielles nt ON n.id = nt.note_id
            WHERE e.nom || ' ' || e.prenom = ? AND n.matiere = ? AND nt.trimestre = ?
        """
        cursor.execute(sql, (eleve_name, matiere, trimestre_precedent))
        result = cursor.fetchall()
        return result
    except sqlite3.Error as e:
        st.error(f"Erreur lors de la récupération des notes précédentes : {e}")
        return []
    finally:
        cursor.close()
        conn.close()
    return result



# Fonction pour calculer la moyenne pondérée
def calculer_moyenne_ponderee(class_name, notes_eleve):
    somme_ponderee = 0
    somme_coefficients = 0

    for matiere, note in notes_eleve.items():
        coefficient = coefficients.get(class_name, {}).get(matiere, 1)  # Coefficient par défaut à 1 si non trouvé
        somme_ponderee += note * coefficient
        somme_coefficients += coefficient

    moyenne_ponderee = round(somme_ponderee / somme_coefficients, 2) if somme_coefficients > 0 else "Non applicable"

    
    return moyenne_ponderee




if __name__ == "__main__":
    performance_trimestrielle_enseignant_page()