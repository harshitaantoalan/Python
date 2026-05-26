class Expression:
    
    # Constructor to initialize attributes
    def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3

    # Method to calculate addition
    def add_numbers(self):
        result = self.num1 + self.num2 + self.num3
        print("Addition of three numbers =", result)


# Creating objects
obj1 = Expression(10, 20, 30)
obj2 = Expression(5, 15, 25)

# Calling method using objects
obj1.add_numbers()
obj2.add_numbers()