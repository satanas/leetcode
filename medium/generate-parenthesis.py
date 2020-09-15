# Use subsets
# In each iteration, take the previous result set and apply a new parenthesis
# Then determine if a parenthesis can be added (tracking the number of open parentheses)
# + We cannot allow more closed parentheses that the ones we have opened
# + We cannot end up with an open parenthesis
# If valid, we add the new set to the result set
# We iterate until we have added 3 open parentheses.

class Solution1:
    def generateParenthesis(self, n):
        if n < 0:
            return []
        
        i = 0
        result = [""]

        while i < 2 * n:
            new_results = []
            #print(f"===> current results: {result}")
            for res in result:
                #print(f"processing res: {''.join(res)}")
                for p in ["(", ")"]:
                    new_item = list(res)
                    new_item.append(p)
                    if self.is_valid(new_item, n):
                        new_results.append(new_item)
            result = new_results
            i += 1

        return ["".join(r) for r in result]

    def is_valid(self, array, n):
        #print(f"validating: {''.join(array)}")
        opened = 0
        closed = 0
        for x in array:
            if x == "(":
                opened += 1
            else:
                closed += 1

            if closed > opened:
                #print(f"  false => o: {opened} - c: {closed}")
                return False
        
        if opened > n:
            #print(f"  false =>  o: {opened} - c: {closed}")
            return False
        #print(f"  true =>  o: {opened} - c: {closed}")
        return True

class Solution:
    def generateParenthesis(self, n):
        self.results = []
        self.recursive_generation("", 0, 0, n)
        return self.results

    def recursive_generation(self, elem, opening, closing, n):
        if opening - closing == 0 and len(elem) == 2 * n:
            self.results.append(elem)

        if opening < n:
            self.recursive_generation(elem + "(", opening + 1, closing, n)
        if closing < opening:
            self.recursive_generation(elem + ")", opening, closing + 1, n)

if __name__ == "__main__":
    s = Solution()
    print(s.generateParenthesis(3))
                



                
["("]
["((", "()"]
["(((", "(()", "()(", "())"]
["((()", "((((", "(()(", "(())", "()()", "()((", "()))", "())("]