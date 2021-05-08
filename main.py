import sys
import data
import districts
import statistics


def main(argv):
    """
    Main function, for Q1 and Q2
    :param argv: input path
    :return: none
    """
    data_dict = data.Data(argv[1])
    statistic_functions = [statistics.mean, statistics.median]
    print("Question 1:")
    feature_list = ["hospitalized_with_symptoms", "intensive_care", "total_hospitalized", "home_insulation"]
    letters_list = ['L', 'S']
    districts_for_work = districts.Districts(data_dict)
    districts_for_work.filter_districts(letters_list)
    districts_for_work.print_details(feature_list, statistic_functions)


if __name__ == '__main__':
    main(sys.argv)
