import data


class Districts:
    def __init__(self, dataset):
        """
        builds dataset, from input
        :param dataset: input Data object from data.py
        """
        self.dataset = dataset
        self.all_districts = self.dataset.all_districts_set
        self.districts_set = self.dataset.districts_set

    def filter_districts(self, letters):
        """
        sets data to conclude values only relevant to specific
        :param letters: list of letters, data will be filtered by the first char in list\not
        :return: updated data
        """
        self.dataset.get_all_districts()
        self.dataset.get_relevant_districts(letters)
        self.dataset.set_districts_data(self.dataset.districts_set)

    # print_details function
    def print_details(self, features, statistic_functions):
        """
        Prints Q1, data inside self
        :param features: the name of the relevant list of values that will be calculated
        :param statistic_functions: three statistics functions, from statistics.py
        :return: none
        """
        for i in features:
            leng = len(statistic_functions)
            print(i, ":", sep="", end="")   # end removes irrelevant '\n'
            for j in statistic_functions:
                if leng == 1:
                    print(" ", j(self.dataset.data[i]), sep="")
                else:
                    print(" ", j(self.dataset.data[i]), ",", sep="", end="")
                leng -= 1


    def determine_day_type(self):
        day_type_list = []
        for j, k in enumerate(self.dataset.data['data']):
            if (self.dataset.data['resigned_healed'][j]>self.dataset.data['new_positives'][j]):
                day_type_list.append(1)
            else:
                day_type_list.append(0)
        self.dataset.data['day_type'] = day_type_list


    def get_districts_class(self):
        self.determine_day_type()
        region_list = []
        color_dict = {}
        for k in self.dataset.data['denominazione_region']:
            if k not in region_list:
                region_list.append(k)
        for name in region_list:
            count = 0
            for m in range(len(self.dataset.data['denominazione_region'])):
                if (self.dataset.data['denominazione_region'][m] == name) and (self.dataset.data['day_type'][m] == 1):
                    count = count + 1
            if (count > 340):
                color_dict[name] = "green"
            else:
                color_dict[name] = "not green"
        return color_dict

