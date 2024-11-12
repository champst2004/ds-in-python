def right_rotate(nums, k): 
    if len(nums) == 0:
        k = 0
    else:
        k = k % len(nums) # effective rotation amount

    rotatedList = []

    for i in range(len(nums) - k, len(nums)):
        rotatedList.append(nums[i])

    for i in range(0, len(nums) - k):
        rotatedList.append(nums[i])
        
    return rotatedList


def rotate(nums, k):
    rotatedList = []

    for i in range(len(nums)):
        rotatedList.append(nums[(i + k - 1) % len(nums)])

    return rotatedList


print(right_rotate([10, 20, 30, 40, 50], 3))
print(rotate([10, 20, 30, 40, 50, 60, 70], 3))