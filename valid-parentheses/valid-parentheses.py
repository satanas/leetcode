# Assumptions:
# * "" is a valid a input
# * Characters can be nested
class Solution:
    openingChars = ['(', '{', '[']
    closingChars = [')', '}', ']']
    
    def isValid(self, s: str) -> bool: # O(n)
        stack = []
        for c in s:
            if c in self.openingChars:
                stack.append(c)
            if c in self.closingChars:
                if len(stack) == 0:
                    return False
                lastOpening = stack.pop()
                index = self.openingChars.index(lastOpening)
                expectedClosing = self.closingChars[index]
                
                if c != expectedClosing:
                    return False
        
        if len(stack) > 0:
            return False
        
        return True

if __name__ == "__main__":
    testCases = [
        "()",
        "{[]}()",
        "", 
        "([)]", 
        "{}{[}", 
        "{}{[}}", 
        "}}{}", 
        "}{", 
        "{{{{{{", 
        "{}}}"
    ]
    s = Solution()
    for t in testCases:
        print(s.isValid(t))

    