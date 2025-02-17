import sqlite3

# Function to create the database and tables
def create_db():
    conn = sqlite3.connect('petshop.db')
    cursor = conn.cursor()

    # Create the admins table (adminID, username, password)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS admins (
            admin_id TEXT PRIMARY KEY,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')

    # Create the customers table (username, password, name, email)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS customers (
            username TEXT PRIMARY KEY,
            password TEXT NOT NULL,
            name TEXT NOT NULL,
            email TEXT NOT NULL
        )
    ''')

    # Insert predefined admin (you can add more admins as needed)
    cursor.execute('''
        INSERT OR REPLACE INTO admins (admin_id, username, password)
        VALUES ("admin123", "admin", "adminpass")
    ''')

    conn.commit()
    conn.close()

# Call the function to create the database
create_db()
