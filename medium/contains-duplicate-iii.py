# Absolute difference means that it's >= 0
# Numbers can be negative

# First approach (too slow):
# We have two pointers, i and j
# We iterate through the whole array
# On each element:
# i starts on that element of the array (n)
# j starts on the n + 1 element
# As long as abs(nums[i] - nums[j]) <= t and j < len(array) - 1
#   we check if abs(i - j) <= k
#   if the condition is met, we return true
#   Otherwise, we increment j + 1

# Second approach:
# We iterate from i=0 to len(array) - 1:
# On each element:
# We get a subarray of k elements or the max number of avail. elements (starting from i)
# Sort the subarray and check if the first two elements fulfill the condition
# If true, then profit!
# Otherwise, we move to the next element of the array

# Third approach:
# Like the second but iterating through the subarray with a binary search tree

# Input: nums = [1,2,3,1], k = 3, t = 0
# Output: true

# len(array) = 4
# i = 0, j = 1, abs(1 - 2) = 1. Bigger than t, next
# i = 0, j = 2, abs(1 - 3) = 2. Bigger than t, next
# i = 0, j = 3, abs(1 - 1) = 0 => Equals to t, abs(0 - 3) = 3. Equals to k. Profit!

from sortedcontainers import SortedList

class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        if k <= 0 or t < 0:
            return False

        sorted_subarray = SortedList()
        for i, num in enumerate(nums):
            if i > k:
                sorted_subarray.remove(nums[i - k - 1])
                pos1 = bisect_left(sorted_subarray, num - t)
                pos2 = bisect_right(sorted_subarray, num + t)

                if pos1 != pos2:
                    return True
            sorted_subarray.add(num)
        return

            


if __name__ == "__main__":
    s = Solution()
    print(s.containsNearbyAlmostDuplicate([1,2,3,1], 3, 0))
    print(s.containsNearbyAlmostDuplicate([1,0,1,1], 1, 2))
    print(s.containsNearbyAlmostDuplicate([1,5,9,1,5,9], 2, 3))
    print(s.containsNearbyAlmostDuplicate([], 2, 3))
    print(s.containsNearbyAlmostDuplicate([1,0,-1,1], 2, 1))
    print(s.containsNearbyAlmostDuplicate([1, 2], 0, 1))
    print(s.containsNearbyAlmostDuplicate([7, 2, 8], 2, 1))
    print(s.containsNearbyAlmostDuplicate([-1,-1], 1, 0))
    print(s.containsNearbyAlmostDuplicate([2, 1], 1, 1))