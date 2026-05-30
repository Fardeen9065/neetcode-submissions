class Solution:
    def isValid(self, s: str) -> bool:
        if s == "":
            return True
        openn = ['(','{','[']
        close = [')','}',']']
        stack = []

        for i in s:
            if i in openn:
                stack.append(i)
            else:
                if len(stack) != 0:
                   elem = stack.pop()
                   if openn.index(elem) != close.index(i):
                      return False
                else:
                    return False

        if len(stack) == 0:
            return True
        if len(stack) != 0:
            return False

