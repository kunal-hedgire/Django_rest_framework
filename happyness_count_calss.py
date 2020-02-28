class HappynessCount:

    def __init__(self):
        # initialize the values
        self.input_array = None
        self.set1 = None
        self.set2 = None
        self.len_arr = None
        self.len_set = None
        self.get_input_and_validation()
        self.count_happiness()

    def validate_length(self, set_obj, expected_length):
        # validating the len of set and array
        if len(set_obj) != expected_length:
            print(f"Enter {self.len_arr} number of elements in array")
            self.get_input_and_validation()

    def get_input_and_validation(self):
        """
        taking inputs and call validate function for len validation.
        :param array:
        :return:
        """
        self.len_arr = int(input("value for len_arr:"))
        self.len_set = int(input("values for len_set:"))
        self.input_array = input("Enter Integers(space seperated) for array :").split()
        self.validate_length(self.input_array, self.len_arr)
        self.set1 = set(input("Enter Integers(space seperated) for "
                              "set1:").split())
        self.validate_length(self.set1, self.len_set)
        self.set2 = set(input("Enter Integers(space seperated) for "
                              "set2:").split())
        self.validate_length(self.set2, self.len_set)

    def count_happiness(self):
        """
        Count the happiness and print the happiness count.
        :return:
        """

        happiness = 0

        # check set1 and set2 are disjoint
        if self.set1.isdisjoint(self.set2):
            for i in range(len(self.input_array)):

                # check array element in set1
                if self.input_array[i] in self.set1:
                    happiness += 1

                # check array element in set2
                elif self.input_array[i] in self.set2:
                    happiness -= 1

            # print the happiness count
            print("Happiness Count is:", happiness)
        else:

            # if set1 and set2 are not disjoint and take inputs again
            print("set A and B is not disjoint, Give input again")
            self.get_input_and_validation()


if __name__ == '__main__':
    happyness_obj = HappynessCount()






students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
students.sort(key=lambda x:(x[1],x[0]))
name = [i[0] for i in students]
per = [i[1] for i in students]


min_val = min(per)

if per[0] == min_val:
    per.remove(per[0])
    name.remove(name[0])

for x in range(0,len(per)):
    if per[x] == min(per):
        print(name[x])



