
class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        prev = None
        for i in range(len(nums)):
            curr = nums[i]
            if prev is None:
                prev = curr
            else:
                x = i
                while curr < prev:
                    nums[x] = prev
                    nums[x - 1] = curr
                    x -= 1
                    if x <= 0:
                        break
                    curr = nums[x]
                    prev = nums[x - 1]               
                    
                prev = nums[i]

if __name__ == "__main__":
    s = Solution()
    s.sortColors([2,0,2,1,1,0])
    s.sortColors([2,0,1,1,1,0])
    s.sortColors([1,0,2,1,2,0,1,2])
    s.sortColors([1,1,1,1,1])