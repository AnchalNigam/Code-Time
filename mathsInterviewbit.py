from itertools import dropwhile, product, takewhile
if B > len(str(C)) or len(A) == 0:
    print(0)
c_tuple = tuple(map(int, str(C)))
combinations = product(A,repeat=B)
if B != 1:
    combinations = dropwhile(lambda x: x[0] == 0, combinations)
if B == len(c_tuple):
    combinations = takewhile(lambda x: x < c_tuple, combinations)
print(sum(1 for _ in combinations))   