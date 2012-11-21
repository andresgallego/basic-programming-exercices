"""
Write a function that accepts a character array, a zero-based start position and a length.
It should return a character array containing length characters starting with
the start character of the input array.
The function should do error checking on the start position and the length
and return null if the either value is not legal.

Examples

if input parameters are	return
{'a', 'b', 'c'}, 0, 4	null
{'a', 'b', 'c'}, 0, 3	{'a', 'b', 'c'}
{'a', 'b', 'c'}, 0, 2	{'a', 'b'}
{'a', 'b', 'c'}, 0, 1	{'a'}
{'a', 'b', 'c'}, 1, 3	null
{'a', 'b', 'c'}, 1, 2	{'b', 'c'}
{'a', 'b', 'c'}, 1, 1	{'b'}
{'a', 'b', 'c'}, 2, 2	null
{'a', 'b', 'c'}, 2, 1	{'c'}
{'a', 'b', 'c'}, 3, 1	null
{'a', 'b', 'c'}, 1, 0	{}
{'a', 'b', 'c'}, -1, 2	null
{'a', 'b', 'c'}, -1, -2	null
{}, 0, 1	null
"""

def char_array(characters, start, length):
    if ((start < 0) or (length < 0) or (start+length-1 >= len(characters))):        
        return    
    sub = [None]*length
    i = start
    for j in range(length):        
        sub[j] = characters[i]
        i += 1    
    return sub
    
print(char_array(['a', 'b', 'c'], 0, 4))
print(char_array(['a', 'b', 'c'], 0, 3))
print(char_array(['a', 'b', 'c'], 0, 2))
print(char_array(['a', 'b', 'c'], 0, 1))
print(char_array(['a', 'b', 'c'], 1, 3))
print(char_array(['a', 'b', 'c'], 1, 2))
print(char_array(['a', 'b', 'c'], 1, 1))
print(char_array(['a', 'b', 'c'], 2, 2))
print(char_array(['a', 'b', 'c'], 2, 1))
print(char_array(['a', 'b', 'c'], 3, 1))
print(char_array(['a', 'b', 'c'], 1, 0))
print(char_array(['a', 'b', 'c'], -1, 2))
print(char_array(['a', 'b', 'c'], -1, -2))
print(char_array([], 0, 1))