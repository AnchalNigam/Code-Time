# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
def subtract(a, b):
    return a - b

def mySubtract(a, b, subtract):
    def my(a, b):
  
        if a > b:
            return subtract(a, b)
        else:
            return subtract(b, a)
    return my
    
call = mySubtract(subtract)
print(call(2, 3))
