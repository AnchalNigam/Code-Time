# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
# def subtract(a, b):
#     return a - b

# def mySubtract(a, b, subtract):
#     def my(a, b):
  
#         if a > b:
#             return subtract(a, b)
#         else:
#             return subtract(b, a)
#     return my
    
# call = mySubtract(subtract)
# print(call(2, 3))

# decorator function to capitalize names
def names_decorator(function):
    def wrapper(arg1, arg2):
        arg1 = arg1.capitalize()
        arg2 = arg2.capitalize()
        string_hello = function(arg1, arg2)
        return string_hello
    return wrapper

@names_decorator
def say_hello(name1, name2):
    return 'Hello ' + name1 + '! Hello ' + name2 + '!'

print(say_hello('sara', 'ansh')) 	 # output => 'Hello Sara! Hello Ansh!'