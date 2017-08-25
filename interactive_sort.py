class InteractiveSortObject:
    """An object that can be sorted interactively.

    This object defines the greater than and less than operations, so it can be used with the normal sort() and sorted()
    functions.
    """
    yes = ["Y", "y", "Yes", "yes"]
    no = ["N", "n", "No", "no"]

    def __init__(self, value):
        """Initialise this object.

        value -- the actual value of this object.
        """
        self.value = value

    # comparison methods
    def __eq__(self, other):
        if not isinstance(other, InteractiveSortObject):
            raise TypeError("Cannot compare.")

        result = input("Are \"{}\" and \"{}\" equal?\n> ".format(self.value, other.value))

        # confirm valid input
        while result not in self.yes + self.no:
            print("Please answer \"y\" or \"n\".")
            result = input("Are \"{}\" and \"{}\" equal?\n> ".format(self.value, other.value))

        return result in self.yes

    def __lt__(self, other):
        if not isinstance(other, InteractiveSortObject):
            raise TypeError("Cannot compare.")

        result = input("Is \"{}\" less than \"{}\"?\n> ".format(self.value, other.value))

        # confirm valid input
        while result not in self.yes + self.no:
            print("Please answer \"y\" or \"n\".")
            result = input("Is \"{}\" less than \"{}\"?\n> ".format(self.value, other.value))

        return result in self.yes

    def __gt__(self, other):
        if not isinstance(other, InteractiveSortObject):
            raise TypeError("Cannot compare.")

        result = input("Is \"{}\" greater than \"{}\"?\n> ".format(self.value, other.value))

        # confirm valid input
        while result not in self.yes + self.no:
            print("Please answer \"y\" or \"n\".")
            result = input("Is \"{}\" greater than \"{}\"?\n> ".format(self.value, other.value))

        return result in self.yes


def interactive_sort(a):
    # turn all into InteractiveSortObjects
    b = list(map(lambda obj: InteractiveSortObject(obj), a))
    b.sort()
    return list(map(lambda obj: obj.value, b))
