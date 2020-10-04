# First obtain the subset of numbers that are less or equal than n
# Start generating all the possible combinations of the numbers in the subset
# Once we find n, we return the length of the subset

# n = 12
# subset = [1, 4, 9]
# combinations = [[]]

# while True:
#     for each c in combinations: # [[1, 1], [4, 1], [9, 1], [1, 4], [4, 4], [4, 9], [1, 9], [4, 9]]
#         new_combinations = []
#         for each x in subset: # 1
#             new_c = list(c) # [1]
#             new_c.append(x) # [1, 9]
#             if sum of elem in new_c == n:
#                 return len(new_c)
#             elif sum of elem in new_c is < n
#                 new_combinations.append(new_c) # [[1, 1, 1], [1, 1, 4], [1, 1, 9]]
#         combinations = new_combinations
    
from functools import reduce

class Solution:
    def numSquares(self, n):
        subset = self.get_subset(n)
        combinations = [[]]
        while True:
            for c in combinations:
                new_combinations = []
                for x in subset:
                    new_c = list(c)
                    print(f"processing x = {x} with {new_c}")
                    new_c.append(x)
                    sum_c = self.get_sum(new_c)
                    if sum_c == n:
                        return len(new_c)
                    if sum_c < n:
                        new_combinations.append(new_c)
                combinations = new_combinations

    def get_subset(self, n):
        i = 1
        result = 1
        subset = []
        while result < n:
            subset.append(result)
            i += 1
            result = i * i
        return subset

    def get_sum(self, array):
        print(f"calculating sum in {array}")
        return reduce(lambda x, y: x + y, array)

if __name__ == "__main__":
    s = Solution()
    s.numSquares(12)