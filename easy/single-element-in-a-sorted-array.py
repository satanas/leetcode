def single_non_duplicate(nums): 

  # We perform a binary search and get the middle index, then we make it even.
  # If both numbers are equal, means everything is balanced in that half, so
  # we move to the other half.
  start = 0
  end = len(nums)

  while start != end:
    middle = start + ((end - start) // 2)
    if middle % 2 != 0:
      middle -= 1
    
    # All good in the first half of the array
    if nums[middle] == nums[middle + 1]:
      start = middle + 2
    else:
      end = middle - 1

  return nums[start]

if __name__ == "__main__":
    # print(single_non_duplicate([1,1,2,2,3,3,4,4,5,8,8]))
    print(single_non_duplicate([1,1,4,4,7,7,10,10,13,13,16,16,19,19,22,22,25]))