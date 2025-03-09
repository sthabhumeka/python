import mysql.connector
try:
    connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "python_mysql"
    )
    print("connected to mysql databases succesfully")
except mysql.connector.Error as err:
    print(f"error: {err}")
    exit()
#  id,first_name,last_name,mobile_number
cursor = connection.cursor()


# cursor = connection.cursor()

def create_record():
    try:
        query ="Insert INTO friend (first_name, last_name, mobile)VALUES (%s, %s, %s)"
        values =("Ram","thapa",9855555555)
        cursor.execute(query,values)
        connection.commit()
        print("record insertion insertedsuccessfully")
    except mysql.connector.Error as err:
        print(f"Error: {err}")


create_record()   


# close the connection
cursor.close()
connection.close()
print("mysql conncetion closed.")