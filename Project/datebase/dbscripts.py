import sqlite3

def script(name_file,dbpath):
    print()
    try:
        sqlite_connection = sqlite3.connect(dbpath)
        cursor = sqlite_connection.cursor()
        print('Соединение с базой данных прошло успешно.')
        try:
            with open (name_file,'r') as file:
                sql_script = file.read()
        except Exception as error:
                    if sqlite_connection:
                        sqlite_connection.close()
                        print('Соединение с SQLite закрыто.')
                    exit(error)
        cursor.executescript(sql_script)
        sqlite_connection.commit()
        print("Скрипт выполнен успешно")
        cursor.close()
    except sqlite3.Error as error:
        print("Не удалось выполнить скрипт.", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

script('Tables.sql','../Xolyavskiy.db')