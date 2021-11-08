import sqlite3
from database.API import db_actions
import json

class AllChannels():
    def __init__(self):
        self.DBActions = db_actions.DBOtherActions()

    def GetAllChannels(self, live_only=False):
        if live_only:
            self.DBActions.cursor.execute('''
                SELECT * from channels
                WHERE type = "Live";
            ''')
        else:
            self.DBActions.cursor.execute('''
                SELECT * from channels;
            ''')
        return self.objectify_channel_output(self.DBActions.cursor.fetchall())
    
    def objectify_channel_output(self, output):
        print(output)
        object_output = []
        for object in output:
            object_output.append({
                "id": str(object[0]),
                "name": object[1],
                "type": object[2],
                "number": str(object[3])
            })
        return object_output


class SearchChannels():
    def __init__(self, channel):
        self.channel = channel
        self.DBActions = db_actions.DBOtherActions()

    def searchChannel(self):
        print(self.channel)
        self.DBActions.cursor.execute('''
            SELECT * FROM channels
            WHERE id = ?;
            ''', (self.channel, ))
        try:
            # If tag exists, will be able to fetch the output
            return self.objectify_channel_output(self.DBActions.cursor.fetchall()[0])
        except IndexError:
            return False

    def objectify_channel_output(self, output):
        #json_string = ('{ "id": '+ str(output[0]) +' , "name": ' + str(output[1]) + ', "type": ' + str(output[2]) + ', "number": ' + str(output[3]) + '}')
        #return json.loads(json_string)
        #return json.loads('{ "id": {}, "name": {}, "type": {}, "number": {}}').format(output[0], output[1], output[2], output[3])
        return ({
            "id": str(output[0]),
            "name": output[1],
            "type": output[2],
            "number": str(output[3])
        })