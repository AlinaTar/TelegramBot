import sqlite3

def SelectTable(dbpath):
    try:
        sqlite_connection = sqlite3.connect(dbpath)
        cursor = sqlite_connection.cursor()
        print('Соединение с базой данных прошло успешно.')

        sqlite_selection_query = "SELECT * FROM changes;"
        cursor.execute(sqlite_selection_query)
        record = cursor.fetchall()
        cursor.close()
        return record
    except sqlite3.Error as error:
        print("Не удалось выбрать данные из таблицы.", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

def selectFromnames(name,dbpath):
    try:
        sqlite_connection = sqlite3.connect(dbpath)
        cursor = sqlite_connection.cursor()
        print('Соединение с базой данных прошло успешно.')

        sqlite_selection_query = "SELECT * FROM changes WHERE name=?;"
        cursor.execute(sqlite_selection_query,(name,))
        record = cursor.fetchall()
        cursor.close()
        return record
    except sqlite3.Error as error:
        print("Не удалось выбрать данные по именам студентов.", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

def selectFromSurnamesAndNames(name_surname,dbpath):
    try:
        sqlite_connection = sqlite3.connect(dbpath)
        cursor = sqlite_connection.cursor()
        print('Соединение с базой данных прошло успешно.')

        sqlite_selection_query = "SELECT * FROM changes WHERE name_surname=?;"
        cursor.execute(sqlite_selection_query,(name_surname,))
        record = cursor.fetchall()
        cursor.close()
        return record
    except sqlite3.Error as error:
        print("Не удалось выбрать данные по именам студентов.", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


def addNewchanges(record: list,dbpath):
    print()
    try:
        sqlite_connection = sqlite3.connect(dbpath)
        cursor = sqlite_connection.cursor()
        print('Соединение с базой данных прошло успешно.')

        insert_query = '''INSERT INTO changes (name,name_surname,data)
                          VALUES (?,?,?);'''
        cursor.executemany(insert_query,(record,))
        print('Запись добавленна')
        sqlite_connection.commit()
        cursor.close()
    except sqlite3.Error as error:
        print("Не удалось записать информацию", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")
    print()


def deleteRecord(dbpath):
    try:
        sqlite_connection = sqlite3.connect(dbpath)
        cursor = sqlite_connection.cursor()
        print('Соединение с базой данных прошло успешно.')

        sqlite_delete_query = "DELETE FROM changes WHERE id=3;"
        cursor.execute(sqlite_delete_query)
        sqlite_connection.commit()
        print('Запись', 'успешно удалена')
    except sqlite3.Error as error:
        print("Не удалось удалить данные.", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

print(SelectTable('../Xolyavskiy.db'))