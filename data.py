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
        self.districts_set = {}

    def get_all_districts(self):
        """
        creates a set of all districts' names in the csv file
        :return: set of all districts' names
        """
        self.districts_set = set(self.data['denominazione_region'])
