import sqlite3
from pymongo import MongoClient

# Connect to SQLite database
sqlite_conn = sqlite3.connect(r"C:\Users\Timothy\Documents\code\cpe105L_lab5\chinook\chinook.db")  # Fixed path
sqlite_cursor = sqlite_conn.cursor()

# Connect to MongoDB
mongo_client = MongoClient("mongodb://localhost:27017/")
mongo_db = mongo_client["ChinookDB"]

# Get all table names from SQLite
sqlite_cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = [table[0] for table in sqlite_cursor.fetchall()]

for table in tables:
    print(f"Importing {table}...")
    
    # Fetch all rows from the table
    sqlite_cursor.execute(f"SELECT * FROM {table}")
    rows = sqlite_cursor.fetchall()
    
    # Get column names
    column_names = [desc[0] for desc in sqlite_cursor.description]
    
    # Convert rows to dictionaries
    documents = [dict(zip(column_names, row)) for row in rows]
    
    # Insert into MongoDB
    if documents:
        mongo_db[table].insert_many(documents)
        print(f"Inserted {len(documents)} records into {table}")

# Close connections
sqlite_conn.close()
mongo_client.close()