import streamlit as st
from datetime import time, datetime
import mysql.connector
import re

def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def get_db_connection():
    mydb = mysql.connector.connect(
        host="localhost",
        user="gelito01",
        password="admin@01",
        database="collegefoganggenies_db"
    )
    return mydb

def is_valid_time(time_str):
    """Check if the input time string is valid in HH:MM format."""
    regex = r"^(0[0-9]|1[0-9]|2[0-3]|[0-9]):([0-5][0-9])$"
    return re.match(regex, time_str) is not None

def presence_journaliere_page():
    load_css("static/styles/styles.css")

    col1, col2, col3 = st.columns([1.5, 2, 0.5])
    with col2:
        st.image("static/images/logo.png", width=150)

    # Vérifiez le mode de visualisation et le rôle
    if not st.session_state.get('visualisation_mode', False):
        # Si le parent est connecté, il est en mode visualisation
        if st.session_state.get('role') == 'parent':
            st.title("Performance Journalière")

            matricule_eleve = st.session_state.get('matricule_eleve')
            eleve_selectionne = get_eleve_by_matricule(matricule_eleve)

            if eleve_selectionne:
                presence = get_presence_eleve(matricule_eleve)
                if presence:
                    st.subheader(f"Présence de l'élève : {eleve_selectionne}")
                    st.write(f"Date : {presence['date']}")
                    st.write(f"Heure d'entrée : {presence['heure_entree']}")
                    st.write(f"Heure de sortie : {presence['heure_sortie']}")
                    st.write(f"Heures d'absence : {presence['heures_absence']}")
                    st.write(f"Décision : {presence['decision']}")
                    st.write(f"minutes_retard : {presence['minutes_retard']}")
                else:
                    st.warning(f"Aucune présence enregistrée pour {eleve_selectionne}")

            if st.button("Retour", key="retour_visualisation"):  
                st.session_state['page'] = "Page d'évolution"  
                st.rerun()

        else:
            # Mode Saisie des Présences pour l'administrateur 
            st.title("Présence Journalière")

            jour = st.date_input("Jour", datetime.now())

            # Vérifiez si l'administrateur principal est connecté
            if st.session_state.get('role') == 'admin_principal':
                eleves = get_eleves_from_class(st.session_state['class'])
                eleve_selectionne = st.selectbox("Élève", eleves, key="select_eleve_principal", index=None)

                # Affichez les éléments si un élève est sélectionné
                if eleve_selectionne:
                    st.session_state['visualisation_mode'] = True  # Activer le mode visualisation
                    st.rerun() 
            else:
                # Mode de saisie pour l'administrateur
                eleves = get_eleves_from_class(st.session_state['class'])
                eleves_selectionnes = st.selectbox("Élève", eleves, key="select_eleve", index=None)
                
                # Input pour l'heure d'entrée
                heure_entree_str = st.text_input("Heure d'entrée (HH:MM)", placeholder="HH:MM")
                
                if heure_entree_str and is_valid_time(heure_entree_str):
                    heure_entree = datetime.strptime(heure_entree_str, "%H:%M").time()
                else:
                    st.error("Veuillez entrer une heure d'entrée valide au format HH:MM.")
                    heure_entree = None  # Si l'entrée n'est pas valide

                # Calcul du retard et des heures d'absence
                heures_absence = 0  # Initialiser à zéro par défaut
                retard = "Pas de retard"  # Valeur par défaut si l'heure n'est pas valide
                total_minutes_retard = 0  # Nombre total de minutes de retard après 7:30
                minutes_retard = 0
                if heure_entree is not None:
                    # Vérifiez si l'heure d'entrée est valide pour le retard
                    if heure_entree > time(7, 30):
                      # Calculer les minutes de retard après 7h30
                      delta_retard = datetime.combine(jour, heure_entree) - datetime.combine(jour, time(7, 30))
                      total_minutes_retard = delta_retard.seconds // 60  # Total des minutes de retard
                      minutes_retard = total_minutes_retard % 60
                      # Mise à jour des heures d'absence
                      if heure_entree > time(8, 30):
                         # Calcul des heures d'absence après 8h30
                         delta_absence = datetime.combine(jour, heure_entree) - datetime.combine(jour, time(8, 30))
                         heures_absence = delta_absence.seconds // 3600  # Ne pas ajouter 1 ici
                         total_minutes_retard += (delta_absence.seconds % 3600) // 60  # Ajouter les minutes de retard après 8h30
                      else:
                        # Calcul des heures d'absence 
                        delta_absence = datetime.combine(jour, heure_entree) - datetime.combine(jour, time(7, 30)) 
                        heures_absence = delta_absence.seconds // 3600 # Calcul des heures d'absence 
                        if delta_absence.seconds % 3600 > 0:
                         heures_absence += 1 # Ajouter 1 heure si il y a des minutes d'absence 
                            
                    # Convertir les minutes totales en heures et minutes
                    heures_retard = total_minutes_retard // 60
                    minutes_retard = total_minutes_retard % 60
                    # Affichage du retard
                    retard = f"Retard de {heures_retard} heure(s) et {minutes_retard} minute(s)"
                else:
                    retard = "Pas de retard"
                # Input pour l'heure de sortie
                heure_sortie_str = st.text_input("Heure de sortie (HH:MM)", placeholder="HH:MM")
                if heure_sortie_str and is_valid_time(heure_sortie_str):
                    heure_sortie = datetime.strptime(heure_sortie_str, "%H:%M").time()
                else:
                    heure_sortie = None  # Si l'entrée n'est pas valide

                # Déterminer la décision (en tenant compte du retard et des minutes de retard)
                if heures_absence > 0 or total_minutes_retard > 0:
                    # S'il y a des heures d'absence OU des minutes de retard, il y a une absence
                    decision = "Blâme" if heures_absence <= 8 else \
                               "Corvée" if heures_absence <= 16 else \
                               "Conseil de discipline avec parents"
                    decision += f" et {retard}"
                else:
                    # Pas d'absence
                    decision = "Pas d'absence"

                # Affiche la décision finale
                st.text_input("Décision", value=decision, disabled=True)
                # Affiche le retard (en rouge si retard)
                st.markdown(f"<h4 style='color: { 'red' if retard != 'Pas de retard' else 'black' };'>Retard : {retard}</h4>", unsafe_allow_html=True)

                if total_minutes_retard > 0: 
                    heures_absence_str = f"{heures_retard} heure(s)" if heures_retard > 1 else f"{heures_retard} heure"
                    heures_absence_str += f" et {minutes_retard} minute(s)" if minutes_retard > 0 else ""
                    st.text_input("Nombre total d'heures d'absence", value=heures_absence_str, disabled=True)
                else:
                    st.text_input("Nombre total d'heures d'absence", value="Pas d'absence", disabled=True)
                
                # Bouton Enregistrer
                if st.button("Enregistrer"):
                    if heure_entree and heure_sortie:
                        # Enregistrer la présence avec le nombre de minutes de retard
                        enregistrer_presence(eleves_selectionnes, jour, heure_entree, heure_sortie, heures_absence, decision, minutes_retard)
                        st.success("Présence enregistrée avec succès !")
                    else:
                        st.error("Veuillez saisir une heure d'entrée et de sortie valides.")

                # Affiche les boutons Retour et Visualisation sur la même ligne
                col1, col2 = st.columns([1, 1])
                with col1:
                    if st.button("Retour", key="retour_saisie"):  
                        st.session_state['page'] = "Page des Classes"  
                        st.rerun()
                with col2:
                    if st.button("Visualisation des performances", key="visualisation"):
                        st.session_state['visualisation_mode'] = True
                        st.rerun() 
    else:
        visualisation_presence_journaliere()


def visualisation_presence_journaliere():
    st.title("Performance Journalière")
    
    # Vérifiez le rôle de l'utilisateur
    role = st.session_state.get('role')
    
    if role == 'parent':
        # Affichage pour les parents
        matricule_eleve = st.session_state.get('matricule_eleve')
        eleve_selectionne = get_eleve_by_matricule(matricule_eleve)

        if eleve_selectionne:
            presence = get_presence_eleve(matricule_eleve)
            if presence:
                st.subheader(f"Présence de l'élève : {eleve_selectionne}")
                st.write(f"Date : {presence['date']}")
                st.write(f"Heure d'entrée : {presence['heure_entree']}")
                st.write(f"Heure de sortie : {presence['heure_sortie']}")
                st.write(f"Heures d'absence : {presence['heures_absence']}")
                st.write(f"Décision : {presence['decision']}")
                st.write(f"minutes_retard : {presence['minutes_retard']}")
            else:
                st.warning(f"Aucune présence enregistrée pour {eleve_selectionne}")

        if st.button("Retour", key="retour_visualisation"):
            st.session_state['page'] = "Page d'évolution"  
            st.rerun()

    else:
        # Affichage pour les administrateurs et l'administrateur principal
        eleves = get_eleves_from_class(st.session_state['class'])
        eleve_selectionne = st.selectbox("Élève", eleves, key="select_eleve_visualisation", index=None)  # Key différente pour la visualisation

        if eleve_selectionne:
            # Récupérez le matricule de l'élève sélectionné
            matricule_eleve = get_matricule_by_nom_prenom(eleve_selectionne)
            if matricule_eleve:
                presence = get_presence_eleve(matricule_eleve)
                if presence:
                    st.subheader(f"Présence de l'élève : {eleve_selectionne}")
                    st.write(f"Date : {presence['date']}")
                    st.write(f"Heure d'entrée : {presence['heure_entree']}")
                    st.write(f"Heure de sortie : {presence['heure_sortie']}")
                    st.write(f"Heures d'absence : {presence['heures_absence']}")
                    st.write(f"Décision : {presence['decision']}")
                    st.write(f"minutes_retard : {presence['minutes_retard']}")
                else:
                    st.warning(f"Aucune présence enregistrée pour {eleve_selectionne}")
                

        if st.button("Retour", key="retour_visualisation"):  
            role = st.session_state.get('role', 'admin') 
            st.session_state['visualisation_mode'] = False 
            if role == 'admin_principal':
                st.session_state['page'] = "Page des Classes" 
                st.rerun()
            else:
                st.session_state['page'] = "Présence Journalière"  
                st.rerun()

def enregistrer_presence(eleve_selectionne, jour, heure_entree, heure_sortie, heures_absence, decision, minutes_retard):
    db = get_db_connection()
    cursor = db.cursor()

    matricule_eleve = get_matricule_by_nom_prenom(eleve_selectionne)
    if matricule_eleve:
        # Ajout de la colonne 'minutes_retard' dans l'INSERT SQL
        sql = """
            INSERT INTO presences (matricule_eleve, date, heure_entree, heure_sortie, heures_absence, decision, minutes_retard)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(sql, (matricule_eleve, jour, heure_entree, heure_sortie, heures_absence, decision, minutes_retard))
        db.commit()

    cursor.close()
    db.close()

def get_matricule_by_nom_prenom(eleve_name):
    db = get_db_connection()
    cursor = db.cursor()
    sql = "SELECT matricule_eleve FROM eleves WHERE CONCAT(nom, ' ', prenom) = %s"
    cursor.execute(sql, (eleve_name,))
    result = cursor.fetchone()
    cursor.close()
    db.close()

    return result[0] if result else None

def get_eleves_from_class(class_name):
    db = get_db_connection()
    cursor = db.cursor()
    sql = "SELECT matricule_eleve, nom, prenom FROM eleves WHERE classe = %s"
    cursor.execute(sql, (class_name,))
    eleves = cursor.fetchall()
    cursor.close()
    db.close()

    return [f"{row[1]} {row[2]}" for row in eleves]

def get_presence_eleve(matricule_eleve):
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)  # Use dictionary=True to return a dictionary
    sql = """
        SELECT date, heure_entree, heure_sortie, heures_absence, decision, minutes_retard 
        FROM presences 
        WHERE matricule_eleve = %s
        ORDER BY date DESC LIMIT 1
    """
    cursor.execute(sql, (matricule_eleve,))
    presence = cursor.fetchone()
    cursor.close()
    db.close()

    return presence  # Return the fetched record (or None if no record is found)




def get_eleve_by_matricule(matricule_eleve):
    db = get_db_connection()
    cursor = db.cursor()
    sql = "SELECT nom, prenom FROM eleves WHERE matricule_eleve = %s"
    cursor.execute(sql, (matricule_eleve,))
    result = cursor.fetchone()
    cursor.close()
    db.close()

    if result:
        return f"{result[0]} {result[1]}"
    return None


def main():
    presence_journaliere_page()

if __name__ == "__main__":
    main()