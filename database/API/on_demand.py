import sqlite3
from database.API import db_actions
from database.API import tags

class AddODShow():
    def __init__(self, show_info):
        #Show info = JSON input from user
        self.show_info = show_info
        self.DBAdd = db_actions.DBAdd()

    def ExecuteAdd(self):
        # To Add, we need to execute the statement, check and add the tags, then close the DB
        sql_statement = self.execute_statement()
        self.tag_control()
        self.DBAdd.close_db()

    def execute_statement(self):
        # Execute Add Statement
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
        # Deal with tag(s)
        # First, get the last row we've just added - for the link table reference
        show_id = self.DBAdd.retrieve_last_row_id()
        for tag in self.show_info['tags']:
            # Check tag exists, and if not create
            tag_id = self.checkTagExists(tag)
            # Using this, we can then add our tag - show link
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
            # If tag exists, will be able to fetch the output
            return select_cursor.fetchall()[0][0]
        except IndexError:
            # Or will error, and so the tag doesn't exist, so we need to create it
            AddTag = tags.AddTag(self.DBAdd.cursor)
            # Will return the tag's row_id
            return AddTag.add_tag(tag)

class GetAllOD():
    def __init__(self):
        self.DBActions = db_actions.DBOtherActions()
        self.cursor = self.DBActions.cursor

    def RetrieveAllShows(self):
        all_shows = self.cursor.execute('''
        SELECT * FROM ODShows;
        ''').fetchall()
        print(all_shows)
        return all_shows
