def find_first_unique(nums): # O(n)
  x = {}
  for i in range(len(nums)):
    x[nums[i]] = 0
  for i in range(len(nums)):
    x[nums[i]] += 1
  for i in x:
    if x[i] == 1:
      return i
    
def find_first_unique2(nums): # O(n^2)
    # Iterate through each element in the list
    for p1 in range(len(nums)):
        p2 = 0
        
        # Compare the current element (p1) with all other elements (p2)
        while(p2 < len(nums)):
            if (p1 != p2 and nums[p1] == nums[p2]):
                break
            p2 += 1
        
        # If p2 reaches the end of the list, the element at p1 is unique
        if (p2 == len(nums)):
            return nums[p1]
    return None


lst = [1,1,2,2,3,3,4,5,5,6,7,8]
print(find_first_unique(lst))
print(find_first_unique2(lst))