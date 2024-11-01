def find_second_maximum(nums): # O(n)
    max = float('-inf')
    max2 = float('-inf')

    for i in nums:
        if i > max:
            max = i

    for i in nums:
        if i > max2 and i != max:
            max2 = i
    return max2


list = [-2,-3,-5,-7]
print(find_second_maximum(list))