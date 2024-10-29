def find_sum(nums, k): # O(n^2)
  for i in range(len(nums)):
    for j in range (i + 1, len(nums)):
      if nums[i] + nums[j] == k:
        return [nums[i], nums[j]]

def find_sum2(nums, k): # o(nlogn)
  nums.sort()
  soln = []
  left = 0
  right = len(nums) - 1
  while left < right:
    if k > nums[left] + nums[right]:
      left += 1
    if k < nums[left] + nums[right]:
      right -= 1
    else:
      soln.append(nums[left])
      soln.append(nums[right])
      break
  return soln

print(find_sum([2,3,5,9], 8))
print(find_sum2([2,3,5,9], 8))