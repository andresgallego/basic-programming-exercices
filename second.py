"""
Write a function that takes an array of integers as an argument and returns
a value based on the sums of the even and odd numbers in the array.
Let X = the sum of the odd numbers in the array and
let Y = the sum of the even numbers.
The function should return X - Y

Examples

if input array is	return
{1}	1
{1, 2}	-1
{1, 2, 3}	2
{1, 2, 3, 4}	-2
{3, 3, 4, 4}	-2
{3, 2, 3, 4}	0
{4, 1, 2, 3}	-2
{1, 1}	2
{}	0
"""
def function_array(integers):
    x = 0
    y = 0
    for i in range(len(integers)):
        if integers[i] % 2 != 0:
            x += integers[i]
        elif integers[i] % 2 == 0:
            y += integers[i]    
    return x - y

print(function_array([1]))
print(function_array([1,2]))
print(function_array([1,2,3]))
print(function_array([1,2,3,4]))
print(function_array([3,3,4,4]))
print(function_array([3,2,3,4]))
print(function_array([4,1,2,3]))
print(function_array([1,1]))
print(function_array([]))