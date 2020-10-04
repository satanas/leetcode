# Iterate recursively passing the result from the previous calculation and interpreting the new value
# 1. 1
# 2. 11
# 5. 111221
# 6. 312211
# 7. 13112221

class Solution2:
    def countAndSay(self, n):
        if n == 1:
            return "1"
        
        return self.recursive_count("1", 2, n)
    
    def recursive_count(self, term, i, n):
        result = ""
        counter = 0
        stack = []

        for index in range(len(term)):
            # print(f"index: {index} - stack: {stack} - term[{index}]: {term[index]} - counter: {counter}")

            if len(stack) == 0:
                stack.append(term[index])
                counter += 1
                # print(f"counting - stack: {stack} - counter: {counter}")
                continue
            
            # Count
            if term[index] == stack[-1]:
                counter += 1
                # print(f"counting - stack: {stack} - counter: {counter}")
            # Say
            else:
                # print(f"===> saying: {counter}{stack[-1]} - stack: {stack} - counter: {counter}")
                result += f"{counter}{stack[-1]}"
                counter = 1

            stack.append(term[index])

        result += f"{counter}{stack[-1]}"
        
        if i == n:
            return result
        else:
            return self.recursive_count(result, i + 1, n)

# Using less memory
class Solution:
    def countAndSay(self, n):
        if n == 1:
            return "1"
        
        return self.recursive_count("1", 2, n)
    
    def recursive_count(self, term, i, n):
        result = ""
        counter = 0
        prev = None

        for index in range(len(term)):
            if prev is None:
                prev = term[index]
                counter += 1
                continue
            
            # Count
            if term[index] == prev:
                counter += 1
            # Say
            else:
                result += f"{counter}{prev}"
                counter = 1

            prev = term[index]

        result += f"{counter}{prev}"
        
        if i == n:
            return result
        else:
            return self.recursive_count(result, i + 1, n)
        
if __name__ == "__main__":
    s = Solution()
    print(s.countAndSay(6))