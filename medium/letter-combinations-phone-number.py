class Solution:
    LETTERS = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }
    def letterCombinations(self, digits):
        if digits == "":
            return []
            
        result = [""]
        for num in digits:
            new_results = []
            for r in result:
                for letter in self.LETTERS[num]:
                    new_item = r + letter
                    new_results.append(new_item)
            result = new_results
        return result


if __name__ == "__main__":
    s = Solution()
    print(s.letterCombinations("23"))
    print(s.letterCombinations("234"))