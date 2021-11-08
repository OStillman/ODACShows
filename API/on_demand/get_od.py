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
            response["od_shows"].append(this_response)
        return response

class RetrieveSpecificShow():
    def __init__(self, show_id):
        self.show_id = show_id

    def fetch_show(self):
        GetSpecificOD = on_demand.GetSpecificOD(self.show_id)
        retrieved_show = GetSpecificOD.RetrieveShow()
        print(retrieved_show)
        retrieved_show = self.objectify_response(retrieved_show)
        return retrieved_show

    def objectify_response(self, retrieved_show):
        response = {"od_show": []}
        for show in retrieved_show:
            this_response = {
                "id": show[0],
                "name": show[1],
                "service": show[2],
                "watching": show[3],
                "series": show[4],
                "episode": show[5]
            }
            response["od_show"].append(this_response)
        return response