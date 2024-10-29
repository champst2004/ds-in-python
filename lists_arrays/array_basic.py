import array

# type: 'f' (float), initializer list: [1, 2, 3]
new_array = array.array('f', [1, 2, 3])
print(new_array[0])


initializer_list = [2, 5, 43, 5, 10, 52, 29, 5]
number_array = array.array('i', initializer_list)

print(number_array[1:5])  # 2nd to 5th
print(number_array[:-5])  # beginning to 3rd
print(number_array[5:])  # 6th to end
print(number_array[:])   # beginning to end


integers = array.array('i', [1, 2, 3, 5, 7, 10])

# changing first element
integers[0] = 0
print(integers)  # array('i', [0, 2, 3, 5, 7, 10])

# changing 3rd to 5th element
integers[2:5] = array.array('i', [4, 6, 8])
print(integers)     # Output: array('i', [0, 2, 4, 6, 8, 10])


numbers = array.array('i', [1, 2, 3])

numbers.append(4)
print(numbers)  # array('i', [1, 2, 3, 4])

# extend() appends iterable to the end of the array
numbers.extend([5, 6, 7])
print(numbers)     # array('i', [1, 2, 3, 4, 5, 6, 7])


odd = array.array('i', [1, 3, 5])
even = array.array('i', [2, 4, 6])

int = array.array('i')   # creating empty array of integer
int = odd + even

print(int)

del int[2]
print(int)