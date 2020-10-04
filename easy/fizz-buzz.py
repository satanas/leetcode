# Iterate from 1 to n
# Check if number is multiple of 3 and 5, then of 3 and finally of 5 (using mod)
# Add the corresponding output to the result array

class Solution:
    def fizzBuzz(self, n):
        result = []
        for i in range(1, n + 1):
            word = str(i)
            if i % 3 == 0 and i % 5 == 0:
                word = "FizzBuzz"
            elif i % 3 == 0:
                word = "Fizz"
            elif i % 5 == 0:
                word = "Buzz"
            result.append(word)
        return result

if __name__ == "__main__":
    s = Solution()
    print(s.fizzBuzz(15))
