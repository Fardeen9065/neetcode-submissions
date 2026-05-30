class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op = ['+','-','*','/']
        stack = []

        for elem in tokens:
            if elem not in op:
                stack.append(elem)
            else:
                if elem == '+':
                    num1 = int(stack.pop(-2))
                    num2 = int(stack.pop())
                    stack.append(num1+num2)
                elif elem == "-":
                    num1 = int(stack.pop(-2))
                    num2 = int(stack.pop())
                    stack.append(num1-num2)
                elif elem == "*":
                    num1 = int(stack.pop(-2))
                    num2 = int(stack.pop())
                    stack.append(num1*num2)
                else:
                    num1 = int(stack.pop(-2))
                    num2 = int(stack.pop())
                    stack.append(int(num1/num2))

        return int(stack[-1])




        