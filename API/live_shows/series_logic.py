

class SeriesNumber():
    def __init__(self, show_details):
        self.show_details = show_details

    def getSeriesNumber(self):
        series_number = self.seriesBranchOne()
        if series_number != False:
            return [series_number, "B1"]
        else:
            print("Series Number Not Found...")
            branch_two = self.seriesBranchTwo()
            if branch_two != False:
                return [branch_two, "B2"]
            return [False, False]

    def seriesBranchOne(self):
        try:
            return self.show_details["seriesNo"]
        except:
            return False

    def seriesBranchTwo(self, start_point = 0):
        description = self.show_details["description"]
        find_point = description.find("S", start_point)

        if find_point != -1:
            print("Found AN S")
            potential_series_number = find_point + 1
            print(description[potential_series_number])
            if description[potential_series_number].isnumeric():
                print("Found it!")
                return description[potential_series_number]
            else:
                if potential_series_number + 1 < len(description):
                    return(self.seriesBranchTwo(potential_series_number))
                else:
                    return False
        else:
            return False