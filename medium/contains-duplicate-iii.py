# Absolute difference means that it's >= 0
# Numbers can be negative

# We have two pointers, i and j
# We iterate through the whole array
# On each element:
# i starts on that element of the array (n)
# j starts on the n + 1 element
# As long as abs(nums[i] - nums[j]) <= t and j < len(array) - 1
#   we check if abs(i - j) <= k
#   if the condition is met, we return true
#   Otherwise, we increment j + 1

# Input: nums = [1,2,3,1], k = 3, t = 0
# Output: true

# len(array) = 4
# i = 0, j = 1, abs(1 - 2) = 1. Bigger than t, next
# i = 0, j = 2, abs(1 - 3) = 2. Bigger than t, next
# i = 0, j = 3, abs(1 - 1) = 0 => Equals to t, abs(0 - 3) = 3. Equals to k. Profit!

class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        for i in range(len(nums)):
            j = i + 1
            while j < len(nums):
                if abs(nums[i] - nums[j]) <= t and abs(i - j) <= k:
                    return True
                else:
                    j += 1
        return False

if __name__ == "__main__":
    s = Solution()
    print(s.containsNearbyAlmostDuplicate([1,2,3,1], 3, 0))
    print(s.containsNearbyAlmostDuplicate([1,0,1,1], 1, 2))
    print(s.containsNearbyAlmostDuplicate([1,5,9,1,5,9], 2, 3))
    print(s.containsNearbyAlmostDuplicate([], 2, 3))
    print(s.containsNearbyAlmostDuplicate([1,0,-1,1], 2, 1))