class Solution:
    def removeDuplicates(self, nums):
        index = 0
        traverse_index = 0
        while traverse_index < len(nums) - 1:
            traverse_index = self.dedup(traverse_index, nums)
            if traverse_index is not None:
                index += 1
                nums[index] = nums[traverse_index]
            else:
                break
        return index + 1

    # Return the next non-identical number in the array
    def dedup(self, index, nums):
        original = nums[index]
        index += 1
        while nums[index] == original:
            if index + 1 >= len(nums):
                return None
            else:
                index += 1
        return index

if __name__ == "__main__":
    s = Solution()
    print(s.removeDuplicates([0, 0, 1, 1, 1, 2, 3, 3, 4]))
    print(s.removeDuplicates([0, 1, 2, 3, 4]))
    print(s.removeDuplicates([1, 1]))