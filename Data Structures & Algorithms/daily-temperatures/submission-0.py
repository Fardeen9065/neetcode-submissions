class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp = [0]*len(temperatures)
        stack = []

        for i,num in enumerate(temperatures):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                idx = stack.pop()
                temp[idx] = i -idx
            stack.append(i)

        return temp
        