from os import *
from sys import *
from collections import *
from math import *

def getInversions(arr, n):
	# Write your code here.
    count = 0
    def mergeArr(L, R, arr):
        nonlocal count
        i = j = k = 0
        n1 = len(R)
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]               
                i += 1
            else:
                count += len(L)-i
                arr[k] = R[j]
                j += 1
            k += 1
        # if i < len(L):
        #     count += len(R)*(len(L)-i)
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
      
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    def mergeSort(arr):
        if len(arr) > 1:
            mid = len(arr)//2
            L = arr[:mid]
            R =  arr[mid:]
            mergeSort(L)
            mergeSort(R)
            mergeArr(L, R, arr)
    mergeSort(arr)   
    # print(count)
    return count
# Taking inpit using fast I/O.
def takeInput():
    n = int(input())
    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n

# Main.
arr, n = takeInput()
print(getInversions(arr, n))