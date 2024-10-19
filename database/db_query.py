import sqlite3


def get_db_connection():
    try:
        connection = sqlite3.connect("buddy.db", timeout=10)
        return connection
    except Exception as e:
        print("Error in creating table", e)
        return None
    

#get all records from the table
def get_all_record(query): 
    db_connection = get_db_connection()
    cur = db_connection.cursor()
    
    #Get All Rows From the Table
    cur.execute(query)
    rows = cur.fetchall()
    cur.close()
    
    return rows

#get single record from the table
def single_record(query):
    db_connection = get_db_connection()
    cur = db_connection.cursor()
    
    #Get All Rows From the Table
    cur.execute(query)
    row = cur.fetchone()
    cur.close()
    
    return row