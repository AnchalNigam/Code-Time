# def pow(x, n, d):
#     c = 1
#     powerRes = 1
#     while(c <= n):
#         powerRes *= x
#         c += 1
#     print(powerRes, 'power')
#     return powerRes%d
# print(pow(71045970,41535484,64735492))

# optimised way 
def myPow(self, x: float, n: int) -> float:
    if n == 0:
        return 1
    if n < 0:
        return self.myPow(1/x, -n)
    else:
        
        if(n%2 == 0):
            return self.myPow(x * x, n//2)
        else:
            return x * self.myPow(x, n-1)
        
print(pow(71045970,41535484,64735492))
# print(pow(4,16,64735492)

# here one pattern is observed and that is implemented. applied recursion here
# detailed explan - https://www.youtube.com/watch?v=l0YC3876qxg