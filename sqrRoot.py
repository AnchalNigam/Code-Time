if A == 0 or A == 1:
    print(A)
else:
    
    for i in range(1,int(A/2)+1):
        if (i**2) == A or ((i**2) < A and ((i+1)**2) > A):
            print(i)
    
    
                
                