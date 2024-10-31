def find_product(nums): # O(n^2)
  product = []
  i = 0
  while i < len(nums):
    pdt = 1
    for j in range(len(nums)):
      if i == j:
        continue
      else:
        pdt *= nums[j]
    i += 1
    product.append(pdt)
  return product

def find_product2(nums): # O(n^2)
    product = []
    left = 1  
    
    for i in range(len(nums)):
        current_product = 1 
     
        for values in nums[i+1:]:
            current_product *= values

        product.append(current_product * left)
        left *= nums[i]

    return product

def find_product3(nums): # O(n)
    left = 1
    product = []
    # First pass: Calculate products starting from left
    for values in nums:
        product.append(left)
        left = left * values
    #print(product)
        
    # Second pass: Update the product list by calculating products from right to left
    right = 1
    for i in range(len(nums)-1, -1, -1):
        product[i] = product[i] * right
        right = right * nums[i]
    #print(product)

    return product

find_product3([1, 2, 3, 4, 5])