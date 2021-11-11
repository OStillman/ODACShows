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


class AddChannels():
    def __init__(self, live = False):
        self.live = live
        self.db_actions = db_actions.DBAdd()

    def insertChannel(self, channel_data):
        channel_data = self.checkChannel(channel_data)
        this_data = channel_data[1]
        if channel_data[0] == True:
            self.db_actions.cursor.execute('''
            INSERT INTO channels (
                name,
                type,
                number
            )
            values (
                ?,
                ?,
                ?
            );
            ''', (this_data["channelName"], "Live", this_data["channelId"]))

    def checkChannel(self, channel_data):
        this_channel_name = channel_data["channelName"].lower()
        if "freesat" in this_channel_name:
            return [False, channel_data]
        elif "radio" in this_channel_name:
            return [False, channel_data]
        elif "fm" in this_channel_name:
            return [False, channel_data]
        elif "rte" in this_channel_name:
            return [False, channel_data]
        elif "qvc" in this_channel_name:
            return [False, channel_data]
        elif "great!" in this_channel_name:
            return [False, channel_data]
        elif "s4c" in this_channel_name:
            return [False, channel_data]
        elif "jazeera" in this_channel_name:
            return [False, channel_data]
        elif "capital" in this_channel_name:
            return [False, channel_data]
        elif "heart" in this_channel_name:
            return [False, channel_data]
        elif "radio" in channel_data["description"].lower():
            return [False, channel_data]
        elif "wales" in this_channel_name:
            return [False, channel_data]
        elif "rb" in this_channel_name:
            return [False, channel_data]
        elif "bbc one london" in this_channel_name:
            print("London found")
            channel_data["channelName"] = "BBC ONE"
        return [True, channel_data]

    def commitAndClose(self):
        self.db_actions.close_db()

class UpdateChannel():
    def __init__(self):
        self.db_actions = db_actions.DBOtherActions()


    def run_Update(self, channel_id, channel_new_number):
        self.db_actions.cursor.execute('''
        UPDATE channels 
        SET number = ?
        WHERE id = ?;
        ''', (channel_new_number, channel_id))

    def commitAndClose(self):
        self.db_actions.close_db()
