import mysql.connector
from mysql.connector import Error


def connect():
    """ Connect to DB """

    try:
        conn = mysql.connector.connect(host="localhost",
                                       database="EMSI_TEST_DB",
                                       user='root',
                                       password='')
        if conn.is_connected():
            print('Connected to Database')

        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Material")

        row = cursor.fetchone()
        while row is not None:
            print(row)
            row = cursor.fetchone()

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    connect()