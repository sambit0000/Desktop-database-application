# Importing the required libraries
import sqlite3

# Function to create a table in database
def connect():
    conn = sqlite3.connect("books1.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn INTEGER)")
    conn.commit()
    conn.close()

# Function to insert rows in the table
def insert(title, author, year, isbn):
    conn = sqlite3.connect("books1.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",(title,author,year,isbn))
    conn.commit()
    conn.close()    

# Function to view all the rows in the table
def view():
    conn = sqlite3.connect("books1.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    conn.close()
    return rows

# Function to view a specific row in the table
def search(title="",author="",year="",isbn=""):
    conn = sqlite3.connect("books1.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?",(title,author,year,isbn))
    rows = cur.fetchall()
    conn.close()
    return rows

# Function to delete rows in the table
def delete(id):
    conn = sqlite3.connect("books1.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?",(id,))
    conn.commit()
    conn.close() 

# Function to update row values in table
def update(id,title,author,year,isbn):
    conn = sqlite3.connect("books1.db")
    cur = conn.cursor()
    cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?",(title,author,year,isbn,id))
    conn.commit()
    conn.close() 

connect()
#insert("Ramayana","Maharshi Valmiki",1200000,67483823829389)
#delete(1)
#update(2,"Mahabharata","Veda Vyasa",6000,45556566)
#print(view())
#print(search(title="",author="",year="",isbn=""))
