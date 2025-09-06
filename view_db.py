import sqlite3
from tabulate import tabulate  # pip install tabulate (for pretty table output)
import os

# Point to the correct database inside the instance folder
DB_FILE = os.path.join("instance", "users.db")

def show_tables_and_data():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    # Show all tables
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    print("\n📂 Tables in database:")
    for t in tables:
        print(" -", t[0])

    # For each table, print schema + data
    for t in tables:
        table_name = t[0]
        print(f"\n🔹 Table: {table_name}")

        # Show schema
        cursor.execute(f"PRAGMA table_info({table_name});")
        schema = cursor.fetchall()
        print("Schema:")
        for col in schema:
            print(f"  {col[1]} ({col[2]})")

        # Show data
        cursor.execute(f"SELECT * FROM {table_name} LIMIT 10;")  # show first 10 rows
        rows = cursor.fetchall()
        if rows:
            headers = [col[1] for col in schema]
            print("\nData (first 10 rows):")
            print(tabulate(rows, headers=headers, tablefmt="grid"))
        else:
            print("⚠️ No data found in this table.")

    conn.close()


if __name__ == "__main__":
    show_tables_and_data()
