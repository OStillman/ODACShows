import sqlite3

class DBAdd():
    def __init__(self):
        self.db = sqlite3.connect('database/db_v1.1.1')
        self.cursor = self.db.cursor()

    def cursor_execute(self, sql_statement):
        self.cursor.execute(sql_statement)

    def retrieve_last_row_id(self):
        return self.cursor.lastrowid

    def close_db(self):
        self.db.commit()
        self.db.close()
