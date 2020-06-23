# Questions:
# 
class Solution:
    def singleNumber(self, nums):
        d = {}
        for n in nums:
            if n in d:
                d[n] = d[n] + 1
            else:
                d[n] = 1

        return [x for x, y in d.items() if y == 1][0]


if __name__ == "__main__":
    s = Solution()
    print(s.singleNumber([2,2,1]))
    print(s.singleNumber([4,1,2,1,2]))