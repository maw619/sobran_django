import mysql.connector

def execute_mysql_script(script_path):
    # Open the script file and read the SQL statements
    with open(script_path, 'r') as script_file:
        script = script_file.read()

    # Connect to the MySQL database
    connection = mysql.connector.connect(
        user='<your_mysql_username>',
        password='<your_mysql_password>',
        host='<your_mysql_host>',
        database='<your_mysql_database>'
    )

    # Execute the SQL script
    cursor = connection.cursor()
    cursor.execute(script)

    # Commit the changes and close the connection
    connection.commit()
    connection.close()
