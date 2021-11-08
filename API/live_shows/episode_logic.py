

class EpisodeNumber():
    def __init__(self, show_details):
        self.show_details = show_details

    def getEpisodeNumber(self):
        episode_number = self.episodeBranchOne()
        if episode_number != False:
            return [episode_number, "B1"]
        else:
            branch_two = self.episodeBranchTwo()
            if branch_two != False:
                return [branch_two, "B2"]
            print("Episode Number Not Found...")
            return [False, False]

    def episodeBranchOne(self):
        try:
            return self.show_details["episodeNo"]
        except:
            return False

    def episodeBranchTwo(self, start_point = 0):
        description = self.show_details["description"]
        find_point = description.find("Ep", start_point)
        print(find_point)

        if find_point != -1:
            print("Found AN Ep")
            potential_ep_number = find_point + 2
            print(description[potential_ep_number])
            if description[potential_ep_number].isnumeric():
                print("Found it!")
                return description[potential_ep_number]
            else:
                print(potential_ep_number+2)
                if potential_ep_number + 2 < len(description):
                    return(self.episodeBranchTwo(start_point=potential_ep_number))
                else:
                    return False
        else:
            return False