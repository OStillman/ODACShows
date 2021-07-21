import sqlite3

class AddODShow():
    def __init__(self, show_info):
        self.show_info = show_info
        self.db = sqlite3.connect('database/db_v1.1.1')
        self.cursor = self.db.cursor()

    def ExecuteAdd(self):
        self.cursor.execute('''
        INSERT INTO ODShows (
            name,
            service,
            watching,
            episode,
            series
        )
        values (
            ?,
            ?,
            ?,
            ?,
            ?
        );
        ''', (self.show_info["name"], self.show_info["service"], self.show_info["watching"], self.show_info["episode"], self.show_info["series"]))
        self.db.commit()
        self.db.close()