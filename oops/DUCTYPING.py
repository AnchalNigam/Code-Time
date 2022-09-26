class MyAwesomeClass:
    def __init__(self, str):
        self.str = str
    
    # def __len__(self):
    #     return len(self.str)
a = MyAwesomeClass("hey")
print(len(a))  # Prints 3
