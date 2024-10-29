def merge_lists(nums1, nums2): # O(m + n)
    result = [None] * (len(nums1)+len(nums2))
    p1 = 0
    p2 = 0
    p3 = 0

    while (p1 < len(nums1)) and (p2 < len(nums2)):
        if (nums1[p1] < nums2[p2]):
            result[p3] = nums1[p1]
            p1 += 1
            p3 += 1
        else:
            result[p3] = nums2[p2]
            p2 += 1
            p3 += 1
    while (p1 < len(nums1)):
        result[p3] = nums1[p1]
        p1 += 1
        p3 += 1
    while (p2 < len(nums2)):
        result[p3] = nums2[p2]
        p2 += 1
        p3 += 1
    return result

def merge_lists2(nums1, nums2): # O((m + n) * m)
    p1 = 0
    p2 = 0
    
    while (p1 < len(nums1)) and (p2 < len(nums2)):
        # If the value at p1 is greater than the value at p2, place the value at p2 into p1 and increment p1 and p2.
        if(nums1[p1] > nums2[p2]):
            nums1.insert(p1, nums2[p2])
            p1 += 1
            p2 += 1
        # Otherwise, increment p1
        else:
            p1 += 1

    # Append the remaining elements of nums2 into nums1
    if p2 < len(nums2):
        nums1.extend(nums2[p2:])
    
    return nums1

if __name__ == "__main__":
    l1 = [1, 2, 4, 5, 7, 10]
    l2 = [4, 6, 8, 9]

    print(merge_lists(l1, l2))
    print(merge_lists2(l1, l2))