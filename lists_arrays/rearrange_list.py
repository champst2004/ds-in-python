def rearrange(lst): # O(n)
  new = []
  for i in range(len(lst)):
    if lst[i] < 0:
      new.append(lst[i])
  for i in range(len(lst)):
    if lst[i] >= 0:
      new.append(lst[i])
  return new

def rearrange2(lst): # O(n)
    leftMostPosEle = 0 
    for i in range(len(lst)):
        # If negative number
        if lst[i] < 0:
            # If not the last negative number
            if i != leftMostPosEle:
                # Swap the two
                lst[i], lst[leftMostPosEle] = lst[leftMostPosEle], lst[i]
            # Update the last position
            leftMostPosEle += 1
    return lst

def rearrange3(lst):
    return [i for i in lst if i < 0] + [i for i in lst if i >= 0]

print(rearrange([-3, -10, -19, 21, -17]))
print(rearrange2([-3, -10, 19, 21, -17]))
print(rearrange3([-3, -10, 19, 21, -17]))