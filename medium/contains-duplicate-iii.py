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

# Input: nums = [1,2,3,1], k = 3, t = 0
# Output: true

# len(array) = 4
# i = 0, j = 1, abs(1 - 2) = 1. Bigger than t, next
# i = 0, j = 2, abs(1 - 3) = 2. Bigger than t, next
# i = 0, j = 3, abs(1 - 1) = 0 => Equals to t, abs(0 - 3) = 3. Equals to k. Profit!

class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        if k == 0:
            return False
        print(len(nums))
        for i in range(len(nums) - 1):
            j = min(i + k + 1, len(nums))
            num = nums[i]
            subarray = nums[i + 1 : j]
            subarray = sorted(subarray)
            print(f"subarray: {subarray} - sorted subarray: {subarray} - k: {k} - j: {j} - i: {i}")
            h = 0
            while h < j - i - 1:
                print(f"num: {num} - subarray[{h}]: {subarray[h]} - abs: {abs(num - subarray[h])} - t: {t} - h: {h}")
                if abs(num - subarray[h]) <= t:
                    return True
                else:
                    h += 1
        return False

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