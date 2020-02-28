def count_happiness(set_a,set_b, array):

    happiness = 0

    if set_a.isdisjoint(set_b):
        for i in range(len(array)):
            if array[i] in set_a:
                happiness += 1

            elif array[i] in set_b:
                happiness -= 1
        print("Happiness Count is:", happiness)

    else:
        print("set A and B is not disjoint, Give input again")
        get_values_for_disjoint_set()


def get_values_for_disjoint_set():
    """
    passing inputs to the count happiness function
    :param array:
    :return:
    """

    array = input("values for array:").split()
    set_a= set(input("Enter Integers(space seperated) for set A:").split())
    set_b = set(input("Enter Integers(space seperated) for set B:").split())

    count_happiness(set_a, set_b, array)


get_values_for_disjoint_set()




