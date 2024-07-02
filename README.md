# Python MySQL Database Interaction

This Python script interacts with a MySQL database (`ppj`) using `mysql.connector`. It provides functionalities to insert, update, select, and delete data from the `users` table. Data retrieval is displayed in a formatted table using `tabulate`.

## Requirements

- Python 3.x
- MySQL server installed and running
- Install required libraries:
  ```bash
  pip install mysql-connector-python tabulate
Functionality
Insert Data:
Allows inserting a new user into the users table with name, age, and place.

Update Data:
Updates existing user data based on the user ID.

Select Data:
Retrieves all user data from the users table and displays it in a formatted table.

Delete Data:
Deletes a user based on the user ID.

Exit:
Ends the program.

Usage
Running the Script:

Ensure your MySQL server is running and accessible.
Open a terminal or command prompt.
Navigate to the directory containing main.py.
Run the script:
bash
Copy code
python main.py
Interaction:

Follow the on-screen menu to perform actions:
Enter 1 to insert new data.
Enter 2 to update existing data.
Enter 3 to view all data.
Enter 4 to delete data based on ID.
Enter 5 to exit the program.
Note:

Customize database connection parameters (host, user, password, database) in the script as per your MySQL setup.
Ensure MySQL user has appropriate permissions (SELECT, INSERT, UPDATE, DELETE) for the users table.
