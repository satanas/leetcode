[1, 2, 6]
output = 2
[6, 1, 2]
output = 0
[1, 0, 1]
output = -1
[1, 0]
output = 0

# Brute force approach
# Iterate all elements and compare neighborgs

# check first case (overflow window from last to first two elements)

# for each element:
#     we check a window of 3 elements
#     if the middle one is bigger than its neighborgs, return the index
#     else continue moving the window 1 step

class Solution:
    def findPeakElement(self, nums):
        start = -1
        end = 1
        
        while end < len(nums):
            index = start + 1
            if nums[index] > nums[index + 1] and nums[index] > nums[index - 1]:
                return index
            else:
                start += 1
                end += 1

        # Check final overflow
        index = len(nums) - 1
        if nums[index] > nums[0] and nums[index] > nums[index - 1]:
            return index
        
        return 0
