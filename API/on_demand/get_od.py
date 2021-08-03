from database.API import on_demand

class RetrieveAllShows():
    def __init__(self):
        self.GetAllOD = on_demand.GetAllOD()

    def run_retrieval(self):
        all_shows = self.GetAllOD.RetrieveAllShows()
        all_shows = self.objectify_response(all_shows)
        return all_shows

    def objectify_response(self, all_shows):
        response = {"od_shows": []}
        for show in all_shows:
            this_response = {
                "id": show[0],
                "name": show[1],
                "service": show[2],
                "watching": show[3],
                "series": show[4],
                "episode": show[5]
            }
            print(this_response)
            response["od_shows"].append(this_response)
        
        print(response)
        return response