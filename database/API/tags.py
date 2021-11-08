import sqlite3

class AddTag():
    def __init__(self, cursor):
        self.cursor = cursor

    def add_tag(self, tag):
        self.cursor.execute('''
            INSERT INTO tags(
                name
            )
            VALUES(
                ?
            )
            ''', (tag, ))
        return self.cursor.lastrowid