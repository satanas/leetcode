# Input: [1,2,3]
# []
# 1
# --
# [1]
# 2
# [2, 1], [1, 2]
# 3
# [3, 2, 1], [2, 3, 1], [2, 1, 3], [3, 1, 2], [1, 3, 2], [1, 2, 3]

class Solution:
    def permute(self, nums):
        result = [[]]
        for x in nums: # o(n)
            new_result = []
            for i in range(len(result)): # o(n * m)
                for j in range(len(result[i]) + 1): # o (n * m * k)
                    new_item = list(result[i])
                    new_item.insert(j, x)
                    new_result.append(new_item)
            result = new_result
        return result
                    

if __name__ == "__main__":
    s = Solution()
    s.permute([1,2,3])