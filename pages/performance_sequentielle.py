import streamlit as st
import mysql.connector
import seaborn as sns
import matplotlib.pyplot as plt
from statistics import mean, median, stdev

def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def get_db_connection():
    mydb = mysql.connector.connect(
        host=st.secrets["mysql"]["host"],  # Accéder au secret stocké dans secrets.toml
        user=st.secrets["mysql"]["user"],  # Accéder au secret stocké dans secrets.toml
        password=st.secrets["mysql"]["password"],  # Accéder au secret stocké dans secrets.toml
        database=st.secrets["mysql"]["database"]  # Accéder au secret stocké dans secrets.toml
    )
    return mydb

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


def performance_sequentielle_page():
    if 'class' not in st.session_state:
        st.session_state['class'] = None

    load_css("static/styles/styles.css")

    # Logo en haut de la page
    col1, col2, col3 = st.columns([1.5, 2, 0.5])
    with col2:
        st.image("static/images/logo.png", width=150)

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
                moyenne_ponderee = calculer_moyenne_ponderee(st.session_state['class'], notes_eleve)
                st.subheader("Moyenne de l'élève")
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
    db = get_db_connection()
    cursor = db.cursor()
    sql = "SELECT matricule_eleve, nom, prenom FROM eleves WHERE classe = %s"
    cursor.execute(sql, (class_name,))
    eleves = cursor.fetchall()
    cursor.close()
    db.close()

    return [f"{row[1]} {row[2]}" for row in eleves]  # Retourne une liste de noms complets




# Fonction pour obtenir le nom de l'enseignant à partir d'une matière
def get_enseignant_nom(matiere):
    db = get_db_connection()
    cursor = db.cursor()
    sql = """
        SELECT e.nom
        FROM enseignants e
        JOIN matieres_des_enseignants me ON e.identifiant = me.identifiant_enseignant
        WHERE me.matiere_enseignee = %s
    """
    cursor.execute(sql, (matiere,))
    result = cursor.fetchone()
    cursor.close()
    db.close()

    return result[0] if result else "N/A"



# Fonction pour obtenir les informations d'un élève par son matricule
def get_eleve_info(matricule_eleve):
    db = get_db_connection()
    cursor = db.cursor()
    sql = "SELECT nom, prenom FROM eleves WHERE matricule_eleve = %s"
    cursor.execute(sql, (matricule_eleve,))
    result = cursor.fetchone()
    cursor.close()
    db.close()

    if result:
        return {"nom": result[0], "prenom": result[1]}
    else:
        return None

# Fonction pour obtenir les matières enseignées dans une classe
def get_matieres_for_class(class_name):
    db = get_db_connection()
    cursor = db.cursor()

    # Requête SQL pour récupérer les matières et les noms d'enseignants
    sql = """
        SELECT me.matiere_enseignee, IFNULL(e.nom, 'N/A') AS nom_enseignant
        FROM matieres_des_enseignants me
        LEFT JOIN enseignants e ON me.identifiant_enseignant = e.identifiant
        LEFT JOIN enseignants_classes ec ON me.identifiant_enseignant = ec.identifiant_enseignant
        WHERE ec.nom_de_la_classe = %s AND (me.classe_specifique IS NULL OR me.classe_specifique = %s)
    """
    cursor.execute(sql, (class_name, class_name))
    matieres = cursor.fetchall()
    cursor.close()
    db.close()

    # Ajouter "Travail manuel" ou "Manual labour" à la liste existante
    matieres_list = [{"matiere": row[0], "nom": row[1]} for row in matieres]
    if class_name in ['6ème', '5ème', '4ème']:
        matieres_list.append({"matiere": "Travail manuel", "nom": "N/A"})
    elif class_name in ['Form1', 'Form2', 'Form3']:
        matieres_list.append({"matiere": "Manual labour", "nom": "N/A"})

    return matieres_list

# Fonction pour enregistrer les notes dans la base de données
def enregistrer_notes_sequentielles(class_name, eleves_selectionnes):
    db = get_db_connection()
    cursor = db.cursor()

    for eleve_name in eleves_selectionnes:
        for matiere in get_matieres_for_class(class_name):
            note = st.session_state.get(f"note_{matiere['matiere']}")
            if note:
                matricule_eleve = get_matricule_by_nom_prenom(eleve_name)
                if matricule_eleve:
                    # Insérer la note dans la base de données
                    sql = "INSERT INTO notes (matricule_eleve, matiere, note) VALUES (%s, %s, %s)"
                    cursor.execute(sql, (matricule_eleve, matiere['matiere'], note))
                    db.commit()

                    note_id = cursor.lastrowid

                    # Insérer la relation dans la table 'notes_sequentielles'
                    sql = "INSERT INTO notes_sequentielles (note_id, sequence) VALUES (%s, %s)"
                    cursor.execute(sql, (note_id, st.session_state['sequence']))
                    db.commit()

    cursor.close()
    db.close()

# Fonction pour trouver le matricule d'un élève par son nom et prénom
def get_matricule_by_nom_prenom(eleve_name):
    db = get_db_connection()
    cursor = db.cursor()
    sql = "SELECT matricule_eleve FROM eleves WHERE CONCAT(nom, ' ', prenom) = %s"
    cursor.execute(sql, (eleve_name,))
    result = cursor.fetchone()
    cursor.close()
    db.close()

    return result[0] if result else None


def get_notes_eleve_sequentielles(eleve_name=None, matricule_eleve=None):
    db = get_db_connection()
    cursor = db.cursor()

    if matricule_eleve is not None:
        # Utiliser le matricule de l'élève (pour le parent)
        sql = """
            SELECT n.matiere, n.note
            FROM notes n
            JOIN eleves e ON n.matricule_eleve = e.matricule_eleve
            WHERE n.matricule_eleve = %s
        """
        cursor.execute(sql, (matricule_eleve,))
    else:
        # Utiliser le nom de l'élève (pour l'admin et l'admin principal)
        sql = """
            SELECT n.matiere, n.note
            FROM notes n
            JOIN eleves e ON n.matricule_eleve = e.matricule_eleve
            WHERE CONCAT(e.nom, ' ', e.prenom) = %s
        """
        cursor.execute(sql, (eleve_name,))

    notes = cursor.fetchall()
    cursor.close()
    db.close()

    return {row[0]: row[1] for row in notes}
# Fonction pour obtenir les informations de l'enseignant pour une matière donnée
def get_enseignant_infos(matiere):
    db = get_db_connection()
    cursor = db.cursor()
    sql = """
        SELECT e.nom
        FROM enseignants e
        JOIN matieres_des_enseignants me ON e.identifiant = me.identifiant_enseignant
        WHERE me.matiere_enseignee = %s
           AND (me.classe_specifique IS NULL OR me.classe_specifique = %s)  -- Vérifiez classe_specifique
    """
    cursor.execute(sql, (matiere, st.session_state['class']))  # Passez la classe actuelle en argument
    result = cursor.fetchone()
    cursor.close()
    db.close()

    if result:
        return {"nom": result[0]}
    else:
        return {"nom": "N/A"}

# Fonction pour vérifier si les notes ont été enregistrées
def notes_enregistrees(class_name, eleves_selectionnes):
    db = get_db_connection()
    cursor = db.cursor()

    for eleve_name in eleves_selectionnes:
        matricule_eleve = get_matricule_by_nom_prenom(eleve_name)
        if matricule_eleve:
            sql = """
                SELECT COUNT(*) 
                FROM notes n
                JOIN notes_sequentielles ns ON n.id = ns.note_id
                WHERE n.matricule_eleve = %s AND ns.sequence = %s
            """
            cursor.execute(sql, (matricule_eleve, st.session_state['sequence']))
            count = cursor.fetchone()[0]
            if count == 0:
                cursor.close()
                db.close()
                return False

    cursor.close()
    db.close()
    return True


# Fonction pour obtenir les notes précédentes d'un élève pour une matière
def get_notes_eleve_precedentes(eleve_name=None, matricule_eleve=None, matiere=None, sequence_precedente=None):
    db = get_db_connection()
    cursor = db.cursor()

    if matricule_eleve is not None:
        # Utiliser le matricule de l'élève (pour le parent)
        sql = """
            SELECT n.note
            FROM notes n
            JOIN eleves e ON n.matricule_eleve = e.matricule_eleve
            JOIN notes_sequentielles ns ON n.id = ns.note_id
            WHERE n.matricule_eleve = %s AND n.matiere = %s AND ns.sequence = %s
        """
        cursor.execute(sql, (matricule_eleve, matiere, sequence_precedente))
    else:
        # Utiliser le nom de l'élève (pour l'admin et l'admin principal)
        sql = """
            SELECT n.note
            FROM notes n
            JOIN eleves e ON n.matricule_eleve = e.matricule_eleve
            JOIN notes_sequentielles ns ON n.id = ns.note_id
            WHERE CONCAT(e.nom, ' ', e.prenom) = %s AND n.matiere = %s AND ns.sequence = %s
        """
        cursor.execute(sql, (eleve_name, matiere, sequence_precedente))

    result = cursor.fetchall()
    cursor.close()
    db.close()
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
    performance_sequentielle_page()