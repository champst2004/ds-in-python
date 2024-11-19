def find_max_sum_sublist(nums): # O(n)
    max_sum = float("-inf")
    curr_sum = float("-inf")

    for num in nums:
        curr_sum = max(num, curr_sum + num)
        max_sum = max(curr_sum, max_sum)

    return max_sum

def find_max_sum_sublist(nums): # O(n)
    if len(nums) < 1: 
        return 0

    curr_max = nums[0]
    global_max = nums[0]
    
    for i in range(1, len(nums)):
        if curr_max < 0: 
            curr_max = nums[i]
        else:
            curr_max += nums[i]
        if global_max < curr_max:
            global_max = curr_max

    return global_max