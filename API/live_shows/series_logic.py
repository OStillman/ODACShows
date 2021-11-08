

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
            if description[potential_series_number] == " ":
                potential_series_number = potential_series_number + 1
            if description[potential_series_number].isnumeric():
                print("Found it!")
                return self.checkMoreThanOneDigit(description, potential_series_number)
                #return description[potential_series_number]
            else:
                if potential_series_number + 1 < len(description):
                    return(self.seriesBranchTwo(potential_series_number))
                else:
                    return False
        else:
            return False


    def checkMoreThanOneDigit(self, description, series_number):
        this_series_number = str(description[series_number])
        series_number = series_number + 1
        is_numeric = True
        while is_numeric:
            this_char = description[series_number]
            if this_char.isnumeric():
                this_series_number = this_series_number + str(this_char)
            else:
                is_numeric = False
            series_number = series_number + 1
        return this_series_number

