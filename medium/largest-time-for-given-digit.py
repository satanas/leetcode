# Assume it's not sorted
# array length == 4
# 0 <= a[i] <= 9
# return empty if no valid time is possible

# smallest time = 00:00
# largest time = 23:59

# Input: [1,2,3,4]
# Output: "23:41"
# Input: [0,2,9,4]
# Output: "09:42"
# Input: [0,7,9,7]
# Output: ""
# Input: [0,5,9,7]
# Output: "09:57"

# 1) Calculate all possible permutations
# 2) Filter the invalid permutations
# 3) If no permutations are valid, return ""
# 4) Otherwise, calculate the number of seconds (since midnight) of each remaining permutation
# 5) Store a reference to the largest one
# 6) Construct the response string and return it

from collections import deque

class Solution:
    def largestTimeFromDigits(self, array):
        permutations = self.calculate_permutations(array)
        # print(f"permutations: {permutations}")
        valid_permutations = list(filter(self.is_valid_array, permutations))
        # print(f"valid permutations: {valid_permutations}")
        if len(valid_permutations) == 0:
            return ""
        largest_time = None
        largest_time_in_minutes = -1
        for x in valid_permutations:
            minutes = self.calculate_minutes(x)
            # print(f" - minutes for {x}: {minutes}")
            if minutes > largest_time_in_minutes:
                largest_time_in_minutes = minutes
                largest_time = x
        return self.build_response(largest_time)

    def calculate_permutations(self, array):
        results = []
        permutations = deque()
        permutations.append(results)

        for num in array:
            n = len(permutations)
            for j in range(n):
                p = permutations.popleft()
                # print(f"checking permutation: {p} - j: {j} - num: {num}")
                for i in range(len(p) + 1):
                    new_perm = list(p)
                    new_perm.insert(i, num)
                    if len(new_perm) == 4:
                        results.append(new_perm)
                    else:
                        permutations.append(new_perm)

        return results


    def is_valid_array(self, a):
        hours = (a[0] * 10) + a[1]
        minutes = (a[2] * 10) + a[3]

        if hours <= 23 and minutes <= 59:
            return True
        else:
            return False

    def calculate_minutes(self, a):
        hours = (a[0] * 10) + a[1]
        minutes = (a[2] * 10) + a[3]
        return minutes + (hours * 60)

    def build_response(self, a):
        return f"{a[0]}{a[1]}:{a[2]}{a[3]}"

if __name__ == "__main__":
    s = Solution()
    print(s.largestTimeFromDigits([1,2,3,4]))
    print(s.largestTimeFromDigits([0,2,9,4]))
    print(s.largestTimeFromDigits([0,7,9,7]))
    print(s.largestTimeFromDigits([0,5,9,7]))
    print(s.largestTimeFromDigits([5,5,5,5]))
    print(s.largestTimeFromDigits([0,0,0,0]))