def right_rotate(nums, k): # O(n)
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

def right_rotate2(nums, k): # O(n)
    if len(nums) == 0:
        k = 0
    else:
        k = k % len(nums)
    rotated_list = nums[-k:] + nums[:-k]

    return rotated_list

def rotate(nums, k): # O(n)
    rotatedList = []

    for i in range(len(nums)):
        rotatedList.append(nums[(i + k - 1) % len(nums)])

    return rotatedList


print(right_rotate([10, 20, 30, 40, 50], 3))
print(right_rotate2([10, 20, 30, 40, 50], 3))
print(rotate([10, 20, 30, 40, 50], 3))