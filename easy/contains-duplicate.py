# First approach
# Iterating all the elements and populating a hashmap with the frequency/occurence of each element
# If we encounter another element in the hashmap, we return true (dup)
# O(n) - O(n)

# Second approach
# Sort the array and iterate. If the previous element is the same than the current one, then return true

class Solution2:
    def containsDuplicate(self, nums):
        hashmap = {}
        for n in nums:
            if n in hashmap:
                return True
            else:
                hashmap[n] = True
        return False

class Solution:
    def containsDuplicate(self, nums):
        sorted_nums = sorted(nums)

        prev = None
        for n in sorted_nums:
            if n == prev:
                return True
            prev = n
        return False

if __name__ == "__main__":
    s = Solution()
    print(s.containsDuplicate([1,2,3,1]))
    print(s.containsDuplicate([1,2,3,4]))
    print(s.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))