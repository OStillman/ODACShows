from database.API import on_demand

class DeleteODShow():
    def __init__(self, show_id):
        self.show_id = show_id
        self.DeleteOD = on_demand.DeleteOD(show_id)
    
    def run_deletion(self):
        sanitise = self.sanitise_input()
        if sanitise[0]:
            self.DeleteOD.DeleteShow()
        return sanitise

    def sanitise_input(self):
        try:
            show_id = int(self.show_id)
            return [True]
        except:
            return [False, "Show ID is not in correct format, ensure an integer is supplied"]
            