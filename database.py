import os
import sqlite3

db_path = 'test.db'


'''
setting_new()
Setting a new database with a set layout
'''
def setting_new():
        #Creating new testdb
        connection = sqlite3.connect('testdb')
        cursor = connection.cursor()

        cursor.execute('''
                CREATE TABLE IF NOT EXISTS images (
                       ID INTEGER PRIMARY KEY,
                       image BLOB
                )
        ''')

        connection.commit()
        connection.close()


def insert_image():
        return

''''''

'''
create_connection()
Check if the database currently exist and return a connection
Otherwise, create a new database
'''
def create_connection():
        if os.path.exists(db_path):
                print("Databasse exist")
                return sqlite3.connect(db_path)
        else:
                print("Database does not exist, creating new one")
                setting_new()




def main():
        print("check")
        connection = sqlite3.connect('test.db')
        cursor = connection.cursor()
        cursor.execute("CREATE TABLE movie(title,year,score)")

       

        connection.commit()

        res = cursor.execute("SELECT score FROM movie")
        print(res.fetchall())


main()