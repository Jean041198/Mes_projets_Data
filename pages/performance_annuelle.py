import streamlit as st
import sqlite3
import seaborn as sns
import matplotlib.pyplot as plt
from statistics import mean, median, stdev

def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        6
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

def performance_annuelle_page():
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
            notes_eleve = get_notes_eleve_annuelles(matricule_eleve=matricule_eleve) 
            if notes_eleve:
                matieres = list(notes_eleve.keys())
                notes = list(notes_eleve.values())

                # Statistiques descriptives
                st.subheader("Statistiques descriptives")
                
                mediane = round(median(notes), 2)
                ecart_type = round(stdev(notes), 2) if len(notes) > 1 else "Non applicable"

                
                st.write(f"Médiane : {mediane}/20")
                st.write(f"Écart-type : {ecart_type}")

                # Interprétation statistique
                st.subheader("Interprétation statistique")
                st.write(f"La médiane des notes de l'élève est de {mediane}/20. Cela signifie que la moitié des notes de l'élève sont supérieures à "
                    f"{mediane} et l'autre moitié sont inférieures.")
                st.write(f"L'écart-type est de {ecart_type}. Un écart-type faible indique que les notes sont concentrées autour "
                    f"de la moyenne, tandis qu'un écart-type élevé indique une plus grande dispersion des notes.")

                # Graphique avec Seaborn
                st.subheader("Graphiques d'évolution")
                sns.set_theme(style="whitegrid")
                fig, ax = plt.subplots(figsize=(10, 6))
                sns.barplot(x=matieres, y=notes, ax=ax, color='orange')
                ax.set_title(f"Évolution des notes de {eleve_info['nom']} {eleve_info['prenom']}")
                ax.set_ylabel("Note /20")

                # Ajouter une courbe d'évolution des notes
                sns.lineplot(x=matieres, y=notes, ax=ax, color='black', marker='o')

                # Rotation des labels pour les matières pour éviter le chevauchement
                ax.set_xticklabels(matieres, rotation=45, ha='right')
                st.pyplot(fig)

                 # Calcul de la moyenne pondérée
                moyenne_ponderee = calculer_moyenne_ponderee(st.session_state['class'], notes_eleve)
                st.subheader("Moyenne de l'élève")
                st.write(f"Moyenne de l'élève : {moyenne_ponderee}/20")

                  # Interprétation de la moyenne pondérée
                if moyenne_ponderee != "Non applicable":
                    if moyenne_ponderee >= 14:
                        st.write(f"La moyenne  de l'élève est de {moyenne_ponderee}/20, ce qui correspond à une excellente performance. "
                            f"L'élève excelle dans ses études et maîtrise bien les différentes matières.")
                    elif 10 <= moyenne_ponderee < 14:
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
                    if note >= 14:
                        st.write(f"{matiere} : Excellente performance annuelle, continuez comme ça !Félicitations prof {enseignant_nom} pour votre travail effectuer tout au long de cette année scolaire!")
                    elif 10 <= note < 14:
                        st.write(f"{matiere} :  Performance annuelle satisfaisante, mais peut être améliorée.Prof {enseignant_nom}, encouragez l'élève à poursuivre ses efforts durant les vacances")
                    else:
                        st.write(f"{matiere} : Note annuelle insuffisante, un suivi rigoureux est nécessaire.Prof {enseignant_nom}, un suivi personnalisé pourrait être bénéfique via les cours de remise à niveau pendant les vacances.")
                    
                   

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
                notes_eleve = get_notes_eleve_annuelles(eleve_name=eleve_selectionne) 
                if notes_eleve:
                    matieres = list(notes_eleve.keys())
                    notes = list(notes_eleve.values())

                    # Statistiques descriptives
                    st.subheader("Statistiques descriptives")
    
                    mediane = round(median(notes), 2)
                    ecart_type = round(stdev(notes), 2) if len(notes) > 1 else "Non applicable"

                
                    st.write(f"Médiane : {mediane}/20")
                    st.write(f"Écart-type : {ecart_type}")

                    # Interprétation statistique
                    st.subheader("Interprétation statistique")
                    st.write(f"La médiane des notes de l'élève est de {mediane}/20. Cela signifie que la moitié des notes de l'élève sont supérieures à "
                         f"{mediane} et l'autre moitié sont inférieures.")
                    st.write(f"L'écart-type est de {ecart_type}. Un écart-type faible indique que les notes sont concentrées autour "
                         f"de la moyenne, tandis qu'un écart-type élevé indique une plus grande dispersion des notes.")


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
                    moyenne_ponderee = calculer_moyenne_ponderee(st.session_state['class'], notes_eleve)
                    st.subheader("Moyenne de l'élève")
                    st.write(f"Moyenne de l'élève : {moyenne_ponderee}/20")

                    # Interprétation de la moyenne pondérée
                    if moyenne_ponderee != "Non applicable":
                        if moyenne_ponderee >= 14:
                            st.write(f"La moyenne  de l'élève est de {moyenne_ponderee}/20, ce qui correspond à une excellente performance. "
                            f"L'élève excelle dans ses études et maîtrise bien les différentes matières.")
                        elif 10 <= moyenne_ponderee < 14:
                            st.write(f"La moyenne  de l'élève est de {moyenne_ponderee}/20, ce qui correspond à une performance satisfaisante. "
                            f"L'élève a un bon niveau général, mais il (elle) peut encore progresser dans certaines matières.")
                        else:
                            st.write(f"La moyenne  de l'élève est de {moyenne_ponderee}/20, ce qui correspond à une performance insuffisante. "
                            f"L'élève a des difficultés dans certaines matières et nécessite un suivi plus approfondi.")
                    else:
                        st.write("La moyenne  n'est pas disponible pour cet élève.")


                    # Prise de décision automatique
                    st.subheader("Prise de décision")
                    for matiere, note in notes_eleve.items():
                        enseignant_nom = get_enseignant_nom(matiere)  # Obtenir le nom de l'enseignant
                        if note >= 14:
                            st.write(f"{matiere} : Excellente performance annuelle, continuez comme ça !Félicitations prof {enseignant_nom} pour votre travail effectuer tout au long de cette année scolaire!")
                        elif 10 <= note < 14:
                            st.write(f"{matiere} :  Performance annuelle satisfaisante, mais peut être améliorée.Prof {enseignant_nom}, encouragez l'élève à poursuivre ses efforts durant les vacances")
                        else:
                            st.write(f"{matiere} : Note annuelle insuffisante, un suivi rigoureux est nécessaire.Prof {enseignant_nom}, un suivi personnalisé pourrait être bénéfique via les cours de remise à niveau pendant les vacances.")
                    
                         # Recommandation de cours de vacances
                        if note < 10:
                           st.write(f"**{matiere} : Recommandation de cours de vacances pour améliorer le niveau en {matiere}.**")

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
    db = get_db_connection()
    cursor = db.cursor()
    sql = "SELECT matricule_eleve, nom, prenom FROM eleves WHERE classe = %s"
    cursor.execute(sql, (class_name,))
    eleves = cursor.fetchall()
    cursor.close()
    db.close()

    return [f"{row[1]} {row[2]}" for row in eleves]  # Retourne une liste de noms complets




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
        return cursor.fetchone()[0] if cursor.fetchone() else "N/A"
    except (sqlite3.Error, IndexError) as e: #Gestion de l'erreur si fetchone() retourne None ou une liste vide.
        st.error(f"Erreur lors de la récupération du nom de l'enseignant : {e}")
        return "N/A"
    finally:
        cursor.close()
        conn.close()



# Fonction pour obtenir les informations d'un élève par son matricule
# Fonction pour obtenir les informations d'un élève par son matricule
def get_eleve_info(matricule_eleve):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        sql = "SELECT nom, prenom FROM eleves WHERE matricule_eleve = ?"
        cursor.execute(sql, (matricule_eleve,))
        result = cursor.fetchone()
        if result:
            return {"nom": result[0], "prenom": result[1]}
        else:
            return None  # Retourne None si aucun élève n'est trouvé
    except sqlite3.Error as e:
        st.error(f"Erreur lors de la récupération des informations de l'élève : {e}")
        return None
    finally:
        cursor.close()
        conn.close()

def get_eleves_from_class(class_name):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        sql = "SELECT matricule_eleve, nom, prenom FROM eleves WHERE classe = ?"
        cursor.execute(sql, (class_name,))
        eleves = cursor.fetchall()
        return [f"{row[1]} {row[2]}" for row in eleves]
    except sqlite3.Error as e:
        st.error(f"Erreur lors de la récupération des élèves : {e}")
        return []
    finally:
        conn.close()


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
        st.error(f"Erreur lors de la récupération du nom de l'enseignant : {e}")
        return "N/A"
    finally:
        conn.close()

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
        st.error(f"Erreur lors de la récupération des matières : {e}")
        return []
    finally:
        conn.close()


def enregistrer_notes_annuelles(class_name, eleves_selectionnes):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        for eleve_name in eleves_selectionnes:
            for matiere in get_matieres_for_class(class_name):
                note = st.session_state.get(f"note_{matiere['matiere']}")
                if note is not None: #Check if note is actually defined
                    matricule_eleve = get_matricule_by_nom_prenom(eleve_name)
                    if matricule_eleve:
                        sql = "INSERT INTO notes (matricule_eleve, matiere, note) VALUES (?, ?, ?)"
                        cursor.execute(sql, (matricule_eleve, matiere['matiere'], note))
                        note_id = cursor.lastrowid
                        sql = "INSERT INTO notes_annuelles (note_id) VALUES (?)"
                        cursor.execute(sql, (note_id,))
                        conn.commit()
    except sqlite3.Error as e:
        st.error(f"Erreur lors de l'enregistrement des notes : {e}")
    finally:
        conn.close()


def get_matricule_by_nom_prenom(eleve_name):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        sql = "SELECT matricule_eleve FROM eleves WHERE nom || ' ' || prenom = ?"
        cursor.execute(sql, (eleve_name,))
        result = cursor.fetchone()
        return result[0] if result else None
    except sqlite3.Error as e:
        st.error(f"Erreur lors de la récupération du matricule : {e}")
        return None
    finally:
        conn.close()

def get_notes_eleve_annuelles(eleve_name):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        sql = """
            SELECT n.matiere, n.note
            FROM notes n
            JOIN eleves e ON n.matricule_eleve = e.matricule_eleve
            JOIN notes_annuelles na ON n.id = na.note_id
            WHERE e.nom || ' ' || e.prenom = ?
        """
        cursor.execute(sql, (eleve_name,))
        notes = cursor.fetchall()
        return {row[0]: row[1] for row in notes}
    except sqlite3.Error as e:
        st.error(f"Erreur lors de la récupération des notes : {e}")
        return {}
    finally:
        conn.close()

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
                    JOIN notes_annuelles na ON n.id = na.note_id
                    WHERE n.matricule_eleve = ?
                """
                cursor.execute(sql, (matricule_eleve,))
                count = cursor.fetchone()[0]
                if count == 0:
                    return False
        return True
    except sqlite3.Error as e:
        st.error(f"Erreur lors de la vérification des notes : {e}")
        return False
    finally:
        conn.close()
    return True


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
    performance_annuelle_page()