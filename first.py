"""
1. Write a function that accepts an array of non-negative integers and returns
the second largest integer in the array. Return -1 if there is no second largest.

Examples:

if the input array is	return
{1, 2, 3, 4}	3
{{4, 1, 2, 3}}	3
{1, 1, 2, 2}	1
{1, 1}	-1
{1}	-1
{}	-1
"""

def function_array(integers):
    
    max1 = -1
    max2 = -1
    for i in range(len(integers)):
        #if int(i):
        if integers[i] > max1:
            max2 = max1
            max1 = integers[i]
        elif (integers[i] != max1 and integers[i] > max2):
            max2 = integers[i]                
    return max2

print(function_array([1,2,3,4]))
print(function_array([4,1,2,3])) 
print(function_array([1,1,2,2]))
print(function_array([1,1]))
print(function_array([1]))
print(function_array([]))