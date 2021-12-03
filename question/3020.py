class Checker:

    def __init__(self):
        self.str1 = lambda x: "n={}".format(x)
        self.str2 = "is not a number"

    def check_and_print(self, test_str):
        """
        TODO
        """


checker = Checker()

while True:
    try:
        input_str = input()
    except:
        break
    checker.check_and_print(input_str)
