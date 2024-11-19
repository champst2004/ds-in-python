def rearrange_list(nums): # O(n)
    n = len(nums)
    new = [None] * n
    i = 0
    p1  = 0
    p2 = n - 1
    while i < n:
        if i % 2 == 0:
            new[i] = nums[p2]
            p2 -= 1
        else:
            new[i] = nums[p1]
            p1 += 1
        i += 1
    return new



def rearrange_list2(nums): # O(n)
    if (len(nums) == 0):
        return []    

    result = []
    mid = len(nums) // 2

    # Iterate through half of the sorted list
    for i in range(mid):
        # Append the largest remaining element (from the end of the list)
        result.append(nums[-(i+1)])
        # Append the smallest remaining element (from the start of the list)
        result.append(nums[i])

    if len(nums) % 2 == 1:
        result.append(nums[mid])

    return result

def rearrange_list(nums): # O(n)
    if (len(nums) == 0):
        return []

    # Initialize pointers to the start and end of the list
    max_idx = len(nums) - 1
    min_idx = 0
    # Initialize a variable larger than any element in the list to use for encoding
    max_elem = nums[len(nums) - 1] + 1

    # Encoding phase
    for i in range(len(nums)):
        if i % 2 == 0:  # Encoding at even indexes
            nums[i] += (nums[max_idx] % max_elem) * max_elem
            max_idx -= 1
        else:  # Encoding at odd indexes
            nums[i] += (nums[min_idx] % max_elem) * max_elem
            min_idx += 1

    # Decoding phase
    for i in range(len(nums)):
        nums[i] = nums[i] // max_elem

    return nums