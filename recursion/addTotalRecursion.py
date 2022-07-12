# total = 0
# def recursive_me(mystring):
#     global total
#     chars = len(mystring)
#     print(chars, 'check', total)
#     if chars == 0:
#         print("Done")
#         # print(total[0])
#     else:      
#       first = int(mystring[0])
#       total = total + first
#       recursive_me(mystring[1:])

# recursive_me("4567")
# print(total)

_my_global = 5

def func1():
  #  _my_global
  if True:
    _my_global = 3


def func2():
    print(_my_global)

# func1()
# print(_my_global) 
# # 5
# func2()



total = 0

def doA():
    # not accessing global total
    total = 10

def doB():
    global total
    total = total + 1

def checkTotal():
    # global total - not required as global is required
    # only for assignment - thanks for comment Greg
    print(total)
    # 1 as dob k mutation k dekhega not doa as doa me it is not mentioned that its 
    # want to mutate global variable total

def main():
    doA()
    doB()
    checkTotal()

# if __name__ == '__main__':
#     main()

def sum_list_items(_list):
    total = 0

    def do_the_sum(_list):

        # Define the total variable as non-local, causing it to bind
        # to the nearest non-global variable also called total.
        nonlocal total

        for i in _list:
            total += i

    do_the_sum(_list)

    return total

# print(sum_list_items([1, 2, 3])  )
def sum_list_items(_list):

    total = 0

    def do_the_sum(_list):

        # The nonlocal total binds to this variable.
        total = 0

        def do_core_computations(_list):

            # Define the total variable as non-local, causing it to bind
            # to the nearest non-global variable also called total.
            nonlocal total

            for i in _list:
                total += i

        do_core_computations(_list)

    do_the_sum(_list)

    return total

# print(sum_list_items([1, 2, 3]))

c = 0
res = 0
def solve(root):
    print(c)

    if c < 8:
      print('hii')
    c += 2
    if c < 8:
      print('hii2')

solve(0)