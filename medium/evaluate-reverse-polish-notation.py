# Input: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
# Find the first operator and take the two previous operands
# Resolve that operation and generate a new RPN, then repeat until no more operands are found
# Return the last operation executed

# ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]

# "9", "3", "+"
# pre = ["10", "6"]
# post = ["-11", "*", "/", "*", "17", "+", "5", "+"]
# "12"
# rebuild the array with the current operation solved, and repeat
# ["10", "6", "12", "-11", "*", "/", "*", "17", "+", "5", "+"]

# ["17", "5", "+"]
# 22

class Solution1:
    OPERATORS = ["+", "-", "*", "/"]

    def evalRPN(self, tokens):
        if len(tokens) == 1:
            return int(tokens[0])

        # Find first operator
        op_idx = self.find_operator(tokens)
        arg1_idx = op_idx - 2
        arg2_idx = op_idx - 1
        result = self.resolve_operation(tokens, arg1_idx, arg2_idx, op_idx)

        if len(tokens) == 3:
            return result
        else:
            new_token = tokens[:arg1_idx]
            new_token.append(str(result))
            new_token += tokens[op_idx + 1:]
            return self.evalRPN(new_token)

    def find_operator(self, tokens):
        for i, t in enumerate(tokens):
            if t in self.OPERATORS:
                return i
        return -1

    def resolve_operation(self, tokens, arg1_idx, arg2_idx, op_idx):
        int_result = 0
        if tokens[op_idx] == "+":
            int_result = int(tokens[arg1_idx]) + int(tokens[arg2_idx])
        elif tokens[op_idx] == "-":
            int_result = int(tokens[arg1_idx]) - int(tokens[arg2_idx])
        elif tokens[op_idx] == "*":
            int_result = int(tokens[arg1_idx]) * int(tokens[arg2_idx])
        elif tokens[op_idx] == "/":
            int_result = int(int(tokens[arg1_idx]) / int(tokens[arg2_idx]))
        return int_result

# Approach using a stack
class Solution:
    OPERATORS = ["+", "-", "*", "/"]

    def evalRPN(self, tokens):
        if len(tokens) == 1:
            return int(tokens[0])

        stack = []
        for t in tokens:
            if t in self.OPERATORS:
                arg2 = stack.pop()
                arg1 = stack.pop()
                result = self.resolve_operation(int(arg1), int(arg2), t)
                stack.append(str(result))
            else:
                stack.append(t)
        return stack.pop()

    def resolve_operation(self, arg1, arg2, operator):
        if operator == "+":
            return arg1 + arg2
        elif operator == "-":
            return arg1 - arg2
        elif operator == "*":
            return arg1 * arg2
        elif operator == "/":
            return int(arg1 / arg2)


if __name__ == "__main__":
    s = Solution()
    print(s.evalRPN(["2", "1", "+", "3", "*"]))
    print(s.evalRPN(["4", "13", "5", "/", "+"]))
    print(s.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))