import sqlite3
from database.API import db_actions
from database.API import tags

class AddODShow():
    def __init__(self, show_info):
        self.show_info = show_info
        self.DBAdd = db_actions.DBAdd()

    def ExecuteAdd(self):
        sql_statement = self.execute_statement()
        self.tag_control()
        self.DBAdd.close_db()

    def execute_statement(self):
        self.DBAdd.cursor.execute('''
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

    def tag_control(self):
        show_id = self.DBAdd.retrieve_last_row_id()
        for tag in self.show_info['tags']:
            tag_id = self.checkTagExists(tag)
            self.DBAdd.cursor.execute('''
            INSERT INTO ShowTags(
                show_id,
                tag_id
            )
            VALUES(
                ?,
                ?
            )
            ''', (show_id, tag_id, ))
            

    def checkTagExists(self, tag):
        print(tag)
        select_cursor =  self.DBAdd.cursor
        select_cursor.execute('''
            SELECT * FROM tags
            WHERE name = ?;
            ''', (tag, ))
        try:
            return select_cursor.fetchall()[0][0]
        except IndexError:
            AddTag = tags.AddTag(self.DBAdd.cursor)
            return AddTag.add_tag(tag)