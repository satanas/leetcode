# Approach
# Sort the array and iterate it comparing the value of the num against its index
# If they're different, then the missing number is the index.

class Solution:
    def missingNumber(self, nums):
        sorted_nums = sorted(nums)

        # [0, 1] => [0, 1, 2]
        for i in range(len(sorted_nums)):
            if i != sorted_nums[i]:
                return i
        return len(sorted_nums)

if __name__ == "__main__":
    s = Solution()
    print(s.missingNumber([3,0,1]))
    print(s.missingNumber([0,1]))
    print(s.missingNumber([9,6,4,2,3,5,7,0,1]))
    print(s.missingNumber([0]))