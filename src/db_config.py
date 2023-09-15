import sqlite3


class DatabaseConfig:
    def __init__(self, database):
        self.database = database

    def connect_db(self):
        conn = sqlite3.connect(self.database)
        cursor = conn.cursor()
        return cursor

    def retrieve_data(self, cursor, sql_statement):
        cursor.execute(sql_statement)
        data = cursor.fetchall()
        return data