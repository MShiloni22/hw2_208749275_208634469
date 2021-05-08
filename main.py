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
    districts_for_q1 = districts.Districts(data_dict)
    districts_for_q1.filter_districts(letters_list)
    districts_for_q1.print_details(feature_list, statistic_functions)
    print()  # before question 2

    print("Question 2:")
    districts_for_q2 = districts.Districts(data_dict)
    print("Number of districts:", len(districts_for_q2.all_districts))
    color_dict = districts_for_q2.get_districts_class()
    not_green_counter = 0
    for key in color_dict:
        if key[0] == 'not green':
            not_green_counter += 1
    print("Number of not green districts:", not_green_counter)
    if not_green_counter > 10:
        print("Will a lockdown be forced on whole of Italy?: Yes")
    else:
        print("Will a lockdown be forced on whole of Italy?: No")


if __name__ == '__main__':
    main(sys.argv)
