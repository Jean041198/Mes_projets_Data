import sqlite3

# Fonction de migration vers SQLite (modifiée)
def migrate_sql_to_sqlite(sql_file, sqlite_db):
    conn = sqlite3.connect(sqlite_db)
    cursor = conn.cursor()

    try:
        with open(sql_file, 'r', encoding='utf-8') as f:
            sql_script = f.read()
        cursor.executescript(sql_script)
        conn.commit()
        print("Migration terminée avec succès !")
    except sqlite3.Error as e:
        print(f"Erreur lors de la migration : {e}")
        # Affichage de l'erreur SQL pour le débogage
        print(f"Erreur SQL : {e.args[0]}") # Afficher la partie SQL de l'erreur
    finally:
        cursor.close()
        conn.close()

# Chemin vers le fichier .sql ORGANISE
sql_file = "utils/collegefoganggenies_db_cleaned.sql"  
# Chemin de la base de données SQLite
sqlite_db = "utils/collegefoganggenies_db.sqlite"

# Migration du fichier ORGANISE vers SQLite
migrate_sql_to_sqlite(sql_file, sqlite_db)