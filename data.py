import pandas


# define Data class
class Data:
    def __init__(self, path):
        """
        creates a data object with a given path
        :param path: the given path
        """
        self.path = path
        df = pandas.read_csv(path)
        self.data = df.to_dict(orient="list")
        self.all_districts_set = {}
        self.districts_set = {}  # a set of relevant districts

    def get_all_districts(self):
        """
        creates a set of all districts' names in the csv file
        :return: set of all districts' names
        """
        self.all_districts_set = set(self.data['denominazione_region'])

    def get_relevant_districts(self, letters):
        """
        creates a new set of districts, with the relevant ones only
        :param letters: a list of letters, deciding which district is in the set
        :return: updated set of districts
        """
        districts_set = []
        for i in self.all_districts_set:
            if i[0] in letters:
                districts_set.append(i)
        self.districts_set = set(districts_set)

    def set_districts_data(self, districts):
        """
        update data, will conclude all relevant regions
        :param districts: list of relevant regions
        :return: updated data
        """
        data = {}
        for i in self.data:  # creates the keys
            data.update({i: []})
        for i in range(len(self.data['denominazione_region'])):  # puts the values in the relevant keys
            if self.data['denominazione_region'][i] in districts:
                for j in self.data:
                    data[j].append(self.data[j][i])
        self.data = data
