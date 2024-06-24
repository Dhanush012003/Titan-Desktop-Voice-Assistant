# import csv
# import sqlite3

# Import the csv module for reading CSV files.
# con = sqlite3.connect("jarvis.db")
# cursor = con.cursor()

# Uncommented lines to establish a connection to the SQLite database and create a cursor object.
# # query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
# # cursor.execute(query)

# # query = "INSERT INTO sys_command VALUES (null,'notepad', 'D:\\notepad.txt')"
# # cursor.execute(query)
# # con.commit()

# # query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), url VARCHAR(1000))"
# # cursor.execute(query)


# # query = "INSERT INTO web_command VALUES (null,'notepad', 'D:\\notepad.txt')"
# # cursor.execute(query)
# # con.commit()

# query = "UPDATE contacts SET name = REPLACE(name, ' hicet', ''), name = REPLACE(name, ' hicet','') WHERE UPPER(name) LIKE '% hicet';"
# cursor.execute(query)
# # con.commit()

# # testing module
# # app_name = "android studio"
# # cursor.execute('SELECT path FROM sys_command WHERE name IN (?)', (app_name,))
# # results = cursor.fetchall()
# # print(results[0][0])

# #Create a table with the desired columns
# # cursor.execute('''CREATE TABLE IF NOT EXISTS contacts (id integer primary key, name VARCHAR(200), mobile_no VARCHAR(255), email VARCHAR(255) NULL)''')


# # # Specify the column indices you want to import (0-based index)
# # # Example: Importing the 1st and 3rd columns
# # desired_columns_indices = [0, 32]

# # # # Read data from CSV and insert into SQLite table for the desired columns
# # with open('contacts.csv', 'r', encoding='utf-8') as csvfile:
# #     csvreader = csv.reader(csvfile)
# #     for row in csvreader:
# #         selected_data = [row[i] for i in desired_columns_indices]
# #         cursor.execute(''' INSERT INTO contacts (id, 'name', 'mobile_no') VALUES (null, ?, ?);''', tuple(selected_data))

# # Commit changes and close connection
# con.commit()
# con.close()

# # # query = "INSERT INTO contacts VALUES (null,'pawan', '1234567890', 'null')"
# # # cursor.execute(query)
# # # con.commit()

# # # query = 'kunal'
# # # query = query.strip().lower()

# # # cursor.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", ('%' + query + '%', query + '%'))
# # # results = cursor.fetchall()
# # # print(results[0][0])



#UPDATE CONTACT DATABASE
# import csv
# import sqlite3

# con = sqlite3.connect("jarvis.db")
# cursor = con.cursor()

# # Update query to replace 'hicet' without a space
# query = "UPDATE contacts SET name = REPLACE(name, 'Hicet', '') WHERE UPPER(name) LIKE '% HICET';"
# cursor.execute(query)
# con.commit()  # Commit changes after executing the update query

# # Close connection
# con.close()

# # Import sqlite3 module if not already imported
# import sqlite3

# # Connect to the database
# con = sqlite3.connect("jarvis.db")
# cursor = con.cursor()

# # Define the SQL query to delete the row by ID
# query = "DELETE FROM contacts WHERE id = ?"

# # Specify the ID number to be deleted
# id_to_delete = (209,)

# # Execute the query
# cursor.execute(query, id_to_delete)

# # Commit the transaction
# con.commit()

# # Close the connection
# con.close()

# import csv
# import sqlite3

# con = sqlite3.connect("jarvis.db")
# cursor = con.cursor()

# query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
# cursor.execute(query)



#GMAIL ADDING
# import sqlite3

# # Connect to the SQLite database
# conn = sqlite3.connect('jarvis.db')
# cursor = conn.cursor()

# # Create a table to store gmail if it doesn't exist already
# cursor.execute('''CREATE TABLE IF NOT EXISTS gmail (
#                     id INTEGER PRIMARY KEY,
#                     name TEXT,
#                     email TEXT
#                 )''')

# def add_gmail(name, email):
#     try:
#         # Insert the provided name and email address into the contacts table
#         cursor.execute("INSERT INTO gmail (name, email) VALUES (?, ?)", (name, email))
#         conn.commit()
#         print("Contact added successfully!")
#     except sqlite3.Error as e:
#         print("An error occurred while adding the gmail:", str(e))

# # Example usage to add a contact
# add_gmail("kousalya mam", "kousalyadevi.cse@hicet.ac.in")

# # Close the database connection after use
# conn.close()
